"""
Campbell's Soup Can #4736
Produced: 2026-08-21 05:48:11
Worker: Ox Alpha (stealth/ox-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
   D E E P   T H O U G H T S   &   S H A L L O W   B R E A T H I N G
--------------------------------------------------------------------
   An unnecessarily dramatic philosophical quotation device.
   100% standard library. Side effects may include mild sighing,
   sudden clarity, and the urge to cancel your weekend plans.
====================================================================
"""

import os
import sys
import time

# ------------------------------------------------------------ ANSI setup
if os.name == "nt":
    os.system("")          # politely wake up ANSI support on Windows

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"

RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
GREY    = "\033[90m"

RAINBOW = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

BOX_W   = 58            # inner width of the grand quote box

QUOTE = ("I've made peace with death — we meet Tuesdays at four, "
         "and frankly, he's very disappointed in my progress.")

ATTRIBUTION = "— one very nervous philosopher"


# ------------------------------------------------------------ tiny helpers
def flush():
    sys.stdout.flush()


def nap(seconds):
    time.sleep(seconds)


def clear():
    sys.stdout.write("\033[2J\033[H")
    flush()


def print_centered(text, width, color="", style=""):
    pad = max(0, (width - len(text)) // 2)
    print(" " * pad + style + color + text + RESET)


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = (cur + " " + w) if cur else w
        if len(cand) <= width:
            cur = cand
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------ showpieces
def rainbow_type(text, delay=0.035):
    for i, ch in enumerate(text):
        sys.stdout.write(RAINBOW[i % len(RAINBOW)] + ch)
        flush()
        nap(delay)
    sys.stdout.write(RESET + "
")


def progress_bar(label, width=30, delay=0.02):
    for i in range(width + 1):
        bar = "█" * i + "░" * (width - i)
        pct = round(i / width * 100)
        sys.stdout.write(
            f"\r{GREY}{label:<36}{RESET} {YELLOW}[{bar}]{RESET} {pct:3d}% "
        )
        flush()
        nap(delay)
    sys.stdout.write("
")


def spin_thought(message, cycles=14, delay=0.11):
    frames = "-\\|/"
    for i in range(cycles):
        sys.stdout.write(f"\r{MAGENTA}{message} {frames[i % 4]}{RESET}  ")
        flush()
        nap(delay)
    sys.stdout.write(f"\r{GREEN}{message} ... concluded.{RESET}      
")


FACE = [
    '      .-"""""""-.',
    '     /  _     _  \',
    '    |  (o)   (o)  |',
    '    |     ,_,     |',
    '     \\   \\___/   /',
    "      '-.......-'",
    '         |   |',
    '        /|   |\',
    '       d |   | b',
]

DROP_FRAMES = [
    {(0, 1): "°", (18, 3): "°"},
    {(1, 4): "°", (17, 0): "°"},
    {(0, 6): "°", (18, 2): "°"},
]


def render_face(drops):
    grid = [list(line.ljust(20)) for line in FACE]
    for (col, row), ch in drops.items():
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
            grid[row][col] = ch
    return ["".join(row) for row in grid]


def animate_face(frames=9, delay=0.22):
    for i in range(frames):
        block = render_face(DROP_FRAMES[i % len(DROP_FRAMES)])
        for line in block:
            sys.stdout.write(CYAN + line.replace("°", MAGENTA + "°" + CYAN) + RESET + "
")
        flush()
        nap(delay)
        if i < frames - 1:
            sys.stdout.write(f"\033[{len(block)}A\r")


def boxed_quote(quote):
    body = wrap("“" + quote + "”", BOX_W - 4)
    pad = 1
    rows = [""] * pad + body + [""] * pad
    height = len(rows)

    top    = "╔" + "═" * BOX_W + "╗"
    bottom = "╚" + "═" * BOX_W + "╝"
    blank  = "║" + " " * BOX_W + "║"

    print(CYAN + BOLD + top + RESET)
    for _ in range(height):
        print(blank)
    print(CYAN + BOLD + bottom + RESET)

    sys.stdout.write(f"\033[{height + 1}A")     # climb back inside the box

    for idx, line in enumerate(rows):
        if line:
            col = 2 + (BOX_W - len(line)) // 2
            sys.stdout.write(f"\r\033[{col}G" + YELLOW + BOLD)
            for ch in line:
                sys.stdout.write(ch)
                flush()
                nap(0.028)
            sys.stdout.write(RESET)
        else:
            sys.stdout.write("\r")
        if idx < height - 1:
            sys.stdout.write("\033[1B")

    sys.stdout.write("\033[2B\r")               # step back out, gracefully
    flush()
    return height


def shimmer_borders(height, rounds=2, delay=0.08):
    for _ in range(rounds):
        for color in RAINBOW:
            sys.stdout.write(f"\033[{height + 2}A\r")
            sys.stdout.write(color + BOLD + "╔" + "═" * BOX_W + "╗" + RESET + "
")
            sys.stdout.write(f"\033[{height + 1}B\r")
            sys.stdout.write(color + BOLD + "╚" + "═" * BOX_W + "╝" + RESET + "
")
            flush()
            nap(delay)


def pulse_tagline(tagline, colors=None, delay=0.25):
    colors = colors or [GREEN, YELLOW, GREEN, YELLOW, GREEN]
    for color in colors:
        sys.stdout.write("\r" + color + BOLD + tagline + RESET)
        flush()
        nap(delay)
    print()


# ------------------------------------------------------------ the show
def main():
    clear()
    nap(0.3)

    rainbow_type("✦ ✦ ✦   DEEP THOUGHTS & SHALLOW BREATHING   ✦ ✦ ✦")
    print_centered("an unnecessary philosophical emergency broadcast", 54, GREY, ITALIC)
    print()

    animate_face()
    print()

    progress_bar("Importing existential dread")
    progress_bar("Watering the anxiety plant")
    progress_bar("Reorganizing the closet of the soul")
    print()

    spin_thought("Consulting the abyss")
    nap(0.5)

    clear()
    nap(0.4)

    height = boxed_quote(QUOTE)
    shimmer_borders(height)

    print()
    print_centered(ATTRIBUTION, BOX_W + 2, CYAN, ITALIC)
    print()
    pulse_tagline("✦  THE MORE YOU KNOW, THE LESS YOU SLEEP  ✦")
    print_centered("* no philosophers were harmed — several were mildly startled *",
                   BOX_W + 2, GREY, DIM)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "

Interrupted mid-crisis. How fitting." + RESET)