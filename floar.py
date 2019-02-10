from map_class import *
import time
import os

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

    _newRoom(dico)
        add room int room line

    PrintStage(windo)
        print all room and road in this floor
    """
    floor_id = 0
    def __init__(self, dico):
        self.floor_id += 1
        self.rooms = []
        self.roads = []
        self.monstres = []
        self._new_room(dico)

    def _new_stage(self, dico):
        self.rooms.append(Room(dico))
        if "road" in dico:
            for road in dico["road"]:
                self.roads.append(Road(road))

    def print_stage(self, window):
        i = 0
        for room in self.rooms:
            room.draw_room(window)
            i += 1
        print(self.rooms)
        #for chemin in self.road:
        #    chemin.print_chemin(window)
