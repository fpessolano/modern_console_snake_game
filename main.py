import curses
import random
import snake as sn
import screen as sc

# setting screen
playfieldHeight = 30
playfieldWidth = 60
screen = sc.Screen(playfieldHeight, playfieldWidth)

# snake
snake = sn.Snake(6, 10, 10)
snake.setPlayfield(playfieldWidth, playfieldHeight)
direction = [1, 0]

# food
random.seed()
food = [random.randint(0, playfieldWidth - 1), random.randint(0, playfieldHeight - 1)]
addFood = True

# support variables
play = True
score = 0

while play:
    if addFood:
        screen.write(food[1], food[0], 'X')
        addFood = False

    command = screen.getCommand()
    if command.cmd == sc.CommandType.END:
        play = False
    elif command.cmd == sc.CommandType.MOVE:
        direction = command.data

    oldPosition = snake.move(direction[0], direction[1])
    currentPosition = snake.getHead()

    if snake.covers(food):
        food = [random.randint(0, playfieldWidth - 1), random.randint(0, playfieldHeight - 1)]
        addFood = True
        snake.grow(1)
        score += 1

    if oldPosition[0] != -1:
        screen.write(oldPosition[1], oldPosition[0], ' ')
    screen.write(currentPosition[1], currentPosition[0], 'O')
    screen.stdscr.refresh()

    curses.napms(50)

print("Your score is:", score)

