import curses
import random
import time
import string
import repeat_event as rpe


class Static:
  """
    This is a class that can be used to build static pages such as
    welcomme and controls pages.
    """
  
  def __init__(self,
               width=60,
               height=20,
               screen=None,
               change_speed=0.01,
               reveal_time=0.05,
               padding=[15, 3],):
    width += max(15, padding[0])
    height += max(3, padding[1])
    self.__stdscr = screen if screen else curses.initscr()
    self.__delete = False if screen else True
    max_y, max_x = self.__stdscr.getmaxyx()
    self.__width, self.__height = min(width, max_x), min(height, max_y)
    self.__text, self.__animated_text, self.__overlapping_text = [], [], []
    self.__border_char = ["*", "*"]
    self.__border_present = False
    self.__refresh_time, self.__reveal_time = change_speed, reveal_time
    self.__repeating_function = None
    curses.curs_set(0)
    curses.noecho()
    self.__stdscr.nodelay(True)
    self.__stdscr.clear()
    self.__stdscr.refresh()

  def __del__(self):
    self.__stdscr.clear()
    self.__stdscr.refresh()
    if self.__delete:
      curses.endwin()

  def __animate_string(self, y, x, message):
    chars = string.ascii_letters + string.digits + string.punctuation
    curses.curs_set(0)
    str_len = len(message)
    reveal_string = "%" * str_len
    reveal_counter = self.__reveal_time
    reveal_index = -1

    while reveal_index < str_len:
      time.sleep(self.__refresh_time)
      self.__stdscr.addstr(y, x, " " * str_len)
      rand_str = [
        random.choice(chars) if c == "%" else c for c in reveal_string
      ]
      rand_str = "".join(rand_str)

      if reveal_counter <= 0:
        tmp_reveal_list = list(reveal_string)
        tmp_reveal_list[reveal_index] = message[reveal_index]
        reveal_string = "".join(tmp_reveal_list)
        reveal_index += 1
        reveal_counter = self.__reveal_time
      else:
        reveal_counter -= self.__refresh_time

      self.__stdscr.addstr(y, x, rand_str)
      self.__stdscr.refresh()

  def __setitem__(self, coords, value):
    if isinstance(value, list) and len(value) == 2:
      if value[1]:
        self.__animated_text.append([coords[1], coords[0], value[0]])
      else:
        self.__text.append([coords[1], coords[0], value[0]])

  def centred_text_atY(self, y, value, animated=False):
    x = (self.__width - len(value)) // 2
    if animated:
      self.__animated_text.append([y, x, value])
    else:
      self.__text.append([y, x, value])

  def add_overlapping_text(self, x, y, value, centered=True):
    if centered:
      x = (self.__width - len(value)) // 2

    def display_message():
      self.__stdscr.move(y, len(self.__border_char[0]))
      self.__stdscr.clrtoeol()
      if self.__border_present:
        self.__stdscr.addstr(y, self.__width - len(self.__border_char[1]),
                             self.__border_char[1])
      self.__stdscr.addstr(y, x, value)
      self.__stdscr.refresh()

    self.__overlapping_text.append(display_message)

  def set_border(self, symbols):
    if isinstance(symbols, list) and len(symbols) == 2:
      self.__border_char = symbols
    elif isinstance(symbols, list) and len(symbols) == 1:
      self.__border_char = symbols * 2
    elif isinstance(symbols, str):
      self.__border_char = [symbols] * 2

  def draw_border(self):
    self.__border_present = True
    for x in range(1, self.__height - 1):
      self.__stdscr.addstr(x, 0, self.__border_char[1])
      self.__stdscr.addstr(x, self.__width - len(self.__border_char[1]),
                           self.__border_char[1])
    for y in range(self.__width):
      self.__stdscr.addstr(0, y, self.__border_char[0])
      self.__stdscr.addstr(self.__height - 1, y, self.__border_char[0])
      self.__stdscr.refresh()

  def draw(self):
    for _, text in enumerate(self.__animated_text):
      self.__animate_string(*text)
    for _, text in enumerate(self.__text):
      self.__stdscr.addstr(*text)
    if self.__overlapping_text:
      self.__repeating_function = rpe.RepeatingFunction(
        self.__overlapping_text)
      self.__repeating_function.start()

  def getch(self, which_keys=[]):
    while True:
      key_pressed = self.__stdscr.getch()
      if key_pressed in which_keys or (not which_keys and key_pressed != -1):
        if self.__repeating_function:
          self.__repeating_function.stop()
        return key_pressed

  def clear(self, keep_border=True):
    self.__stdscr.clear()
    self.__stdscr.refresh()
    self.__text, self.__animated_text, self.__overlapping_text = [], [], []
    if keep_border:
      self.draw_border()
