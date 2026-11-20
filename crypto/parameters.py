class PedersenParameters:

    def __init__(self, p, q, g, h):
        self.p = p
        self.q = q
        self.g = g
        self.h = h
        
    def display_public_parameters(self):
        """
        Affiche les paramètres publics p, q, g et h.
        """
        
        print(self.p,"Un grand nombre premier")
        print(self.q, "L'ordre du groupe utilisé")
        print(self.g, "Premier générateur")
        print(self.h, "Deuxième générateur")
        
        
    def generate_parameters(self):
    """
    Génère ou récupère un ensemble de paramètres cryptographiques adaptés.
    Il faut :
    - p et q premiers ;
    - q divise p-1 ;
    - g et h appartiennent au sous-groupe d'ordre q modulo p ;
    - g et h sont non triviaux ;
    la relation permettant de calculer le logarithme discret de \(h\) en base \(g\) doit être inconnue.
    """
