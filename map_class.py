import curses
from door import *
from utile import *

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
        self.room_id += 1
        self.ncols = dico["cols"]
        self.nlines = dico["lines"]
        self.pos = { 'x' : dico["x"], 'y' : dico['y'] }
        self.objets = []
        self.escalier = []
        self.hidden = False
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


class Door:
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
        self.door_id += 1
        self.door = {'room' : room, 'road' : road}
        self.pos = pos

    def print_porte(self, window):
        window.addstr(self.pos['y'], self.pos['x'], 'o')


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
        self.road_id += 1
        self.doors = door

#    def print_chemin(self, window):
#        while self.long:
#            window.addstr(self.x, self.y + self.long, '=')
#            self.long -= 1
