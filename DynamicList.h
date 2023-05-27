#ifndef DYNAMIC_LIST_H
#define DYNAMIC_LIST_H

#include <vector>

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
};

// Include the implementation file
#include "DynamicList.cc"

#endif
