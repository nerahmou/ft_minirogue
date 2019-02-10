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

    def _new_stage(self, etage_file, chemins_file):
        with open(etage_file) as file:
            for line in file:
                self.salles.append(Salle(line.split(',')))
        with open(chemins_file) as file:
            for line in file:
                self.chemins.append(Chemin(line.split('/')))

    def print_stage(self, window):
        for salle in self.salles:
            salle.draw_room(window)
        for chemin in self.chemins:
            chemin.print_chemin(window)
