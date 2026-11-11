"""Partie PROUVEUR (Alice).

Déroulement (chaque preuve se fait en 3 messages : Alice envoie, Bob défie, Alice répond) :
  1. commit_grid()                              -> 81 engagements, envoyés à Bob (UNE seule fois)
  2. start_clue_proofs()   puis answer_clue_proofs(e)   -> preuves pour les cases pré-remplies
  3. start_round(numero)   puis answer_round(e)         -> preuves pour UNE contrainte (0 à 26)
     choisie par Bob ; on répète l'étape 3 plusieurs fois.
Le défi e est choisi au hasard par Bob dans [0, Q).
"""
import secrets
from itertools import combinations

from constraints import Is_grid, Check_rows, Check_columns, Check_blocs
from commun import Q, P, H, CHIFFRES, DIFFERENCES, engagement, decale, quotient, contraintes


# ============================================================================
# Preuve de Schnorr : « je connais s tel que Y = H^s » (sans révéler s)
# ============================================================================
def schnorr_start(s):
    w = secrets.randbelow(Q)                 # nonce : aléa temporaire, JAMAIS réutilisé
    return pow(H, w, P), (w, s)              # message A = H^w, et l'état secret à garder


def schnorr_answer(etat, e):
    w, s = etat
    return (w + e * s) % Q                   # z = w + e·s


# ============================================================================
# Preuve OU : « l'une des cibles Y_j vaut H^s » (sans révéler laquelle)
# ============================================================================
def or_start(cibles, k, s):
    """cibles : les Y_j ; k : la branche vraie ; s : le secret de la branche vraie (Y_k = H^s).

    Branche vraie  -> vraie preuve de Schnorr.
    Autres branches -> preuves SIMULÉES : on choisit e_j et z_j au hasard, puis on en déduit A_j.
    Bob ne peut pas distinguer la vraie branche des fausses.
    """
    w = secrets.randbelow(Q)
    e = [0] * len(cibles)
    z = [0] * len(cibles)
    A = []
    for j, Y in enumerate(cibles):
        if j == k:
            A.append(pow(H, w, P))
        else:
            e[j], z[j] = secrets.randbelow(Q), secrets.randbelow(Q)
            A.append(pow(H, z[j], P) * pow(Y, (-e[j]) % Q, P) % P)   # A_j = H^z_j · Y_j^(-e_j)
    return A, (w, e, z, k, s)


def or_answer(etat, defi):
    """Les défis e_j doivent s'additionner au défi de Bob : c'est ce qui empêche de tout simuler."""
    w, e, z, k, s = etat
    e[k] = (defi - sum(e)) % Q               # (e[k] vaut 0 ici : sum(e) = somme des autres)
    z[k] = (w + e[k] * s) % Q
    return e, z


# ============================================================================
# Le prouveur
# ============================================================================
def _verifier_entrees(solution, grille):
    """Alice refuse de travailler avec des données incohérentes."""
    for nom, g in (("solution", solution), ("grille initiale", grille)):
        if not Is_grid(g):
            raise ValueError(f"{nom} : il faut une grille 9x9 d'entiers")
        if any(isinstance(v, bool) for ligne in g for v in ligne):
            raise ValueError(f"{nom} : les booléens sont refusés")
        if not (Check_rows(g) and Check_columns(g) and Check_blocs(g)):
            raise ValueError(f"{nom} : doublon ou valeur hors de 1..9")
    if any(v == 0 for ligne in solution for v in ligne):
        raise ValueError("la solution doit être complète (aucun 0)")
    for i in range(9):
        for j in range(9):
            if grille[i][j] not in (0, solution[i][j]):
                raise ValueError(f"l'indice en ({i}, {j}) ne correspond pas à la solution")


def _verifier_defi(e):
    if not isinstance(e, int) or not 0 <= e < Q:
        raise ValueError("défi invalide : entier attendu dans [0, Q)")


