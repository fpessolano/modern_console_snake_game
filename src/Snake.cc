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

void Snake::setPlayfield(int width, int height) {
  screenHeight = width;
  screenWidth = height;
}

void Snake::grow(int moves) { growthMovements += moves; }

std::array<int, 2> Snake::peek_move(int x, int y) {
  std::array<int, 2> invalidMove{-1, -1};
  std::array<int, 2> currentPosition{coords.getHead()};
  currentPosition.at(0) += x;
  currentPosition.at(1) += y;
  if (coords.getIndexInArray(currentPosition) != -1) {
    // this is temporary, does not always work obviously
    currentPosition.at(0) -= 2*x;
    currentPosition.at(1) -= 2*y;
  }
  if (currentPosition.at(0) >= 0 and currentPosition.at(0) < screenWidth and
      currentPosition.at(1) >= 0 and currentPosition.at(1) <screenHeight) {
    return currentPosition;
  }

  return invalidMove;
}

std::array<int, 2> Snake::move(int x, int y) {
  std::array<int, 2> oldPosition{-1, -1};
  std::array<int, 2> headPosition{peek_move(x,y)};
  if (headPosition.at(0)!=-1) {
    coords.pushFront(headPosition);
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
