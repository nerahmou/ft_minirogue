# coding: utf8
# lang: python3

class GameObject:
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
        self.pos = pos_x, pos_y
        self.char = char
        self.points = points

    def _draw_object(self, window):
        window.addch(self.pos[1], self.pos[0], self.char)


class Items(GameObject):
    def __init__(self, pos_x, pos_y, char, points):
        GameObject.__init__(self, pos_x, pos_y, char, points)


class Poison(Items):
    def __init__(self, room):
        x = room.pos['x']
        y = room.pos['y']
        Items.__init__(self, x + 5, y + 1, 'P', 10)

    def _beat_player(self, player):
        player.hp -= self.points

class Bread(Items):
    def __init__(self, room):
        x = room.pos['x']
        y = room.pos['y']
        Items.__init__(self, x + 2, y + 1, 'B', 20)

    def _feed_player(self, player):
        player.hp += self.points
