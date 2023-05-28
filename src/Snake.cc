#include "../include/Snake.h"

Snake::Snake(int size, int starting_x, int starting_y) {
  minimumSize = size;
  for (int i = 0; i < minimumSize; i--) {
    coords.pushFront({starting_x, starting_y + i});
  }
}

Snake::Snake(int size) { Snake(size, 0, 0); };

Snake::Snake() { Snake(0); }