from partie import Partie
import curses
import time

def init_window(window):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(1)
    window.keypad(True)

def close_window(window):
    window.keypad(False)
    curses.echo()
    curses.endwin()



def main(window):
    partie = Partie(window)
    partie.start()
    while True:
        pass

if __name__ == '__main__':
    curses.wrapper(main)