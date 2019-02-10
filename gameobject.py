# coding: utf8
# lang: python3

class Items:
    """
    Attributes
    ----------

    name : str
        name

    pos : [ int , int]
        pos x y on the map

    char : char
        char represent
    """
    def __init__(self, pos_x, pos_y, char, points):
        self.pos = { 'x' :pos_x, 'y' : pos_y}
        self.char = char
        self.points = points

    def _draw_object(self, window):
        window.addch(self.pos['y'], self.pos['x'], self.char)

    def use_obj(self, player):
        pass

class Poison(Items):
    def __init__(self, room):
        x = room.pos['x']
        y = room.pos['y']
        Items.__init__(self, x + 5, y + 1, 'P', 10)

    def use_obj(self, player):
        player.hp -= self.points

class Bread(Items):
    def __init__(self, room):
        x = room.pos['x']
        y = room.pos['y']
        Items.__init__(self, x + 2, y + 1, 'B', 20)

    def use_obj(self, player):
        player.hp += self.points
