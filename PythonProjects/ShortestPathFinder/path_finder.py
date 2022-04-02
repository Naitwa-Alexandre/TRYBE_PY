import curses
from curses import wrapper
import queue
import time
from maze import maze

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j * 2, value, BLUE)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    # curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # blue_and_black = curses.color_pair(3)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)