import curses
import Partie
import time

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(1)
    stdscr.keypad(True)


    partie = Partie()
    partie.refresh()

    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)