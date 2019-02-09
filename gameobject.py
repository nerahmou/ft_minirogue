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

    def __init__(self):
        self.name = str()
        self.pos = [0, 0]
        self.char = '.'
