"""Éléments PUBLICS, partagés par Alice (prouveur) et Bob (vérifieur).

Contient : le groupe mathématique, les engagements de Pedersen et la liste des 27 contraintes.
"""
import hashlib

# --- Le groupe ---------------------------------------------------------------
# Les éléments se calculent modulo P, les exposants modulo Q.
# P et Q sont premiers, Q divise P-1, et G est un élément d'ordre Q.
# (Valeurs générées une fois avec un test de primalité de Miller-Rabin.)
P = 0x939002de520dc5e256904caf9d141ed5ada38f8f2209c7e828820ece31a719a24b9f433dd6fe228c1555bd9c17cf9f57346b07369b76adf23e20a5650c1f5b495a94b0d1b1f2e1fa7a2704e477e7d7b792e3ea763ae654ea0dcf271573fedf9af8b537575f66e5cc78376fc0a4e9c251e45c8676b813069d4b792d811f6439d7d1d43809cde3e8cff308f8c3085cd58056cf9490940384c1ac79327d9252a4b95022408a9921528e94b8e818a0767e7a0e008b9ec154fa5bc96c6d2a7aeef589d47917684bbbb795641e5c83891d1eb38aede9817814874c12f6303d0b637d839a715f0adf3cab069dc5c6a9ed3d7630882c98eb6714c74a03a739dd78913a2b
Q = 0x80f69dec1ae83cbd344c4c283512089286759cb027d4b5776324e64a68d906a3
G = 0x154ee18f5d24a58ff88a51df555a0d8487e28cd416a7cfb896ea50699f62b1fa0a897f3ab54c1d00a209691465223a9fc0a1eb547b998859b92ed2fd839a4efcbd9cc2f678c1913ea3c45976b2f00b7b0943270b9607cb26a69c4d6e79017189ff2db89044a58159213434d7032357f4b4600446b7ac15ba48a43c7c4ce1b0ea75fe271b9afdfe8b03877201e74bd1e2a2f2fae3390e42e7e10c2fc5dc9057177045c749ecc508a5be15768d2d74968148f8beae2b845880fb4494610adf0750a4c202eb462ff5255ab9c35b00d5cbab4f8025d4ea21c0143c3d6264103663ba07426db6be913d83e100fcce6f9f601458b6579f167b340968bf1575578b4ade


def _calcule_h():
    """Second générateur H, dérivé d'un hash d'une phrase publique.

    Il faut que PERSONNE ne connaisse x tel que H = G^x : sinon Alice pourrait ouvrir
    un même engagement avec deux chiffres différents (le « binding » serait cassé).
    """
    compteur = 0
    while True:
        brut = hashlib.shake_256(b"zkp-sudoku-h" + bytes([compteur])).digest(264)
        h = pow(int.from_bytes(brut, "big") % P, (P - 1) // Q, P)  # on le met dans le groupe d'ordre Q
        if h != 1:
            return h
        compteur += 1


H = _calcule_h()

# Valeurs possibles d'une case, et différences possibles entre deux cases distinctes.
# L'ORDRE de ces listes est public : c'est l'ordre des branches des preuves OU.
CHIFFRES = list(range(1, 10))                              # 1..9
DIFFERENCES = [d for d in range(-8, 9) if d != 0]          # -8..-1 et 1..8 (16 valeurs)

# G^(-d), pré-calculé pour ne pas le refaire des centaines de fois
G_MOINS = {d: pow(G, (-d) % Q, P) for d in range(-9, 10)}


# --- Engagements de Pedersen -------------------------------------------------
def engagement(m, r):
    """C = G^m · H^r : la « boîte verrouillée » qui contient m, fermée avec l'aléa r."""
    return pow(G, m % Q, P) * pow(H, r % Q, P) % P


def decale(C, d):
    """C · G^(-d). Si C contient m, le résultat contient m-d. Si m == d, il vaut H^r."""
    return C * G_MOINS[d] % P


def quotient(C_a, C_b):
    """C_a / C_b : engagement de (x_a - x_b), avec l'aléa (r_a - r_b)."""
    return C_a * pow(C_b, -1, P) % P


# --- Les 27 contraintes ------------------------------------------------------
def contraintes():
    """Liste des 27 contraintes, chacune = liste de ses 9 cases (ligne, colonne).
    Numéros : 0-8 lignes, 9-17 colonnes, 18-26 blocs 3x3."""
    lignes = [[(i, j) for j in range(9)] for i in range(9)]
    colonnes = [[(i, j) for i in range(9)] for j in range(9)]
    blocs = [[(3 * bi + a, 3 * bj + b) for a in range(3) for b in range(3)]
             for bi in range(3) for bj in range(3)]
    return lignes + colonnes + blocs
