from dynamic_list import DynamicList

class Snake:
    def __init__(self, size: int = 5, starting_x: int = 0, starting_y: int = 0, vertical: bool = False):
        self.minimumSize = size
        self.growthMovements = 0
        self.screenHeight = 0
        self.screenWidth = 0
        self.coords = DynamicList()

        if vertical:
            for i in range(self.minimumSize):
                self.coords.pushFront([starting_x, starting_y + i])
        else:
            for i in range(self.minimumSize):
                self.coords.pushFront([starting_x + i, starting_y])

    def setPlayfield(self, width: int, height: int) -> None:
        self.screenHeight = height
        self.screenWidth = width

    def grow(self, moves: int) -> None:
        self.growthMovements += moves

    def peek_move(self, x: int, y: int):
        invalidMove = [-1, -1]
        currentPosition = self.coords.getHead().copy()
        currentPosition[0] += x
        currentPosition[1] += y

        if self.coords.getIndexInArray(currentPosition) != -1:
            return invalidMove

        if (0 <= currentPosition[0] < self.screenWidth and
                0 <= currentPosition[1] < self.screenHeight):
            return currentPosition

        return invalidMove

    def move(self, x: int, y: int):
        oldPosition = [-1, -1]
        headPosition = self.peek_move(x, y)

        if headPosition[0] != -1:
            self.coords.pushFront(headPosition)

            if self.growthMovements == 0:
                oldPosition = self.coords.popBack()
            else:
                self.growthMovements -= 1
                oldPosition = [-2, -2]

        return oldPosition

    def getHead(self):
        return self.coords.getHead()

    def covers(self, point):
        return self.coords.getIndexInArray(point) != -1
    
    def __len__(self):
        return self.coords.getSize()
    

if __name__ == "__main__":
    # Example usage
    snake = Snake(size=4, starting_x=2, starting_y=2, vertical=True)
    snake.setPlayfield(width=10, height=10)

    print("Initial Head Position:", snake.getHead())
    print("Covers (2, 3):", snake.covers([2, 3]))
    print("Covers (5, 2):", snake.covers([5, 2]))

    snake.grow(2)

    print("After Growth, Head Position:", snake.getHead())

    snake.move(0, 1)
    snake.move(0, 1)
    snake.move(1, 0)

    print("After Moves, Head Position:", snake.getHead())
    print("Covers (2, 3):", snake.covers([2, 3]))
    print("Covers (5, 2):", snake.covers([5, 2]))