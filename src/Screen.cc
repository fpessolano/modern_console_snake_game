#include "../include/Screen.h"
#include <ncurses.h>


Screen::Screen(int rows, int columns) : matrix(rows, std::vector<char>(columns, ' ')) {
  initscr();
  cbreak();
  noecho();
  curs_set(0);
  keypad(stdscr, TRUE);
  nodelay(stdscr, TRUE);
  getmaxyx(stdscr, screenHeight, screenWidth);
  playWidth = columns;
  playHeight = rows;
}

void Screen::write(int row, int column, char value) {
  mvprintw(row, column, "%c", value);
  matrix[row][column] = value;
}

Screen::~Screen() { endwin(); }

char Screen::read(int row, int column) { return matrix[row][column]; }

Command Screen::getCommand(int tries) {
  Command cmd;
  cmd.cmd = CommandType::NONE;
  for (int i = 0; i < tries; i++) {
    int ch{getch()};
    switch (ch) {
    case KEY_UP:
      cmd.cmd = CommandType::MOVE;
      cmd.data = {0,-1};
      break;
    case KEY_DOWN:
      cmd.cmd = CommandType::MOVE;
      cmd.data = {0,1};
      break;
    case KEY_LEFT:
      cmd.cmd = CommandType::MOVE;
      cmd.data = {-1,0};
      break;
    case KEY_RIGHT:
      cmd.cmd = CommandType::MOVE;
      cmd.data = {1,0};
      break;
    case 27: // escape
      cmd.cmd = CommandType::END;
    }
  }
  return cmd;
}