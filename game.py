import curses
import random
import math
import snake as sn
import graphics as gp
import sounds as sounds

def play(screen, sounds):
    curses.cbreak()
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)

    playfieldHeight = 20
    playfieldWidth = 60
    gameboard = gp.Board(width=playfieldWidth, height=playfieldHeight, screen=screen)

    # snake
    snake = sn.Snake(6, 10, 10)
    snake.setPlayfield(playfieldWidth, playfieldHeight)
    direction = [1, 0]

    # food
    random.seed()
    food = [random.randint(0, playfieldWidth - 1),
            random.randint(0, playfieldHeight - 1)]
    addFood = True
    steps_to_food = 0

    # support variables
    play = True
    score = 0
    frame_delay_max = 100
    maximum_blockage = 5
    blockage = maximum_blockage
    speed_up_sound = False

    gameboard.setup()

    while play:
        if addFood:
            gameboard[food[0], food[1]] = 'X'
            addFood = False
            head_position = snake.getHead()
            steps_to_food = int(
                1.5 * math.sqrt((head_position[0] - food[0])**2 + (head_position[1] - food[1])**2))
            frame_delay = frame_delay_max
        elif (steps_to_food := steps_to_food - 1) < 0:
            frame_delay = max(frame_delay - 1, frame_delay_max // 4)
            if not speed_up_sound:
                # sounds.speedup.play()
                speed_up_sound = True

        gameboard.print_speed(1000//frame_delay)

        command = gameboard.getCommand()
        match command.cmd:
            case gp.CommandType.END:
                play = False
            case gp.CommandType.MOVE:
                if direction[0] != - command.data[0] and direction[1] != - command.data[1]:
                    direction = command.data
            case gp.CommandType.PAUSE:
                gameboard.pause()
                while True:
                    command = gameboard.getCommand()
                    if command.cmd == gp.CommandType.PAUSE:
                        break
                gameboard.pause(False)
            case _:
                pass

        if snake.covers(food):
            food = [random.randint(0, playfieldWidth - 1),
                    random.randint(0, playfieldHeight - 1)]
            addFood = True
            sounds.eaten.play()
            speed_up_sound = False
            snake.grow(2)
            score += 1
            frame_delay_max = max(30, frame_delay_max -
                                score if score % 3 == 0 else frame_delay_max)
            gameboard.print_score(score)

        oldPosition = snake.move(direction[0], direction[1])
        currentPosition = snake.getHead()
        if oldPosition[0] >= 0:
            gameboard[oldPosition[0], oldPosition[1]] = ' '
            blockage = maximum_blockage
        elif oldPosition[0] == -1:
            if (blockage := blockage - 1) == 0:
                break
        gameboard[currentPosition[0], currentPosition[1]] = 'O'
        gameboard.print_snake_size(len(snake))
        gameboard.refresh()
        curses.napms(frame_delay)
    
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    return score

