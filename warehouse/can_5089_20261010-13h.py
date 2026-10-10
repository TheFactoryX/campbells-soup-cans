"""
Campbell's Soup Can #5089
Produced: 2026-10-10 13:43:24
Worker: inclusionAI: Ling 3.1 Flash (inclusionai/ling-3.1-flash)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
neurotic_wisdom.py — a one-act terminal vaudeville.

Presents exactly ONE philosophical quote in the style of a certain
neurotic genius, complete with twinkling stars, a theater marquee,
candlelight typewriter text (with the occasional on-screen stutter
of self-doubt), and closing applause.

Pure standard library. Best enjoyed in a color-capable terminal.
"""

import random
import shutil
import sys
import textwrap
import time

# ------------------------------------------------------------------ ANSI kit
RESET  = "\033[0m"
BOLD   = "\033[1m"
ITALIC = "\033[3m"
CLEAR  = "\033[2J"
HOME   = "\033[H"
UP1    = "\033[1A"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def rgb(r, g, b):
    """True-color foreground escape sequence."""
    return f"\033[38;2;{r};{g};{b}m"

def lerp(a, b, t):
    return int(a + (b - a) * t)

def candle(t):
    """Warm gradient: molten gold -> buttery cream."""
    return (lerp(255, 255, t), lerp(185, 245, t), lerp(60, 215, t))

BULBS       = [(255, 196, 66), (255, 96, 96), (255, 238, 150), (255, 150, 210)]
STAR_TINTS  = [(170, 190, 255), (255, 255, 225), (200, 255, 245)]

# ----------------------------------------------------------------- the goods
QUOTE = (
    "I don't mind that the universe is meaningless; "
    "I just mind that it's poorly lit, the Wi-Fi is spotty, "
    "and my analyst is on vacation until Tuesday."
)

ATTRIBUTION = "— Woody Allen's anxious cousin, probably"

# ------------------------------------------------------------ flow control
INTERACTIVE = sys.stdout.isatty()   # skip the theatrics when piped

def nap(seconds):
    if INTERACTIVE:
        time.sleep(seconds)

COLS  = shutil.get_terminal_size().columns
WIDTH = max(54, min(COLS - 2, 80))

def centered(text, *style):
    pad = max(0, (WIDTH - len(text)) // 2)
    return " " * pad + "".join(style) + text + RESET

# ------------------------------------------------------------ act one: sky
def starfield(frames=8, height=9):
    cols  = shutil.get_terminal_size().columns
    count = cols * height // 9
    stars = [(random.randrange(cols), random.randrange(height)) for _ in range(count)]
    for _ in range(frames):
        grid = {}
        for (x, y) in stars:
            if random.random() < 0.7:                      # some stars twinkle out
                tint = random.choice(STAR_TINTS)
                grid[(x, y)] = rgb(*tint) + random.choice("*·•✦+·") + RESET
        sys.stdout.write(CLEAR + HOME)
        for y in range(height):
            sys.stdout.write("".join(grid.get((x, y), " ") for x in range(cols)))
            sys.stdout.write("\n")
        sys.stdout.flush()
        nap(0.13)

# ------------------------------------------------- act two: the marquee sign
def bulb_row(phase):
    return "".join(rgb(*BULBS[(i + phase) % len(BULBS)]) + "●" + RESET
                   for i in range(WIDTH))

def marquee(frames=3):
    title = "· O N E   N I G H T   O N L Y ·"
    sub   = "starring: one restless mind, live from your terminal"
    title, sub = title[:WIDTH - 2], sub[:WIDTH - 2]
    for phase in range(frames):                            # chasing lights!
        sys.stdout.write(CLEAR + HOME)
        sys.stdout.write(bulb_row(phase) + "\n\n")
        sys.stdout.write(centered(title, BOLD, rgb(255, 228, 140)) + "\n")
        sys.stdout.write(centered(sub, ITALIC, rgb(165, 215, 255)) + "\n\n")
        sys.stdout.write(bulb_row(phase + 2) + "\n")
        sys.stdout.flush()
        nap(0.45)

# --------------------------------------------- act three: the quote, typed
def typewriter(text, start=0, total=1, delay=0.02):
    for i, ch in enumerate(text):
        color = rgb(*candle((start + i) / max(total, 1)))
        # the occasional neurotic stutter: type it wrong, think better of it
        if INTERACTIVE and ch not in " \n" and random.random() < 0.012:
            sys.stdout.write(color + random.choice("aeioun") + RESET)
            sys.stdout.flush()
            nap(0.07)
            sys.stdout.write("\b \b")                      # erase the doubt
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        if ch in ",;:":
            nap(delay * 14)
        elif ch in ".!?":
            nap(delay * 20)
        elif ch == " ":
            nap(delay * 0.5)
        else:
            nap(delay * random.uniform(0.5, 1.4))

def quote_box(quote):
    inner = WIDTH - 4
    lines = textwrap.wrap(quote, width=inner) or [""]
    amber = rgb(255, 190, 90)
    print(amber + "╭" + "─" * (WIDTH - 2) + "╮" + RESET)
    offset = 0
    for line in lines:
        sys.stdout.write(amber + "│" + RESET + " ")
        sys.stdout.flush()
        typewriter(line, start=offset, total=len(quote))
        offset += len(line)
        sys.stdout.write(" " * (inner - len(line)) + " " + amber + "│" + RESET + "\n")
        sys.stdout.flush()
    print(amber + "╰" + "─" * (WIDTH - 2) + "╯" + RESET)

# ------------------------------------------------------- act four: applause
def applause(times=3):
    bright = centered("✦  ✦  ✦  ✦  ✦", BOLD, rgb(255, 220, 110))
    dim    = centered("✦  ✦  ✦  ✦  ✦", rgb(70, 70, 90))
    for _ in range(times):
        sys.stdout.write(bright + "\n")
        sys.stdout.flush()
        nap(0.4)
        sys.stdout.write(UP1 + dim + "\n")
        sys.stdout.flush()
        nap(0.4)
        sys.stdout.write(UP1)

# ------------------------------------------------------------------- curtain
def main():
    sys.stdout.write(HIDE_CURSOR)
    try:
        starfield()
        marquee()
        sys.stdout.write(CLEAR + HOME)                   # the curtain rises
        sys.stdout.flush()
        nap(0.4)
        quote_box(QUOTE)
        print()
        nap(0.6)
        print(centered(ATTRIBUTION, ITALIC, rgb(150, 225, 255)))
        print()
        nap(0.4)
        applause()
        print()
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()