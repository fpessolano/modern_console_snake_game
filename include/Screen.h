#ifndef SCREEN_H
#define SCREEN_H

#include <vector>

enum CommandType { NONE, END, MOVE };

struct Command {
  CommandType cmd;
  std::vector<int> data;
};

class Screen {
private:
  std::vector<std::vector<char>> matrix;
  int playHeight;
  int playWidth;

public:
  int screenHeight;
  int screenWidth;
  Screen(int rows, int columns);

  ~Screen();

  void write(int row, int column, char value);

  char read(int row, int column);

  Command getCommand(int tries = 3);
};

// Include the implementation file
#include "../src/Screen.cc"

#endif