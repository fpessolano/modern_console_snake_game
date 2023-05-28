#include "include/DynamicList.h"
#include <array>
#include <iostream>

void printArray(const std::array<int, 2> arr) {
  int size = arr.size();
  if (size <= 0) {
    std::cout << "Array is empty.";
    return;
  }

  std::cout << "[ ";
  for (int i = 0; i < size; ++i) {
    std::cout << arr[i];
    if (i != size - 1) {
      std::cout << ", ";
    }
  }
  std::cout << " ]";
}

int main_test() {
  DynamicList<std::array<int, 2>> myList;

  myList.pushFront({1, 2});
  myList.pushFront({2, 3});
  myList.pushFront({3, 4});
  myList.pushFront({4, 5});
  myList.pushFront({5, 6});
  myList.pushFront({6, 7});

  std::cout << "Head: ";
  printArray(myList.getHead());
  std::cout << std::endl;
  std::cout << "Tail: ";
  printArray(myList.getTail());
  std::cout << std::endl;

  std::cout << "Element at position 1: ";
  printArray(myList.getElementAt(1));
  std::cout << std::endl;

  for (int i = 0; i < 8; i++) {
    if (myList.getSize() > 0) {
      std::cout << "Popped element: ";
      printArray(myList.popBack());
      std::cout << std::endl;
    }

    std::cout << "List size: " << myList.getSize() << std::endl;
  }

  return 0;
}
