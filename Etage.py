import Salle

class Etage:
    def __init__(self):
        self.salles = [Salle(40, 20, 5, 5),
                       Salle(20, 10, 20, 20),
                       Salle(10, 5, 30, 30)]

        self.monstres = []
        self.couloirs = []
