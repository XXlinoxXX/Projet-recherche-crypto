


"""
Module implémentant les preuves OR de Schnorr.

Une preuve OR permet au Prover de démontrer qu'il connaît le secret
associé à au moins une relation parmi plusieurs, sans révéler laquelle.

Dans notre projet Sudoku, elle permet notamment de prouver qu'une
cellule contient une valeur comprise entre 1 et 9, sans révéler
la valeur exacte.
"""


def compute_candidate_statements(commitment, candidates, params):
    """
    Calcule les statements publics correspondant aux différentes
    valeurs candidates.

    Pour chaque valeur d, on calcule :

        Y_d = C * g^(-d) mod p

    Si la valeur secrète de la cellule est égale à d, alors :

        Y_d = h^r mod p

    Le Prover connaît donc l'aléa r associé à cette relation.

    Args:
        commitment : engagement de Pedersen de la cellule.
        candidates : liste des valeurs candidates (ex : 1 à 9).
        params : paramètres publics de Pedersen (p, q, g, h).

    Returns:
        Liste des statements publics, un par valeur candidate.
    """
    pass


def generate_simulated_branch(statement, challenge, response, params):
    """
    Génère une branche simulée de la preuve OR.

    Le Prover ne connaît pas le secret associé à cette branche.
    Il choisit donc un défi et une réponse, puis reconstruit
    l'engagement Schnorr correspondant.

    Pour une relation Y = h^r, la reconstruction est :

        A = h^z * Y^(-e) mod p

    Cette opération permet de simuler une preuve sans connaître r.

    Args:
        statement : statement public de la branche.
        challenge : défi attribué à cette branche.
        response : réponse choisie pour cette branche.
        params : paramètres publics.

    Returns:
        L'engagement Schnorr simulé de la branche.
    """
    pass


def generate_real_branch(randomness, nonce, params):
    """
    Génère l'engagement de la branche réelle.

    La branche réelle correspond à la valeur effectivement contenue
    dans la cellule. Le Prover connaît l'aléa randomness associé.

    Il choisit un nonce secret w et calcule :

        A = h^w mod p

    Contrairement aux branches simulées, cette branche est construite
    à partir du véritable secret connu par le Prover.

    Args:
        randomness : aléa secret r de l'engagement Pedersen.
        nonce : nonce secret w généré pour cette preuve.
        params : paramètres publics.

    Returns:
        L'engagement Schnorr de la branche réelle.
    """
    pass


def generate_branch_challenges(global_challenge, simulated_challenges, q):
    """
    Calcule le défi de la branche réelle.

    Dans une preuve OR de Schnorr, la somme de tous les défis
    individuels doit être égale au défi global modulo q :

        e_global = somme(e_i) mod q

    Les défis des branches simulées sont choisis par le Prover.
    Le défi de la branche réelle est ensuite déduit afin de
    respecter cette égalité.

    Args:
        global_challenge : défi global envoyé par le Verifier.
        simulated_challenges : défis des branches simulées.
        q : ordre du sous-groupe.

    Returns:
        Défi de la branche réelle modulo q.
    """
    pass


def generate_branch_responses(randomness, nonce, challenge, q):
    """
    Calcule la réponse de la branche réelle.

    Cette fonction applique la formule de Schnorr :

        z = w + e * r mod q

    Le Prover utilise son aléa secret r, son nonce w et le défi
    de la branche réelle.

    Args:
        randomness : aléa secret r.
        nonce : nonce secret w.
        challenge : défi de la branche réelle.
        q : ordre du sous-groupe.

    Returns:
        Réponse z de la branche réelle.
    """
    pass


def generate_or_proof(commitment, value, randomness, candidates, params):
    """
    Construit une preuve OR complète.

    Le Prover construit une branche pour chaque valeur candidate.

    - Une branche est réelle : elle correspond à la valeur secrète.
    - Les autres branches sont simulées.
    - Les défis individuels sont liés par le défi global.
    - Les réponses sont calculées pour chaque branche.

    La preuve rassemble les engagements, les défis et les réponses
    de toutes les branches.

    Args:
        commitment : engagement de Pedersen de la cellule.
        value : valeur secrète de la cellule.
        randomness : aléa secret associé à l'engagement.
        candidates : valeurs candidates (ex : 1 à 9).
        params : paramètres publics.

    Returns:
        Structure contenant les éléments nécessaires à la
        vérification de la preuve OR.

    Attention :
        Le nonce de la branche réelle doit être frais et ne jamais
        être réutilisé pour une autre preuve.
    """
    pass


def verify_or_proof(commitment, candidates, proof, params):
    """
    Vérifie une preuve OR.

    Le Verifier :
    1. Recalcule les statements publics des branches.
    2. Vérifie chaque relation de Schnorr.
    3. Vérifie que la somme des défis individuels correspond
       au défi global modulo q.

    Si toutes les vérifications réussissent, la preuve démontre
    que le Prover connaît le secret associé à au moins une
    des valeurs candidates.

    Args:
        commitment : engagement public de Pedersen.
        candidates : valeurs candidates utilisées.
        proof : structure contenant les engagements, défis,
                réponses et défi global.
        params : paramètres publics.

    Returns:
        True si la preuve est valide, False sinon.
    """
    pass


