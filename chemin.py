
class Chemin:
    def __init__(self, chemin):
        self.x = chemin["x"]
        self.y = chemin["y"]
        self.direction = chemin["direction"]
        self.long = chemin["longueur"]


    def print_chemin(self, window):
        while self.long:
            window.addstr(self.x, self.y + self.long, '=')
            self.long -= 1