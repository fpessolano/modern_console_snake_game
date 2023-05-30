#ifndef DYNAMIC_LIST_H
#define DYNAMIC_LIST_H

#include <algorithm>
#include <ranges>
#include <vector>

// TODO add destructor

template <typename T> class DynamicList {
private:
  std::vector<T> elements;

public:
  void pushFront(const T &element);

  T popBack();

  T getElementAt(int position) const;

  const T &getHead() const;

  const T &getTail() const;

  int getSize() const;

  int getIndexInArray(const T &target) const;
};

// Include the implementation file
#include "../src/DynamicList.cc"

#endif
