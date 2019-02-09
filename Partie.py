from etage import *
import time

class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.stage = []
        #self.joueur

    def start(self):
        self.stage.append(Etage('etages/etage1'))
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
