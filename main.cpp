// #include "include/DynamicList.h"
#include "include/Screen.h"
#include "include/Snake.h"
#include "include/types.h"
#include <array>
#include <cstdlib>
#include <iostream>
#include <ncurses.h>
#include <random>

// need to sample the key faster than the movement of the snake
// need a generic collision either using curses or a matrix
// need obstacles
// bombs/food class
// lasers
// frame
// BUG food seem to appear outiside of the frame

int main() {
  // setting screen
  const int playfieldHeight{50};
  const int playfieldWidth{30};
  Screen screen(playfieldHeight, playfieldWidth);

  // snake
  Snake snake(6, 10, 10);
  snake.setPlayfield(playfieldWidth, playfieldHeight);
  std::array<int, 2> direction{1, 0};

  // food
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<int> xDist(0, playfieldWidth - 1);
  std::uniform_int_distribution<int> yDist(0, playfieldHeight - 1);
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

    Command command = screen.getCommand();
    switch (command.cmd) {
    case END:
      play = false;
      break;
    case MOVE:
      direction = {command.data[0], command.data[1]};
      break;
    case NONE:
      break;
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
      screen.write(oldPosition.at(1), oldPosition.at(0), ' ');
    }
    screen.write(currentPosition.at(1), currentPosition.at(0), 'O');
    refresh();

    napms(50);
  }

  std::cout << "Your score is: " << score << std::endl;

  return 0;
}
