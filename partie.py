from etage import *
from many_class import *
import os
import json

class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.nbr_stage = 0
        self.stage = []
        self.player = Playeur()

    def create_stages(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, "text.json")
        with open(path) as file:
            data = json.load(file)
            for etage in data:
                self.stage.append(Etage(etage))

    def start(self):
        """
        Initialise les etages et rafraichit a la fin
        :return:
        """
        self.create_stages()
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
