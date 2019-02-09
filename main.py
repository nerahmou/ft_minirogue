# coding: utf8
# lang: python3


import time
import curses
from welcome import *
from partie import *

NLINE = 30
NCOLS = 100

def init_curses(window):
    curses.noecho()
    curses.cbreak()
    window.keypad(True)
    curses.curs_set(False)
    return (window)

def stop_curses(window):
    window.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

def loop(window):
    partie = Partie(window)
    partie.start()
    while 101:
        key = window.getch()
        
        if (key == ord('q') or key == ord('Q')):
            break

def main(window):
    init_curses(window)
    if curses.LINES < NLINE or curses.COLS < NCOLS:
        stop_curses(window)
        print("To small")
        return 
    start_line = int((curses.LINES / 2)) - int((NLINE / 2))
    start_cols = int((curses.COLS / 2)) - int((NCOLS / 2))
    print(str(start_line) + " " + str(start_cols))
    subwin = window.subwin(NLINE, NCOLS, start_line, start_cols)
    subwin.box()
    welcome(subwin)
    loop(subwin)
    stop_curses(window)

if __name__ == "__main__":
    curses.wrapper(main)
