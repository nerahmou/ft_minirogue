import curses
from porte import *
from utile import *

class Salle:
    def __init__(self, dico):
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
        self.ncols = dico["cols"]
        self.nlines = dico["lines"]
        self.pos_x = dico["x"]
        self.pos_y = dico["y"]
        self.portes = self._add_portes(dico["portes"])
        self.objets = []
        self.escalier = []
        self.visible = False

    def _add_portes(self, portes):
        liste_portes = []
        for porte in portes:
            liste_portes.append(Porte(porte["x"], porte["y"]))
        return liste_portes

    def draw_room(self, window):
        draw_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        feed_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        #for porte in self.portes:
         #   porte.print_porte(window)
