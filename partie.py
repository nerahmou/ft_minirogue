from etage import *
from many_class import *
import os

class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.stage = []
        self.player = Playeur()

    def start(self):
        directory = os.path.dirname(__file__)
        liste_fichiers_etages = os.path.join(directory, "etages")
        liste_fichiers_chemins = os.path.join(directory, "chemins")
        self.stage.append(Etage(liste_fichiers_etages, liste_fichiers_chemins))
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
