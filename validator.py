from constraints import *

#préparer plusieurs grilles différentes (tests)
grid = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
        [3, 4, 5, 1, 1, 1, 1, 1, 1],
        [6, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4, 4, 4],
        [5, 1, 1, 1, 1, 1, 1, 1, 1],
        [6, 2, 2, 2, 2, 2, 2, 2, 2],
        [7, 3, 3, 3, 3, 3, 3, 3, 3],
        [8, 4, 4, 4, 4, 4, 4, 4, 4]]


def Validate_sudoku(grid : list) -> bool:
    if not Is_grid(grid):
        return False
    if not Check_rows(grid):
        return False
    if not Check_columns(grid):
        return False
    if not Check_blocs(grid):
        return False
    return True
    

print( Validate_sudoku(grid))
    