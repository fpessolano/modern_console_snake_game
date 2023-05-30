#ifndef SNAKE_H
#define SNAKE_H

#include "DynamicList.h"
#include <array>

// TODO add destructor
// TODO add collision check

class Snake {
private:
  int minimumSize;
  int growthMovements;
  int screenHeight, screenWidth;
  DynamicList<std::array<int, 2>> coords;

public:
  Snake(int size = 5, int starting_x = 0, int starting_y = 0,
        bool vertical = false);

  void setScreenSize(int width, int height);

  void grow(int moves);

  std::array<int, 2> move(int x, int y);

  std::array<int, 2> getHead();

  bool covers(std::array<int,2> point);
};

// Include the implementation file
#include "../src/Snake.cc"

#endif
