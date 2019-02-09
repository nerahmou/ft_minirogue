import Porte

class Salle:
    def __init__(self, long, larg, x, y):
        self.longeur = long
        self.largeur = larg
        self.pos_x = x
        self.pos_y = y
        self.portes = [Porte(x + long / 2)]
        self.objets = []
        self.escalier = []

