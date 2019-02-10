#coding: utf8
# lang: python3

import curses

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
    door_id = 0
    def __init__(self, pos, room, road):
        Mapobj.__init__(self)
        self.door_id += 1
        self.door = {'room' : room, 'road' : road}
        self.pos = pos

    def print_porte(self, window):
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
    def __init__(self, dico):
        Mapobj.__init__(self)
        self.room_id += 1
        self.ncols = dico["cols"]
        self.nlines = dico["lines"]
        self.pos = { 'x' : dico["x"], 'y' : dico['y'] }
        self.objets = []
        self.escalier = []
        self.doors = self._feed_doors(dico["doors"])

    def _feed_doors(self, doors):
        liste_doors = []
        for door in doors:
            liste_doors.append(Door(door))
        return liste_doors

    def draw_room(self, window):
        draw_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        feed_box(window, self.pos_y, self.pos_x, self.nlines, self.ncols)
        #for door in self.doors:
         #   door.print_door(window)


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
    def __init__(self, doors):
        Mapobj.__init__(self)
        self.road_id += 1
        self.doors = door

#    def print_chemin(self, window):
#        while self.long:
#            window.addstr(self.x, self.y + self.long, '=')
#            self.long -= 1


class Floar:
    """
    Etage

    Attributes
    ---------

    room : [Room]
        list of all room in this floar

    road : [Road]
        list of all road in this floar

    Methods
    -------

    _feed_room(dico)
        add all room in rooms

    _feed_road(dico)
        add all road in road

    PrintStage(windo)
        print all room and road in this floar
    """
    floar_id = 0
    def __init__(self, dico):
        Mapobj.__init__(self)
        self.floar_id += 1
        self.rooms = []
        self.roads = []
        self.monstres = []
        self._feed_rooms(dico)
        self._feed_roads(dico)

    def _feed_rooms(self, dico):
        for room in dico['room']:
            self.rooms.append(Room(room))

    def _feed_roads(self, dico):
        for road in dico['road']:
            self.roads.append(Road(road))

    def print_stage(self, window):
        i = 0
        for room in self.rooms:
            room.draw_room(window)
            i += 1
        print(self.rooms)
        #for chemin in self.road:
        #    chemin.print_chemin(window)
