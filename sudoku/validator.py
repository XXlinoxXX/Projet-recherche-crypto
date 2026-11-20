from constraints import *

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
        