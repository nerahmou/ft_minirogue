# coding: utf8
# lang: python 3

import curses
import os
import time
import json

from map_class import *
from character_class import *

class Partie:
    """
    Attributes
    ----------

    window : curses window
        window return by curses

    current_floor : floor
        curent floor were ise the playeur

    floors : [floor]
        list of all floor

    road : [Road]
        list of all road

    Methods
    -------

    start()
        init all thing befor run the game

    _run()
        run the game is a loop

    """
    def __init__(self, window):
        self.window = window
        self.current_floor = None
        self.floors = []
        self.road = []
        self.playeur = Playeur()

    def start(self):
        """
        Initialise les etages et rafraichit a la fin
        :return:
        """
        self._feed_floors()
        self.playeur.spwan_pos({'x' : 50, 'y' : 15})
        self.current_floor = self.floors[0]
        self.current_floor.print_floor(self.window)
        self.window.refresh()
        self._run()

    def _feed_floors(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, "text2.json")
        with open(path) as file:
            json_data = json.load(file)
            for floor in json_data:
                self.floors.append(Floor(json_data[floor]))
            #for elem in json_data["floor"]["road"]:
            #    print(elem)
            #   time.sleep(2)

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

    def _run(self):
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


