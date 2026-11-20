import secrets

class Cell:
    """
    Représente une case du Sudoku dans le protocole ZKP.

    Chaque case possède :
    - un indice unique entre 0 et 80 ;
    - une valeur secrète entre 1 et 9 ;
    - une valeur aléatoire utilisée pour créer son engagement de Pedersen ;
    - un engagement cryptographique destiné à être communiqué au vérificateur.
    """
    
    def __init__(self, index, value):
        if index < 0 or index > 80 or value < 1 or value > 9:
            raise ValueError("valeur ou indice invalide")
        if not isinstance(index, int) or not isinstance(value, int):
            raise TypeError("index et value doivent être des entiers")
        
        self.index = index
        self.value = value
        self.randomness = None
        self.commitment = None
    
    def generate_randomness(self, q):
        """
        Génère un aléa cryptographique pour cette case.

        L'aléa est tiré uniformément dans l'ensemble {0, ..., q-1}.
        Il sera utilisé comme exposant dans l'engagement de Pedersen :
            C = g^value * h^randomness mod p
        """
        
        if q <= 0:
            return False
        self.randomness = secrets.randbelow(q)
        return self.randomness
