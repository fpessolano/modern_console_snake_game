#include "../include/Snake.h"
#include <array>
#include <iostream>

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

void Snake::setScreenSize(int width, int height) {
  screenHeight = width;
  screenWidth = height;
}

void Snake::grow(int moves) { growthMovements += moves; }

std::array<int, 2> Snake::move(int x, int y) {
  // BUG grows on screen border ...
  std::array<int, 2> oldPosition{-1, -1};
  std::array<int, 2> currentPosition{coords.getHead()};
  currentPosition.at(0) += x;
  currentPosition.at(1) += y;
  if (not(currentPosition.at(0) < 0 || currentPosition.at(0) >= screenWidth ||
          currentPosition.at(1) < 0 || currentPosition.at(1) >= screenHeight)) {
    coords.pushFront(currentPosition);
    if (growthMovements == 0) {
      oldPosition = coords.popBack();
    } else {
      --growthMovements;
    }
  }

  return oldPosition;
}

std::array<int, 2> Snake::getHead() { return coords.getHead(); }

bool Snake::covers(std::array<int,2> point) { 
  return coords.getIndexInArray(point) != -1; 
}
