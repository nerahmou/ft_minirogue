from etage import Etage
#from joueur import Joueur
import time
import os


class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.stage = []

    def start(self):
        directory = os.path.dirname(__file__)
        list_dir = os.path.join(directory, "etages")
        print(list_dir)
        time.sleep(2)
        self.stage.append(Etage(list_dir + "/etage1"))
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
