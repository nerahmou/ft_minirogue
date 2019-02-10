# coding: utf8
# lang: python3

from random import randint
from utile import *
import time

HP_RANK = 2
STR_RANK = 1

GOLD_RANK = 1

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
        self.pos = {'x' : 0, 'y' : 0}
        self.char = '.'

    def print_obj(self, window):
        window.addch(self.pos['y'], self.pos['x'], self.char)


class Character(GameObject):
    """
    Attributes
    ----------

    lv : int
        level of Playeur

    hp : int
        hit point, life point, point de vie

    str : int
        strength, force

    xp : int
        experience points
 
    gold : int
        gold, money

    armor : int
        armor, armure
    """

    def __init__(self):
        GameObject.__init__(self)
        self.lv = 1
        self.hp = 1
        self.str = 1
        self.xp = 1
        self.gold = 0
        self.armor = 0

    def _lv_up(self):
        self.xp = self.xp - (self.lv * 10)
        self.lv = self.lv + 1
        self.hp_max = self.hp_max + HP_RANK
        self.hp = self.hp_max
        self.str = self.str + STR_RANK

    def do_domage(self, enemy):
        damage = self.str
        cc = randint(0, 6)
        if cc == 6:
            damage = damage + (damage * 0.5)
        elif cc == 0:
            damage = 0
        return (damage)

    def check_xp(self):
        while (self.xp / 10) >= self.lv:
            self._lv_up(self)

    def spwan_pos(self, pos):
        self.pos = pos

class Monster(Character):

    def __init__(self, name, lv, hp, gold, armor, char):
        Character.__init__(self)
        self.name = name
        self.lv = lv
        self.hp = hp
        self.gold = gold
        self.char = char
        self._virt_up()

    def _virt_up(self):
        self.hp = self.hp + (HP_RANK * self.lv)
        self.str = self.str + (STR_RANK * self.lv)
        self.gold = self.gold + (GOLD_RANK * self.lv)


class Playeur(Character):
    """
    Attributes
    ----------

    inv : Item {}
        list of item
    """

    def __init__(self):
        Character.__init__(self)
        self.name = "Playeur 1"
        self.char = '@'
        self.hp_max = 10
        self.hp = 10
        self.xp = 1
        self.str = 1
        self.gold = 0
        self.armor = 5
        self.inv = {}

    #def do_domage(self)
    def heal(self, nb):
        if (self.hp + nb) <= self.hp_max:
            self.hp = self.hp + nb
        else:
            self.hp = self.hp_max

    def died(self, window):
        msg = "YOU DIED"
        tmp_y = int(50 - int(len(msg) / 2))
        tmp_x = int((30 / 3) - 1)
        window.clear()
        window.addstr(tmp_x, tmp_y, msg)
        window.refresh()
        time.sleep(3)

    def draw_stat(self, window):
        string = "Level: " + str(self.lv) + "\t\tHp: " + str(self.hp) + "\t\tGold: " + str(self.gold) + "\t\tArmor: " + str(self.armor) + "\t\tExp:" + str(self.xp)
        window.addstr(28, 5, string)

