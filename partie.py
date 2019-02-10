from etage import *
from many_class import *
import os

class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.nbr_stage = 0
        self.stage = []
        self.player = Playeur()

    def create_stages(self):
        directory = os.path.dirname(__file__)
        etages = os.path.join(directory, "etages")
        chemins = os.path.join(directory, "chemins")
        etages = [os.path.join(etages, filename) for filename in os.listdir(etages)]
        chemins = [os.path.join(chemins, filename) for filename in os.listdir(chemins)]
        etages.sort()
        chemins.sort()
        i = 0
        while i < len(etages):
            self.stage.append(Etage(etages[i], chemins[i]))
            self.nbr_stage += 1
            i += 1

    def start(self):
        """
        Initialise les etages et rafraichit a la fin
        :return:
        """
        self.create_stages()
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
