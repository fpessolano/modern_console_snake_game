import curses
from enum import Enum

class CommandType(Enum):
    NONE = 0
    END = 1
    MOVE = 2

class Command:
    def __init__(self):
        self.cmd = CommandType.NONE
        self.data = []

class Screen:
    def __init__(self, rows, columns):
        self.matrix = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.playHeight = rows
        self.playWidth = columns

        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.keypad(True)
        self.stdscr.nodelay(True)
        self.screenHeight, self.screenWidth = self.stdscr.getmaxyx()

    def write(self, row, column, value):
        self.stdscr.addch(row, column, value)
        self.matrix[row][column] = value

    def read(self, row, column):
        return self.matrix[row][column]

    def getCommand(self, tries=3):
        cmd = Command()
        cmd.cmd = CommandType.NONE

        for _ in range(tries):
            ch = self.stdscr.getch()
            if ch == curses.KEY_UP:
                cmd.cmd = CommandType.MOVE
                cmd.data = [0, -1]
                break
            elif ch == curses.KEY_DOWN:
                cmd.cmd = CommandType.MOVE
                cmd.data = [0, 1]
                break
            elif ch == curses.KEY_LEFT:
                cmd.cmd = CommandType.MOVE
                cmd.data = [-1, 0]
                break
            elif ch == curses.KEY_RIGHT:
                cmd.cmd = CommandType.MOVE
                cmd.data = [1, 0]
                break
            elif ch == 27:  # Escape key
                cmd.cmd = CommandType.END
                break

        return cmd

    def __del__(self):
        curses.endwin()

