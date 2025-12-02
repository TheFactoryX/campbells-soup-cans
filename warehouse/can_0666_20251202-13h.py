"""
Campbell's Soup Can #666
Produced: 2025-12-02 13:48:51
Worker: OpenAI: o3 (openai/o3)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny one-file show that delivers a single, neurotic,
existential-yet-playful quip in the spirit of Woody Allen.
No external libraries required—just a terminal that
understands ANSI escape codes.
"""

import sys
import time
import shutil
import itertools

# ---- ANSI COLORS & EFFECTS ---------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
BLINK   = "\033[5m"

FG = {
    'red'    : "\033[31m",
    'green'  : "\033[32m",
    'yellow' : "\033[33m",
    'blue'   : "\033[34m",
    'magenta': "\033[35m",
    'cyan'   : "\033[36m",
    'white'  : "\033[37m",
}

# ---- ASCII ART ---------------------------------------------------------------
GLASSES = r"""
        .-""""-.
       / -   -  \
      |  .-. .- |
      |  \o| |o (
      \     ^   /
       '.  )--'`
         '-...-' 
"""

THOUGHT_BUBBLE = [
"            ( )",
"          (     )",
"        (         )",
"      (   *. *. *.  )",
"     (   *. *. *. *. )",
"    (_______________)",
]

# ---- THE QUOTE ---------------------------------------------------------------
QUOTE = (
    "I finally grasped the meaning of existence: "
    "it's like waiting at the DMV—you’re not sure why you’re there, "
    "the magazines are from 1998, and when your number's called "
    "you still fail the vision test."
)

# ---- HELPER FUNCTIONS --------------------------------------------------------
def slow_print(text, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def center(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def animate_bubble(frames=3, pause=0.2):
    """
    Pulsates the thought bubble a little for comic effect.
    """
    for i in range(frames):
        for line in THOUGHT_BUBBLE:
            color = FG['cyan'] if i % 2 == 0 else FG['magenta']
            print(center(color + line + RESET))
        time.sleep(pause)
        # move cursor up to redraw bubble
        sys.stdout.write(f"\033[{len(THOUGHT_BUBBLE)}A")

def typewriter_quote():
    accent_colors = itertools.cycle([
        FG['yellow'], FG['white'], FG['yellow'], FG['white']
    ])
    for word in QUOTE.split():
        color = next(accent_colors)
        slow_print(color + word + RESET + ' ', delay=0.05, newline=False)
    print()  # final newline

# ---- MAIN --------------------------------------------------------------------
def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print glasses art
    for line in GLASSES.splitlines():
        print(center(FG['yellow'] + line + RESET))
    print()

    # Animate thought bubble
    animate_bubble()

    # Move cursor down after animation so bubble stays
    sys.stdout.write(f"\033[{len(THOUGHT_BUBBLE)}B")

    # Print the quote with a typewriter effect
    print()
    print(center(BOLD + FG['red'] + "Existential Observation:" + RESET))
    print()
    typewriter_quote()

    print("\n" + center(DIM + ITALIC + "— a profoundly anxious insight —" + RESET))
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET)  # ensure colors are reset on Ctrl-C