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
        self.current_room = None
        self.floors = []
        self.road = []
        self.playeur = Playeur()

    def start(self):
        """
        Initialise les etages et rafraichit a la fin
        :return:
        """
        self._feed_floors()
        self.current_floor = self.floors[0]
        self.current_room = self.floors[0].rooms[0]
        self._init_spaw()
        self.current_floor.print_floor(self.window)
        self.window.refresh()
        self._run()

    def _init_spaw(self):
        first_room = self.floors[0].rooms[0]
        ncols = first_room.ncols
        nlines = first_room.nlines
        pos = first_room.pos
        self.playeur.spwan_pos(ncols, nlines, pos)


    def _feed_floors(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, "text2.json")
        with open(path) as file:
            json_data = json.load(file)
            for floor in json_data:
                self.floors.append(Floor(json_data[floor]))

    def _which_room(self, current_door, rooms):
        for room in rooms:
            for door in room.doors:
                if current_door.id == door.id and current_door != door:
                    self.current_room = room
                    return

    def _is_door(self, pos_x, pos_y, room):
        doors = room.doors
        for door in doors:
            if door.pos['x'] == pos_x and door.pos['y'] == pos_y:
                self._which_room(door, self.floors[0].rooms)
                return 1
        return 0

    def _collision(self, room_limit, pos, nbr):
        if room_limit == pos + nbr:
            return 1
        return 0

    def _move_left(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['x'], pos['x'], -1):
            if self._is_door(pos['x'] - 1, pos['y'], room):
                pass
            else:
                return
        self.window.addstr(pos['y'], pos['x'] - 1, character.char + char)
        character.pos['x'] = pos['x'] - 1

    def _move_right(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['x'] + room.ncols, pos['x'], 1):
            if self._is_door(pos['x'] + 1, pos['y'], room):
                pass
            else:
                return
        pos = character.pos
        self.window.addstr(pos['y'], pos['x'], char + character.char)
        character.pos['x'] = pos['x'] + 1

    def _move_up(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['y'], pos['y'], -1):
            if self._is_door(pos['x'], pos['y'] - 1, room):
                pass
            else:
                return
        self.window.addch(pos['y'], pos['x'], char)
        self.window.addch(pos['y'] - 1, pos['x'], character.char)
        character.pos['y'] = pos['y'] - 1

    def _move_down(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['y'] + room.nlines, pos['y'], 1):
            if self._is_door(pos['x'], pos['y'] + 1, room):
                pass
            else:
                return
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
            elif (key == ord('a')):
                self._move_left(self.playeur, char)
            elif (key == ord('d')):
                self._move_right(self.playeur, char)
            elif (key == ord('w')):
                self._move_up(self.playeur, char)
            elif (key == ord('s')):
                self._move_down(self.playeur, char)
            self.window.refresh()


