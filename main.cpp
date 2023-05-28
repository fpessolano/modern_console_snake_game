#include <array>
#include <cstdlib>
#include <iostream>
#include <ncurses.h>
#include <random>
#include "include/DynamicList.h"
#include "include/Snake.h"


// need to sample the key faster than the movement of the sname

int main() {
  initscr();
  cbreak();
  noecho();
  curs_set(0);
  keypad(stdscr, TRUE);
  nodelay(stdscr, TRUE);

  // Get screen dimensions
  int screenHeight, screenWidth;
  getmaxyx(stdscr, screenHeight, screenWidth);

  // random generator
  std::random_device rd;
  std::mt19937 gen(rd());
  // std::uniform_int_distribution<int> dis(0, 1);
  std::uniform_int_distribution<int> xDist(0, screenWidth - 1);
  std::uniform_int_distribution<int> yDist(0, screenHeight - 1);

  DynamicList<std::array<int, 2>> coords;
  for (int i = 0; i < 6; i++) {
    coords.pushFront({screenWidth / 2, screenHeight / 2 + i});
  }

  std::array<int, 2> direction{1, 0};
  std::array<int, 2> food{yDist(gen), xDist(gen)};
  bool addFood = true;
  int play = true;
  int score = 0;

  while (play) {

    if (addFood) {
      mvprintw(food[1], food[0], "X");
      addFood = false;
    }

    int ch{0};
    for (int i = 0; i < 3; i++) {
      ch = getch();
      switch (ch) {
      case KEY_UP:
        // currentPosition[1]--;
        direction = {0, -1};
        break;
      case KEY_DOWN:
        // currentPosition[1]++;
        direction = {0, 1};
        break;
      case KEY_LEFT:
        // currentPosition[0]--;
        direction = {-1, 0};
        break;
      case KEY_RIGHT:
        // currentPosition[0]++;
        direction = {1, 0};
        break;
      case 27: // escape to stop
        play = false;
      }
    }

    std::array<int, 2> currentPosition = coords.getHead();
    currentPosition = {currentPosition[0] + direction[0],
                       currentPosition[1] + direction[1]};

    bool grow = false;

    //  with boundary checks
    if (not(currentPosition[0] < 0 || currentPosition[0] >= screenWidth ||
            currentPosition[1] < 0 || currentPosition[1] >= screenHeight)) {
      std::array<int, 2> oldPosition = coords.getTail();
      coords.pushFront(currentPosition);
      if (coords.getIndexInArray(food) == -1) {
        coords.popBack();
      } else {
        food = {xDist(gen), yDist(gen)};
        addFood = true;
        score += 1;
      }
      mvprintw(oldPosition[1], oldPosition[0], " ");
      mvprintw(currentPosition[1], currentPosition[0], "O");
      refresh();
    }

    napms(50);
  }

  endwin();
  std::cout << "Your score is: " << score << std::endl;
  return 0;
}
