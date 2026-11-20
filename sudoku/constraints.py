#ajouter test si décimal ou non
def Is_grid(grid : list) -> bool:
    #vérifie que le tableau possède 9 lignes
    if len(grid) != 9:
        return False
    #vérifie le bon nombre de colonnes
    for line in grid:
        if len(line) != 9:
            return False
        for val in line:
            if not isinstance(val, int):
                return False
    return True


def Check_rows(grid : list) -> bool:
    for i in range(9):
        numbers = []
        for num in grid[i]:
            if num == 0:
                continue
            elif num in numbers or num < 0 or num > 9:
                return False
            else:
                numbers.append(num)
    return True
    

def Check_columns(grid : list) -> bool:
    for i in range(9):
        numbers = []
        for j in range(9):
            num = grid[j][i]
            if num == 0:
                continue
            elif num in numbers or num < 0 or num > 9:
                return False
            else:
                numbers.append(num)
    return True


def Check_blocs(grid : list) -> bool:
    #3 lignes de blocs, lignes 0-2, lignes 3-5, lignes 6-8
    for i in range(3):
        #3 colonnes de blocs, col. 0-2, col. 3-5, col. 6-8
        for j in range(3):
            numbers = []
            for a in range(3):
                for b in range(3):
                    num = grid[3*i+a][3*j+b]
                    if num == 0:
                        continue
                    elif num in numbers or num < 0 or num > 9:
                        return False
                    else:
                        numbers.append(num)
    return True

def Check_initial_values(grid, solution) -> bool:
    """
    Vérifie que la solution conserve toutes les valeurs initialement données.
    """
    
    if not Is_grid(grid) or not Is_grid(solution):
        return False
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                if grid[i][j] != solution[i][j]:
                    return False
    return True


def get_row(grid, row_index):
    """Retourne les neuf valeurs d'une ligne donnée."""
    
    
def get_column(grid, column_index):
    """Retourne les neuf valeurs d'une colonne donnée."""
    
    
def get_block(grid, block_index):
    """Retourne les neuf valeurs d'un bloc 3×3 donné."""
    
    
def get_all_constraints(grid):
    """Retourne les 27 contraintes du Sudoku : 9 lignes, 9 colonnes et 9 blocs."""
    
    

