import curses
from porte import *
from utile import *

class Salle:
    def __init__(self, data):
        """
        Attributes
        ----------

        ncols : int
            nb of colune (x)

        nlines : int
            nb of line (y)

        pos_x : int
            x pos of the top left wall

        pos_y : 
            y pos of the top left wall
        """
        self.ncols = int(data[0])
        self.nlines = int(data[1])
        self.pos_x = int(data[2])
        self.pos_y = int(data[3])
        self.portes = self._add_portes(data[4].split(':'))
        self.objets = []
        self.escalier = []
        self.visible = False

    def _add_portes(self, portes):
        liste_portes = []
        for porte in portes:
            x, y = porte.split('/')
            liste_portes.append(Porte(int(x), int(y)))
        return liste_portes

    def draw_room(self, window):
        draw_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        feed_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        for porte in self.portes:
            porte.print_porte(window)
