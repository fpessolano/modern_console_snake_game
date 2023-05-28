#ifndef SNAKE_H
#define SNAKE_H

#include "DynamicList.h"
#include <array>

class Snake {
private:
  DynamicList<std::array<int, 2>> coords;
  int minimumSize;

public:
  Snake(int size, int starting_x, int starting_y);

  Snake(int size);

  Snake();
};

// Include the implementation file
#include "../src/Snake.cc"

#endif
