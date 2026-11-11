grid = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
        [3, 4, 5, 1, 1, 1, 1, 1, 1],
        [6, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4, 4, 4],
        [5, 1, 1, 1, 1, 1, 1, 1, 1],
        [6, 2, 2, 2, 2, 2, 2, 2, 2],
        [7, 3, 3, 3, 3, 3, 3, 3, 3],
        [8, 4, 4, 4, 4, 4, 4, 4, 4]]


#ajouter test si décimal ou non
def Is_grid(grid : list) -> bool:
    #vérifie que le tableau possède 9 lignes
    if len(grid) != 9:
        print("erreur ligne")
        return False
    #vérifie le bon nombre de colonnes
    for line in grid:
        if len(line) != 9:
            print("erreur colonne")
            return False
        for val in line:
            if not isinstance(val, int):
                print("erreur type")
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
                
"""  
print(Is_grid(grid))
print(Check_rows(grid))
print(Check_columns(grid))
print(Check_blocs(grid))
"""
