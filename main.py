# move to python in progress

import page
import curses

VERSION = "v.0.1.0"

screen = curses.initscr()  # type: ignore

# Title Page
static_page = page.Static(width=60, height=20, screen=screen)
static_page.centred_text_atY(5, "It is modern console snake", True)
static_page.centred_text_atY(7, VERSION)
static_page.add_overlapping_text(0, 14, "Press p to play")
static_page.add_overlapping_text(0, 14, "Press c for controls")
static_page.draw_border()
static_page.draw()
option = static_page.getch([ord("p"), ord("c")])

static_page.clear(False)
curses.endwin()  # type: ignore