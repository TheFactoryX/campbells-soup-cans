"""
Campbell's Soup Can #2482
Produced: 2026-02-28 11:31:31
Worker: Goliath 120B (alpindale/goliath-120b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import curses
import curses.unctrl # for ANSI escape sequences
def cls():
    curses.culup(0)
    curses.cursup(0)
    while True:
        curses.addstr(0, 0, ' '*curses.getyx()[1]+curses.unctrl('B'*(curses.getyx()[0]//2+1))+curses.unctrl('D'*(curses.getyll()//2+1)))
        time.sleep(char_delay)
        if candidate:
            candidate = candidate[1:]
        else:
            candidate = curses.getch()
        if candidate and candidate in ('q', curses.dok):
            curses.addstr(0, 0, "\r    [ESCAPE] PRESSed, QUITTING...\r\n")
            time.sleep(2)
            curses.nocbreak()
            curses.curs_set(1)
            curses.endwin()
            exit(0)
        if candidate and candidate in (curses.clr, curses.cle):
            candidate = ''
            cls()
            break
        if candidate and candidate in (' '+chr(13)+' '):
            candidate = candidate[1:]
            try:
                char_delay = int(candidate)
            except ValueError:
                pass
        else:
            candidate = chr(0)

curses.curs_set(0)
curses.noecho()
curses.initscr()
std_y, std_x = curses.getyx()
std_clr = curses.cle
char_delay = 0.1
candidate = ''
cl BEEP = '\a'

def clear_screen():
    curses.cursup(0)
    curses.cursup(0)
    while True:
        line = BEEP * curses.getyx()[1]
        while len(line) < curses.COLS:
            line += BEEP
        curses.addstr(0, 0, line+' '*len(line))
        time.sleep(0.05)
        if candidate and candidate in (curses.clr, curses.cle):
            break
        if candidate:
            candidate = candidate[1:]
    curses.cursup(std_y - 3)
    curses.cursup(std_x - len('  [' + str(round(char_delay, 2) * 10) + ']  '))
    curses.addstr('  [' + str(round(char_delay, 2) + ']  ' + ' ' * (curses.maxx - len('  [' + str(round(char_delay, 2) * 10) + ']  '))))

def print_quote(q):
    for l in q.split('\n'):
        if len(l) > 0 and l[-1] != BEEP:
            l += BEEP
        for c in l:
            if c == BEEP:
                curses.addstr(c)
                curses.cursup(1)
                time.sleep(char_delay)
            else:
                curses.addch(ord(c))
                time.sleep(char_delay)
        time.sleep(char_delay)

quote = """

  _       _         
 | |     / \  BEEP, 
 | |    / _ \  BEEP, BEEP, 
  | |   /_ \_\  BEEP, BEEP, BEEP, aLl 
 /|   /   \_\  BEEP, BEEP, BEEP, BEEP 
/ |  /     \ \_  BEEP, BEEP, BEEP,  BEEP 
  | /       ____\  BEEP, BEEP, BEEP,   BEEP
   | |     ________/ BEEP, BEEP,   BEEP,  
    | |    /    \      BEEP,   BEEP,     
     |_|  /      \     BEEP, 
                  \/ 
                            BEEP
                            
                  another