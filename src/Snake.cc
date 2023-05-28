#include "../include/Snake.h"
#include <array>

Snake::Snake(int size, int starting_x, int starting_y, bool vertical) {
  minimumSize = size;
  growthMovements = 0;
  if (vertical) {
    for (int i = 0; i < minimumSize; i++) {
      coords.pushFront({starting_x, starting_y + i});
    }
  } else {
    for (int i = 0; i < minimumSize; i++) {
      coords.pushFront({starting_x + i, starting_y});
    }
  }
}

Snake::Snake(int size, int starting_x, int starting_y) {
  { Snake(size, starting_x, starting_y, false); };
}

Snake::Snake(int size) { Snake(size, 0, 0); };

Snake::Snake() { Snake(0); }

void Snake::grow(int moves) { growthMovements += moves; }

std::array<int, 2>& Snake::move(int x, int y) {
  // to be done
  std::array<int, 2> notMoved{-1,-1};
  return notMoved;
}
