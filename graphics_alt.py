import curses


class Frame:
  """
    This is a class that handles the drawing in console of each frame.
    """
  
  def __init__(self, width, height, padding=[15, 3], screen=None):
    self.__width = width
    self.__height = height
    self.__paddings = [max(15, padding[0]), max(3, padding[1])]
    self.__background = [[0 for i in range(width)] for j in range(height)]
    self.__stdscr = screen if screen else curses.initscr()
    self.__delete = False if screen else True
    curses.cbreak()
    curses.curs_set(0)
    curses.noecho()
    self.__stdscr.refresh()

  def stdscr(self):
    return self.__stdscr, [self.__width, self.__height], self.__paddings

  def print_board(self):
    for y in range(self.__height):
      self.__stdscr.move(self.__paddings[1] + y, self.__paddings[0])
      self.__stdscr.addstr("<!")
      for x in range(self.__width):
        if self.__background[y][x] == 1:
          self.__stdscr.addstr("[].")
        else:
          self.__stdscr.addstr("  .")
      self.__stdscr.addstr("!>")
    self.__stdscr.move(self.__paddings[1] + self.__height,
                       self.__paddings[0] + 2)
    self.__stdscr.addstr("".join(["=" for i in range(3 * self.__width)]))

  def print_score(self, score):
    self.__stdscr.move(self.__paddings[1] + 1, 2)
    self.__stdscr.addstr("SCORE")
    self.__stdscr.move(self.__paddings[1] + 3, 2)
    self.__stdscr.addstr(str(score))
    self.__stdscr.refresh()

  def print_level(self, level):
    self.__stdscr.move(self.__paddings[1] + 1,
                       self.__paddings[0] + 3 * self.__width + 8)
    self.__stdscr.addstr("LEVEL")
    self.__stdscr.move(self.__paddings[1] + 3,
                       self.__paddings[0] + 3 * self.__width + 10)
    self.__stdscr.addstr(str(level))
    self.__stdscr.refresh()

  def line_count(self, count):
    self.__stdscr.move(self.__paddings[1] + 5,
                       self.__paddings[0] + 3 * self.__width + 8)
    self.__stdscr.addstr("LINES")
    self.__stdscr.move(self.__paddings[1] + 7,
                       self.__paddings[0] + 3 * self.__width + 10)
    self.__stdscr.addstr(str(count))
    self.__stdscr.refresh()

  def screen_refresh(self):
    self.__stdscr.refresh()
    
  def pause(self, on=True):
    if on:
      text = "PAUSED"
    else:
      text = "      "
    self.__stdscr.move(self.__paddings[1] + 10,
                       self.__paddings[0] + 3 * self.__width + 8)
    self.__stdscr.addstr(text)
    self.__stdscr.refresh()

  def print_next_shape(self, shape, max_shape_size=5):
    for y in range(max_shape_size):
      for x in range(max_shape_size):
        self.__stdscr.move(self.__paddings[1] + 7 + y, 2 + x * 2)
        self.__stdscr.addstr("  ")
    self.__stdscr.move(self.__paddings[1] + 5, 2)
    self.__stdscr.addstr("NEXT SHAPE")
    for y in range(len(shape)):
      for x in range(len(shape[y])):
        self.__stdscr.move(self.__paddings[1] + 7 + y, 2 + x * 2)
        if shape[y][x]:
          self.__stdscr.addstr("[]")
        else:
          self.__stdscr.addstr("  ")
    self.__stdscr.refresh()

  def __del__(self):
    self.__stdscr.clear()
    self.__stdscr.refresh()
    if self.__delete:
      curses.endwin()

  def background(self):
    return self.__background

  def __setitem__(self, coords, value):
    if coords[0] >= self.__width or coords[1] >= self.__height or len(
        value) == 0:
      return
    mark, shape = value
    block = "[]" if mark else "  "
    for y, line in enumerate(shape):
      for x, el in enumerate(line):
        if (y + coords[1]) < self.__height and (x + coords[0]) < self.__width:
          self.__stdscr.move(coords[1] + self.__paddings[1] + y,
                             (coords[0] + x) * 3 + self.__paddings[0] + 2)
          if el:
            self.__stdscr.addstr(block)
    self.__stdscr.refresh()

  def __getitem__(self, coords):
    x, y = coords
    if self.__stdscr.inch(self.__paddings[1] + y,
                          self.__paddings[0] + 2 + x * 3) == 32:
      return 0
    else:
      return 1

  def shape_fits(self, shape, coords):
    if coords[0] + len(shape[0]) > self.__width or \
        coords[0] < 0 or coords[1] + len(shape) > self.__height or \
        coords[1] < 0:
      return False
    for y, line in enumerate(shape):
      for x, el in enumerate(line):
        if el and self.__background[coords[1] + y][coords[0] + x]:
          return False
    return True

  def update_background(self):
    for y in range(self.__height):
      for x in range(self.__width):
        self.__background[y][x] = self[x, y]

  def remove_filled_lines(self):
    bck_copy = []
    deleted_rows = 0
    for y in range(self.__height):
      if all(item == 1 for item in self.__background[y]):
        for x in range(self.__width):
          self.__stdscr.move(self.__paddings[1] + y,
                             self.__paddings[0] + 2 + x * 3)
          self.__stdscr.addstr("  .")
        deleted_rows += 1
      else:
        bck_copy.append(self.__background[y])
    for _ in range(deleted_rows):
      bck_copy.insert(0, [0] * self.__width)
    self.__background = bck_copy
    return deleted_rows
