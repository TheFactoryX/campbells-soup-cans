"""
Campbell's Soup Can #1932
Produced: 2026-01-29 21:44:03
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, random

# ---------- Helper functions ----------
def ansi(color):
    """Return an ANSI escape sequence for foreground color."""
    fg = {
        'black':   30,
        'red':     31,
        'green':   32,
        'yellow':  33,
        'blue':    34,
        'magenta': 35,
        'cyan':    36,
        'white':   37,
    }
    return f"\033[{fg[color]}m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_spinner(delay=0.15, total=15):
    """Print a rotating spinner while loading."""
    spinner = ["-", "\\", "|", "/"]
    for i in range(total):
        sys.stdout.write(f"\rProcessing {spinner[i % len(spinner)]}   ")
        sys.stdout.flush()
        time.sleep(delay)

def print_colored(text):
    """Print a line where each word gets a random foreground color."""
    words = text.split()
    colors = random.choices(list(ansi.values()), k=len(words))
    for w, c in zip(words, colors):
        sys.stdout.write(f"{c}{w}{c}{' '}"[:-1])  # space after each word
        sys.stdout.flush()
        time.sleep(0.02)          # tiny pause for drama
    sys.stdout.write("\n")
    sys.stdout.flush()

def ascii_art():
    """A tiny Woody‑Allen‑style ASCII coffee cup."""
    art = r"""
      __________      ___
     /  _____  \    /  \`       ___
    /  /    \ \    /   \       /  \
   \  \   \ \ \___/    \      /   /
    \   \  \         \    \    \ /
     \__________   ___   \  \__/
"""
    sys.stdout.write(art + "\n")
    sys.stdout.flush()

# ---------- Main program ----------
def main():
    clear_screen()
    ascii_art()
    print_spinner(delay=0.12, total=12)   # little pre‑loading drama

    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    # Insert a tiny box around the quote
    box_top = "+────────────────────────────────────────────────────────────+"
    box_bottom = box_top
    line = f"|                                                       |"
    width = max(len(box_top), len(line))

    # Print opening line of the box
    sys.stdout.write(box_top + "\n")
    sys.stdout.flush()

    # Animated entry of each character (with random colors)
    chars = list(quote)
    for i in range(len(chars)):
        col = random.choice(list(ansi.values()))
        sys.stdout.write(f"{col}{chars[i]}{col}{' '}" if i != len(chars)-1 else "\n")
        sys.stdout.flush()
        time.sleep(0.07)   # make it feel like typing

    # Closing line of the box
    sys.stdout.write(box_bottom + "\n")
    sys.stdout.flush()
    # Final visual flourish
    print("\n", end="")
    for f in range(30):
        sys.stdout.write("\b\u2013")  # backspace + em dash
        sys.stdout.flush()
        time.sleep(0.02)
    # Print the quote again in a random‑colored, nicely formatted line
    print_colored(quote)

if __name__ == "__main__":
    main()