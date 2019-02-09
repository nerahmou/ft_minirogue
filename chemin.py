
class Chemin:
    def __init__(self, data):
        self.x = int(data[0])
        self.y = int(data[1])
        self.long = int(data[2])

    def print_chemin(self, window):
        while self.long:
            window.addstr(self.x, self.y + self.long, '=')
            self.long -= 1