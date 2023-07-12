# move to python in progress

import page
import curses
# import sounds as sounds


VERSION = "v.0.2.0"

screen = curses.initscr()  # type: ignore
# sounds = sounds.Bit8()

# Title Page
static_page = page.Static(width=60, height=20, screen=screen)
static_page.centred_text_atY(5, "It is modern console snake", True)
static_page.centred_text_atY(7, VERSION)
static_page.add_overlapping_text(0, 14, "Press p to play")
static_page.add_overlapping_text(0, 14, "Press c for controls")
static_page.draw_border()
static_page.draw()
option = static_page.getch([ord("p"), ord("c")])

if option == ord("c"):
    # optional controls page
    static_page.clear()
    static_page[12, 5] = ["left arrow\t->\t move left", False]
    static_page[12, 6] = ["right arrow\t->\t move right", False]
    static_page[12, 7] = ["down arrow\t->\t move down", False]
    static_page[12, 8] = ["up arrow\t->\t move up", False]
    static_page[12, 9] = ["space\t->\t pause game", False]
    static_page[12, 10] = ["esc\t \t->\t sudden quit", False]
    static_page.add_overlapping_text(0, 14, "Press any key to play")
    static_page.add_overlapping_text(0, 14, "")
    static_page.draw()
    static_page.getch([])

# static_page.clear(False)
# sounds.play_music()

# while True:
#     true game loop

#     sounds.stop_music()
#     sounds.gameover.play()
#     screen.clear()
#     screen.refresh()
#     score, level = new_game.score()

#     static_page.clear(False)
#     static_page.centred_text_atY(5, "GAME OVER !!!")
#     static_page.centred_text_atY(7, "your score: " + str(score))
#     static_page.centred_text_atY(10, "your level: " + str(level))
#     static_page.add_overlapping_text(0, 14, "Press p to play")
#     static_page.add_overlapping_text(0, 14, "Press q to quit")
#     static_page.draw_border()
#     static_page.draw()
#     option = static_page.getch([ord("p"), ord("q")])
#     static_page.clear(False)
#     if option == ord("q"):
#         break
#     sounds.gameover.stop()
#     sounds.play_music()

static_page.clear(False)
curses.endwin()  # type: ignore