class Prover:
    def __init__(self, solution, grille_initiale):
        _verifier_entrees(solution, grille_initiale)
        self._solution = [ligne[:] for ligne in solution]       # SECRET
        self._grille = [ligne[:] for ligne in grille_initiale]  # public (0 = case vide)
        self._contraintes = contraintes()
        self._r = None            # SECRET : un aléa par case
        self._C = None            # engagements (publics une fois envoyés)
        self._etat_indices = None
        self._etat_tour = None

    # --- Étape 1 -------------------------------------------------------------
    def commit_grid(self):
        """Engage les 81 cases : C(i,j) = G^chiffre · H^r(i,j). Possible une seule fois."""
        if self._C is not None:
            raise RuntimeError("les engagements sont déjà fixés pour cette session")
        self._r = [[secrets.randbelow(Q) for _ in range(9)] for _ in range(9)]
        self._C = [[engagement(self._solution[i][j], self._r[i][j]) for j in range(9)]
                   for i in range(9)]
        return [ligne[:] for ligne in self._C]

    # --- Étape 2 : indices pré-remplis ---------------------------------------
    def start_clue_proofs(self):
        """Pour un indice c : C·G^(-c) = H^r. Alice prouve (Schnorr) qu'elle connaît r."""
        if self._C is None:
            raise RuntimeError("appelez d'abord commit_grid()")
        self._etat_indices, messages = {}, {}
        for i in range(9):
            for j in range(9):
                if self._grille[i][j] != 0:
                    messages[(i, j)], self._etat_indices[(i, j)] = schnorr_start(self._r[i][j])
        return messages

    def answer_clue_proofs(self, e):
        if self._etat_indices is None:
            raise RuntimeError("appelez d'abord start_clue_proofs()")
        _verifier_defi(e)
        etats, self._etat_indices = self._etat_indices, None    # un nonce ne sert qu'une fois
        return {case: schnorr_answer(etat, e) for case, etat in etats.items()}

    # --- Étape 3 : une contrainte (ligne, colonne ou bloc) -------------------
    def start_round(self, numero):
        """Bob a choisi la contrainte `numero`. Alice prépare, pour ses 9 cases :
          - 9 preuves « la case contient un chiffre de 1..9 »   (OU à 9 branches)
          - 36 preuves « ces deux cases sont différentes »      (OU à 16 branches, une par paire)
        Ensemble : 9 valeurs dans 1..9, toutes distinctes  =>  exactement 1..9.
        """
        if self._C is None:
            raise RuntimeError("appelez d'abord commit_grid()")
        if not isinstance(numero, int) or not 0 <= numero < 27:
            raise ValueError("numéro de contrainte invalide (0 à 26)")
        cases = self._contraintes[numero]
        C = [self._C[i][j] for i, j in cases]
        x = [self._solution[i][j] for i, j in cases]
        r = [self._r[i][j] for i, j in cases]

        appartenance, msg_appartenance = [], []
        for pos in range(9):
            cibles = [decale(C[pos], d) for d in CHIFFRES]       # la vraie vaut H^r
            A, etat = or_start(cibles, CHIFFRES.index(x[pos]), r[pos])
            msg_appartenance.append(A)
            appartenance.append(etat)

        difference, msg_difference = {}, {}
        for a, b in combinations(range(9), 2):
            D = quotient(C[a], C[b])                             # engage x_a - x_b
            cibles = [decale(D, delta) for delta in DIFFERENCES]  # la vraie vaut H^(r_a - r_b)
            k = DIFFERENCES.index(x[a] - x[b])                   # existe car x_a != x_b
            msg_difference[(a, b)], difference[(a, b)] = or_start(cibles, k, (r[a] - r[b]) % Q)

        self._etat_tour = (appartenance, difference)
        return {"contrainte": numero, "appartenance": msg_appartenance, "difference": msg_difference}

    def answer_round(self, e):
        if self._etat_tour is None:
            raise RuntimeError("appelez d'abord start_round()")
        _verifier_defi(e)
        (appartenance, difference), self._etat_tour = self._etat_tour, None   # nonces à usage unique
        return {"appartenance": [or_answer(etat, e) for etat in appartenance],
                "difference": {paire: or_answer(etat, e) for paire, etat in difference.items()}}
