#include "DynamicList.h"

template<typename T>
void DynamicList<T>::pushFront(const T& element) {
    elements.insert(elements.begin(), element);
}

template<typename T>
T DynamicList<T>::popBack() {
    if (elements.empty()) {
        return;
    }

    T poppedElement = elements.back();
    elements.pop_back();
    return poppedElement;
}

template<typename T>
T DynamicList<T>::getElementAt(int position) const {
    return elements.at(position);
}

template<typename T>
const T& DynamicList<T>::getHead() const {
    return elements.front();
}

template<typename T>
const T& DynamicList<T>::getTail() const {
    return elements.back();
}

template<typename T>
int DynamicList<T>::getSize() const {
    int size = elements.size();
    return (size >= 0) ? size : 0;
}
