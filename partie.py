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
        self.monsters = []
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
        self.current_floor.draw_floor(self.window)
        self.window.refresh()
        self._run()

    def _init_spaw(self):
        self.monster = Monster("bat", 1, 2, 1, 0, 'b')
        first_room = self.floors[0].rooms[0]
        pos = {}
        pos['x'] = first_room.pos['x'] + first_room.ncols // 2
        pos['y'] = first_room.pos['y'] + first_room.nlines // 2
        first_room.nether_see = False
        first_room.hidden = False
        self.playeur.spwan_pos(pos)
        segond_room = self.floors[0].rooms[0]
        pos2 = {}
        pos2['x'] = (segond_room.pos['x'] + segond_room.ncols // 2) + 2
        pos2['y'] = (segond_room.pos['y'] + segond_room.nlines // 2)
        self.monster.spwan_pos(pos2)

    def _feed_floors(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, "text2.json")
        with open(path) as file:
            json_data = json.load(file)
            for floor in json_data:
                self.floors.append(Floor(json_data[floor]))

    def _is_door(self, pos_x, pos_y, door_pos):
        if door_pos['x'] == pos_x and door_pos['y'] == pos_y:
            return 1
        return 0

    def _collision(self, room_limit, pos, nbr):
        if room_limit == pos + nbr:
            return 1
        return 0


    def _which_room(self, current_room):
        rooms = self.floors[0].rooms
        id_current_room = current_room.doors[0].id
        i = 0
        self.current_room.hidden_room(self.window)
        while i < len(rooms):
            if rooms[i].doors[0].id == id_current_room and rooms[i] != current_room:
                self.current_room = rooms[i]
                self.current_room.show_room(self.window)
                break
            i += 1

    def _move_left(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['x'], pos['x'], -1):
            if self._is_door(pos['x'] - 1, pos['y'], room.doors[0].pos):
                self._which_room(room)
                pass
            else:
                return
        self.window.addstr(pos['y'], pos['x'] - 1, character.char + char)
        character.pos['x'] = pos['x'] - 1

    def _move_right(self, character, char):
        room = self.current_room
        pos = character.pos
        if self._collision(room.pos['x'] + room.ncols, pos['x'], 1):
            if self._is_door(pos['x'] + 1, pos['y'], room.doors[0].pos):
                self._which_room(room)
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
            if self._is_door(pos['x'], pos['y'] - 1, room.doors[0].pos):
                self._which_room(room)
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
            if self._is_door(pos['x'], pos['y'] + 1, room.doors[0].pos):
                self._which_room(room)
                character.pos['y'] += 1
                pass
            else:
                return
        self.window.addch(pos['y'], pos['x'], char)
        self.window.addch(pos['y'] + 1, pos['x'], character.char)
        character.pos['y'] = pos['y'] + 1

    def _run(self):
        char = '.'
        while 101:
            self.playeur.print_obj(self.window)
            self.monster.print_obj(self.window)
            key = self.window.getch()
            if (key == ord('q') or key == ord('Q')):
                self.playeur.died(self.window)
                break
            elif (key == ord('a')):
                self._move_left(self.playeur, char)
            elif (key == ord('d')):
                self._move_right(self.playeur, char)
            elif (key == ord('w')):
                self._move_up(self.playeur, char)
            elif (key == ord('s')):
                self._move_down(self.playeur, char)
            self.playeur.draw_stat(self.window)
            self.window.refresh()


