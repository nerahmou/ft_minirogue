from salle import *
from chemin import *


class Etage:
    def __init__(self, path):
        self.salles = []
        self.monstres = []
        self.chemins = []
        self._new_stage(path)

    def _new_stage(self, path):
            with open(path) as file:
                for line in file:
                    self.salles.append(Salle(line.split(',')))
            with open(path + "_chemins") as file:
                for line in file:
                    self.chemins.append(Chemin(line.split('/')))

    def print_stage(self, window):
        for salle in self.salles:
            salle.print_salle(window)
        for chemin in self.chemins:
            chemin.print_chemin(window)
