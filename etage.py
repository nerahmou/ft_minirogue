from salle import *
from chemin import *
import time
import os

class Etage:
    def __init__(self, dico):
        self.salles = []
        self.monstres = []
        self.chemins = []
        self._new_stage(dico)

    def _new_stage(self, dico):
        self.salles.append(Salle(dico))
        if "chemins" in dico:
            for chemin in dico["chemins"]:
                self.chemins.append(Chemin(chemin))

    def print_stage(self, window):
        i = 0
        for salle in self.salles:
            salle.draw_room(window)
            i += 1
        print(self.salles)
        #for chemin in self.chemins:
        #    chemin.print_chemin(window)
