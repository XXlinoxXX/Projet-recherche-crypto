def create_commitment(m, r, params):
    value_commitment = pow(params.g, m, params.p)
    randomness_commitment = pow(params.h, r, params.p)
    return value_commitment * randomness_commitment % params.p

def create_all_commitments(cells, params):
    for cell in cells:
        cell.commitment = create_commitment(cell.value,
                                            cell.randomness,
                                            params)
    return cells


def get_all_commitments(cells):
    commitments = []
    for cell in cells:
        commitments.append(cell.commitment)
    return commitments


def get_indexed_commitments(cells):
    return [(cell.index, cell.commitment) for cell in cells]


def get_commitment_by_index(indexed_commitments, index):
    for commitment  in indexed_commitments:
        if commitment[0] == index:
            return commitment[1]




"""
from sudoku.representation import create_cells, generate_all_randomness
from sudoku.cell import Cell

# Grille fictive de 81 valeurs
solution_aplatie = [(i % 9) + 1 for i in range(81)]

# Création des 81 objets Cell
cells = create_cells(solution_aplatie)

params = PedersenParameters(1, 2, 3, 4)
# Génération des aléas privés
cells = generate_all_randomness(cells, params.q)

# Création des engagements
cells = create_all_commitments(cells, params)


print("Nombre de cellules :", len(cells))

for cell in cells:
    print(
        "Index :", cell.index,
        "| Valeur :", cell.value,
        "| Aléa :", cell.randomness,
        "| Engagement :", cell.commitment
    )
 """       