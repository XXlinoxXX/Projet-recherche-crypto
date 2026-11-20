solution_valide = [
    [3, 5, 6, 8, 1, 9, 7, 4, 2],
    [2, 9, 7, 4, 5, 6, 8, 3, 1],
    [4, 8, 1, 2, 7, 3, 6, 9, 5],
    [5, 1, 3, 7, 8, 2, 9, 6, 4],
    [8, 6, 2, 5, 9, 4, 3, 1, 7],
    [9, 7, 4, 6, 3, 1, 2, 5, 8],
    [1, 2, 8, 3, 6, 5, 4, 7, 9],
    [7, 3, 5, 9, 4, 8, 1, 2, 6],
    [6, 4, 9, 1, 2, 7, 5, 8, 3],
]


# doublon sur une ligne.
solution_doublon_ligne = [ligne[:] for ligne in solution_valide]
solution_doublon_ligne[0][0] = solution_doublon_ligne[0][1]


# doublon sur une colonne.
solution_doublon_colonne = [ligne[:] for ligne in solution_valide]
solution_doublon_colonne[0][0] = solution_doublon_colonne[1][0]


# doublon dans un bloc 3x3.
solution_doublon_bloc = [ligne[:] for ligne in solution_valide]
solution_doublon_bloc[0][0] = solution_doublon_bloc[1][1]


# valeur hors de l'intervalle autorisé (1 à 9).
solution_valeur_hors_limites = [ligne[:] for ligne in solution_valide]
solution_valeur_hors_limites[0][0] = 10


# solution incomplète (une case reste vide).
solution_incomplete = [ligne[:] for ligne in solution_valide]
solution_incomplete[0][0] = 0


# grille Sudoku complète et valide, mais incompatible avec
# les indices publics. On permute globalement 1 et 2 : les règles Sudoku
# restent respectées, mais certains indices de la grille initiale changent.
solution_incompatible_avec_grille = [
    [2 if valeur == 1 else 1 if valeur == 2 else valeur for valeur in ligne]
    for ligne in solution_valide
]


# dimensions incorrectes (seulement 8 lignes).
solution_dimensions_invalides = [ligne[:] for ligne in solution_valide[:-1]]


# type incorrect (une chaîne à la place d'un entier).
solution_type_invalide = [ligne[:] for ligne in solution_valide]
solution_type_invalide[0][0] = "3"
