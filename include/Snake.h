#ifndef SNAKE_H
#define SNAKE_H

#include "DynamicList.h"
#include <array>

class Snake {
private:
  DynamicList<std::array<int, 2>> coords;
  int minimumSize;
  int growthMovements;

public:
  Snake(int size, int starting_x, int starting_y, bool vertical);

  Snake(int size, int starting_x, int starting_y);

  Snake(int size);

  Snake();

  void grow(int moves);

  std::array<int, 2>& move(int x, int y);
};

// Include the implementation file
#include "../src/Snake.cc"

#endif
