from salle import *
from chemin import *
import time
import os

class Etage:
    def __init__(self, path_etages, path_chemins):
        self.salles = []
        self.monstres = []
        self.chemins = []
        self._new_stage(path_etages, path_chemins)

    def _new_stage(self, path_etages, path_chemins):
            etages = [os.path.join(path_etages, filename) for filename in os.listdir(path_etages)]
            chemins = [os.path.join(path_chemins, filename) for filename in os.listdir(path_chemins)]
            etages.sort()
            chemins.sort()
            i = 0
            while i < len(etages):
                with open(etages[i]) as file:
                    for line in file:
                        self.salles.append(Salle(line.split(',')))
                with open(chemins[i]) as file:
                    for line in file:
                        self.chemins.append(Chemin(line.split('/')))
                    i += 1

    def print_stage(self, window):
        for salle in self.salles:
            salle.draw_room(window)
        for chemin in self.chemins:
            chemin.print_chemin(window)
