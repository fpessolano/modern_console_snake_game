from typing import TypeVar, List

T = TypeVar('T')

class DynamicList:
    def __init__(self):
        self.__elements = []

    def pushFront(self, element: T) -> None:
        self.__elements.insert(0, element)

    def popBack(self) -> T:
        if self.__elements:
            return self.__elements.pop()
        else:
            return None

    def getElementAt(self, position: int) -> T:
        return self.__elements[position]

    def getHead(self) -> T:
        return self.__elements[0] if self.__elements else None

    def getTail(self) -> T:
        return self.__elements[-1] if self.__elements else None

    def getSize(self) -> int:
        return len(self.__elements)

    def getIndexInArray(self, target: T) -> int:
        try:
            return self.__elements.index(target)
        except ValueError:
            return -1


if __name__ == "__main__":
    # Example usage
    list1 = DynamicList()

    list1.pushFront([1,2])
    list1.pushFront(20)
    list1.pushFront(30)

    print("Size of the list:", list1.getSize())
    print("Head of the list:", list1.getHead())
    print("Tail of the list:", list1.getTail())
    print("Element at index 1:", list1.getElementAt(1))
    print("Index of value 20:", list1.getIndexInArray(20))

    popped_value = list1.popBack()
    print("Popped value from the list:", popped_value)