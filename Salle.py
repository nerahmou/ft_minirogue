from porte import Porte

class Salle:
    def __init__(self, data):
        """
        :param long: longueur
        :param larg: largeur
        :param x: position x
        :param y: position y
        """
        self.longeur = int(data[0])
        self.largeur = int(data[1])
        self.pos_x = int(data[2])
        self.pos_y = int(data[3])
        self.portes = self._add_portes(data[4].split(':'))
        self.objets = []
        self.escalier = []
        self.visible = True

    def _add_portes(self, portes):
        liste_portes = []
        for porte in portes:
            x, y = porte.split('/')
            liste_portes.append(Porte(int(x), int(y)))
        return liste_portes

    def dessine_long(self, window):
        x = self.pos_x
        y = self.pos_y
        while y < self.pos_y + self.longeur:
            window.addstr(x, y, 'X')
            window.addstr(x + self.largeur, y, 'X')
            y += 1

    def dessine_larg(self, window):
        x = self.pos_x + 1
        y = self.pos_y
        while x < self.pos_x + self.largeur:
            window.addstr(x, y, 'X')
            window.addstr(x, y + self.longeur - 1, 'X')
            x += 1

    def remplir_salle(self, window):
        for point_x in range(self.pos_x + 1, self.pos_x + self.largeur):
            for point_y in range(self.pos_y + 1, self.pos_y + self.longeur - 1):
                window.addstr(point_x, point_y, '.')

    def print_salle(self, window):
        self.dessine_long(window)
        self.dessine_larg(window)
        self.remplir_salle(window)
        for porte in self.portes:
            porte.print_porte(window)