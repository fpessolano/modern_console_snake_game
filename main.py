import curses
import random
import snake as sn
import game

# setting screen
playfieldHeight = 20
playfieldWidth = 60
screen = curses.initscr()
curses.cbreak()
curses.curs_set(0)
curses.noecho()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
gameboard = game.Board(width=playfieldWidth,
                       height=playfieldHeight, screen=screen)

# snake
snake = sn.Snake(6, 10, 10)
snake.setPlayfield(playfieldWidth, playfieldHeight)
direction = [1, 0]

# food
random.seed()
food = [random.randint(0, playfieldWidth - 1),
        random.randint(0, playfieldHeight - 1)]
addFood = True

# support variables
play = True
score = 0

gameboard.setup()

while play:
    if addFood:
        gameboard[food[0], food[1]] = 'X'
        addFood = False

    command = gameboard.getCommand()
    if command.cmd == game.CommandType.END:
        play = False
    elif command.cmd == game.CommandType.MOVE:
        direction = command.data

    if snake.covers(food):
        food = [random.randint(0, playfieldWidth - 1),
                random.randint(0, playfieldHeight - 1)]
        addFood = True
        snake.grow(1)
        score += 1
        gameboard.print_score(score)

    oldPosition = snake.move(direction[0], direction[1])
    currentPosition = snake.getHead()
    if oldPosition[0] != -1:
        gameboard[oldPosition[0], oldPosition[1]] = ' '
    gameboard[currentPosition[0], currentPosition[1]] = 'O'
    gameboard.print_snake_size(len(snake))
    gameboard.refresh()
    curses.napms(50)


print("Your score is:", score)
