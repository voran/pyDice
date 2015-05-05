from random import randint
from sys import stdin
import curses

def draw(number):
    screen.move(0,0)
    screen.erase()
    height,width = screen.getmaxyx()
    screen.move(height // 2, width // 2)
    screen.addstr(str(number), curses.A_BOLD)
    screen.move(height - height // 10, width // 10)
    screen.addstr("q: EXIT")
    screen.move(height - height // 10 + 1, width // 10)
    screen.addstr("Any other key: ROLL")


if __name__ == "__main__":
    try:
        screen = curses.initscr()
        curses.curs_set(0)

        while 1:
            draw(randint(1,6) + randint(1,6))
            if screen.getch() == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()
