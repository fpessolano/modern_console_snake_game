// #include "include/DynamicList.h"
#include "include/Snake.h"
#include <array>
#include <cstdlib>
#include <iostream>
#include <ncurses.h>
#include <random>

// need to sample the key faster than the movement of the snake
// need a generic collision (used screen information?)

int main() {
  // setting screen
  initscr();
  cbreak();
  noecho();
  curs_set(0);
  keypad(stdscr, TRUE);
  nodelay(stdscr, TRUE);
  const int screenHeight{50};
  const int screenWidth{30};
  // getmaxyx(stdscr, screenHeight, screenWidth);

  // snake
  Snake snake(6, 10, 10);
  snake.setScreenSize(screenWidth, screenHeight);
  std::array<int, 2> direction{1, 0};

  // food
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<int> xDist(0, screenWidth - 1);
  std::uniform_int_distribution<int> yDist(0, screenHeight - 1);
  std::array<int, 2> food{yDist(gen), xDist(gen)};
  bool addFood = true;

  // support variables
  int play = true;
  int score = 0;

  while (play) {

    if (addFood) {
      mvprintw(food.at(1), food.at(0), "X");
      addFood = false;
    }

    int ch{0};
    for (int i = 0; i < 3; i++) {
      ch = getch();
      switch (ch) {
      case KEY_UP:
        direction = {0, -1};
        break;
      case KEY_DOWN:
        direction = {0, 1};
        break;
      case KEY_LEFT:
        direction = {-1, 0};
        break;
      case KEY_RIGHT:
        direction = {1, 0};
        break;
      case 27: // escape to stop
        play = false;
      }
    }

    std::array<int, 2> oldPosition{
        snake.move(direction.at(0), direction.at(1))};
    std::array<int, 2> currentPosition{snake.getHead()};

    if (snake.covers(food)) {
      food = {xDist(gen), yDist(gen)};
      addFood = true;
      snake.grow(1);
      score += 1;
    }

    if (oldPosition.at(0) != -1) {
      mvprintw(oldPosition.at(1), oldPosition.at(0), " ");
    }
    mvprintw(currentPosition.at(1), currentPosition.at(0), "O");
    refresh();

    napms(50);
  }

  endwin();
  std::cout << "Your score is: " << score << std::endl;

  return 0;
}
