from sudoku.cell import Cell

def coord_to_index(ligne, colonne):
    if ligne < 0 or ligne >8 or colonne < 0 or colonne > 8:
        return -1
    return 9 * ligne + colonne


def index_to_coord(index):
    if index < 0 or index > 80:
        return -1
    return index // 9, index % 9


def flatten_grid(grid):
    flattenGrid = []
    for l in range(9):
        for c in range(9):
            flattenGrid.append(grid[l][c])
    return flattenGrid

def create_cells(solution_aplatie):
    if len(solution_aplatie) != 81:
        raise ValueError("Message d'erreur")
    cells = []
    for i in range(len(solution_aplatie)):
        cell = Cell(i, solution_aplatie[i])
        cells.append(cell)
    return cells

def generate_all_randomness(cells, q):
    for cell in cells:
        cell.generate_randomness(q)
    return cells


def get_public_grid(grid):
    publicGrid = []
    for l in range(9):
        for c in range(9):
            if grid[l][c] != 0:
                publicGrid.append((l,c,grid[l][c]))
    return publicGrid

def get_cell_by_index(cells, index):
    """
    Récupère l'objet Cell correspondant à un indice donné.
    """
    
    
def get_solution_as_grid(cells):
    """
    Reconstruit une grille 9×9 à partir de la liste des cellules.
    """



"""
solution_aplatie = flatten_grid(grid)

cells = create_cells(solution_aplatie)
cells = generate_all_randomness(cells, 100)

for cell in cells:
    print(cell.index, cell.value, cell.randomness)
"""


