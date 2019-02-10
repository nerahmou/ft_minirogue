#coding: utf8
# lang: python3

import time
import curses
from utile import *

class Mapobj:
    """
    """

    def __init__(self):
        self.nether_see = True
        self.hidden = True


class Door(Mapobj):
    """
    porte

    Attributes
    ----------

    pos : { 'x' : int, 'y' : int}
        pos of the door

    rooms : {'room' : Room, 'road' : Road}
         room and road on comunication
    """
    def __init__(self, x, y, door_id, room):
        Mapobj.__init__(self)
        self.door_id = 1
        self.door = {'room' : room, 'road' : None}
        self.pos = { 'x' : x, 'y' : y}

    def draw_door(self, window):
        window.addstr(self.pos['y'], self.pos['x'], 'o')

class Room:
    """
    Attributes
    ----------

    ncols : int
        nb of colune (x)

    nlines : int
        nb of line (y)

    pos : { 'x' : int, 'y' : int }
        y pos of the top left wal

    hidden : bol
        show or not the rooml

    doors : [Door]
        list of all door
    """
    room_id = 0

    def __init__(self, room):
        Mapobj.__init__(self)
        self.room_id += 1
        self.ncols = room["ncols"]
        self.nlines = room["nlines"]
        self.pos = room["pos"]
        self.objets = []
        self.escalier = []
        self.doors = []
        self._feed_doors(room['doors'])

    def _feed_doors(self, doors):
        for door in doors:
            self.doors.append(Door(door["pos"]['x'], door["pos"]['y'], door["door_id"], self))

    def draw_room(self, window):
        draw_box(window, self.pos['y'], self.pos['x'], self.nlines, self.ncols)
        feed_box(window, self.pos['y'], self.pos['x'], self.nlines, self.ncols)
        for door in self.doors:
            door.draw_door(window)


class Road:
    """
    chemin

    Attributes
    ----------

    door : [Door]
        list of all door

    Methods
    -------

    draw_road(window)
        draw the road

    """
    road_id = 0
    def __init__(self, door_ids):
        Mapobj.__init__(self)
        self.road_id += 1
        self.doors = None
        self.door_ids = door_ids["door_id1"], door_ids["door_id2"]

#    def print_chemin(self, window):
#        while self.long:
#            window.addstr(self.x, self.y + self.long, '=')
#            self.long -= 1


class Floor:
    """
    Etage

    Attributes
    ---------

    room : [Room]
        list of all room in this floor

    road : [Road]
        list of all road in this floor

    Methods
    -------

    _feed_room(dico)
        add all room in rooms

    _feed_road(dico)
        add all road in road

    PrintStage(windo)
        print all room and road in this floor
    """
    floor_id = 0
    def __init__(self, floor):
        Mapobj.__init__(self)
        self.floor_id += 1
        self.rooms = []
        self.roads = []
        self.monstres = []
        self._feed_roads(floor['road'])
        self._feed_rooms(floor['room'])

    def _feed_rooms(self, rooms):
        for room in rooms:
            self.rooms.append(Room(room))

    def _feed_roads(self, roads):
        for road in roads:
            self.roads.append(Road(road))

    def print_floor(self, window):
        i = 0
        for room in self.rooms:
            room.draw_room(window)
            i += 1
        #for chemin in self.road:
        #    chemin.print_chemin(window)
