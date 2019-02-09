
class Porte:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def print_porte(self, window):
        window.addstr(self.pos_x, self.pos_y, 'o')
