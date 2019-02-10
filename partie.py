from etage import *
from many_class import *
import curses
import os

class Partie:
    def __init__(self, window):
        self.window = window
        self.current_stage = 0
        self.stage = []
        self.playeur = Playeur()

    def start(self):
        directory = os.path.dirname(__file__)
        liste_fichiers_etages = os.path.join(directory, "etages")
        liste_fichiers_chemins = os.path.join(directory, "chemins")
        self.stage.append(Etage(liste_fichiers_etages, liste_fichiers_chemins))
        self.stage[self.current_stage].print_stage(self.window)
        self.window.refresh()
        self.playeur.spwan_pos({'x' : 50, 'y' : 15})

    def _move_left(self, character, char):
        pos = character.pos
        self.window.addstr(pos['y'], pos['x'] - 1, character.char + char)
        character.pos['x'] = pos['x'] - 1

    def _move_right(self, character, char):
        pos = character.pos
        self.window.addstr(pos['y'], pos['x'], char + character.char)
        character.pos['x'] = pos['x'] + 1

    def _move_up(self, character, char):
        pos = character.pos
        self.window.addch(pos['y'], pos['x'], char)
        self.window.addch(pos['y'] - 1, pos['x'], character.char)
        character.pos['y'] = pos['y'] - 1

    def _move_down(self, character, char):
        pos = character.pos
        self.window.addch(pos['y'], pos['x'], char)
        self.window.addch(pos['y'] + 1, pos['x'], character.char)
        character.pos['y'] = pos['y'] + 1

    def run(self):
        char = ' '
        while 101:
            self.playeur.print_obj(self.window)
            key = self.window.getch()
            if (key == ord('q') or key == ord('Q')):
                break
            if (key == ord('a')):
                self._move_left(self.playeur, char)
            if (key == ord('d')):
                self._move_right(self.playeur, char)
            if (key == ord('w')):
                self._move_up(self.playeur, char)
            if (key == ord('s')):
                self._move_down(self.playeur, char)
            self.window.refresh()
