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


class Board:
    """
      This is a class that handles the drawing in console
      """

    def __init__(self, width, height, padding=[15, 3], screen=None):
        self.__width = width
        self.__height = height
        self.matrix = [[' ' for _ in range(height)] for _ in range(width)]
        self.__paddings = [max(15, padding[0]), max(3, padding[1])]
        self.__stdscr = screen if screen else curses.initscr()
        self.__delete = False if screen else True
        self.__stdscr.keypad(True)
        self.__stdscr.nodelay(True)
        self.__stdscr.refresh()

    def stdscr(self):
        return self.__stdscr, [self.__width, self.__height], self.__paddings

    def setup(self):
        for y in range(self.__height):
            self.__stdscr.move(self.__paddings[1] + y, self.__paddings[0])
            for x in range(self.__width):
                self.__stdscr.addstr(" ",  curses.color_pair(1))
        self.print_score(0)
        self.print_level(1)
        self.print_snake_size(0)
        self.__stdscr.refresh()

    def print_score(self, score):
        self.__stdscr.move(self.__paddings[1] + 1, 1)
        self.__stdscr.addstr("SCORE")
        self.__stdscr.move(
            self.__paddings[1] + 3, max(1, 4-len(str(score))//2))
        self.__stdscr.addstr(str(score))

    def print_level(self, level):
        self.__stdscr.move(self.__paddings[1] + 1,
                           self.__paddings[0] + self.__width + 8)
        self.__stdscr.addstr("LEVEL")
        self.__stdscr.move(self.__paddings[1] + 3,
                           self.__paddings[0] + self.__width + 10)
        self.__stdscr.addstr(str(level))

    def getCommand(self, tries=3):
        cmd = Command()
        cmd.cmd = CommandType.NONE

        for _ in range(tries):
            ch = self.__stdscr.getch()
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

    def refresh(self):
        self.__stdscr.refresh()

    def print_snake_size(self, count):
        self.__stdscr.move(self.__paddings[1] + 5,
                           self.__paddings[0] + self.__width + 8)
        self.__stdscr.addstr("LENGTH")
        self.__stdscr.move(self.__paddings[1] + 7,
                           self.__paddings[0] + self.__width + max(1, 11-len(str(count))//2))
        self.__stdscr.addstr(str(count))

    # def pause(self, on=True):
    #   if on:
    #     text = "PAUSED"
    #   else:
    #     text = "      "
    #   self.__stdscr.move(self.__paddings[1] + 10,
    #                      self.__paddings[0] + 3 * self.__width + 8)
    #   self.__stdscr.addstr(text)
    #   self.__stdscr.refresh()

    def __del__(self):
        self.__stdscr.clear()
        self.__stdscr.refresh()
        if self.__delete:
            curses.endwin()

    def __setitem__(self, coords, value):
        if coords[0] >= self.__width or coords[1] >= self.__height:
            return False
        self.__stdscr.addch(
            self.__paddings[1] + coords[1], self.__paddings[0] + coords[0], value,  curses.color_pair(1))
        self.matrix[coords[0]][coords[1]] = value
        return True
