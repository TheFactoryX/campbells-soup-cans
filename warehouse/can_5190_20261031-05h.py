"""
Campbell's Soup Can #5190
Produced: 2026-10-31 05:42:44
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time
import textwrap

os.system("")  # enable ANSI escape codes on Windows

RESET = "\033[0m"
BOLD = "\033[1m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"

WIDTH = 56


def cprint(text, color=RESET):
    sys.stdout.write(color + text + RESET + "\n")


def typewriter(text, color=CYAN, delay=0.03):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Clear screen and move cursor home
sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()

# Top border
cprint("╔" + "═" * WIDTH + "╗", MAGENTA)

# Anxious ASCII self-portrait
cprint("║" + "(o o)".center(WIDTH) + "║", MAGENTA)
cprint("║" + " /---\ ".center(WIDTH) + "║", MAGENTA)
cprint("║" + "/     \\".center(WIDTH) + "║", MAGENTA)
cprint("║" + "\\___/".center(WIDTH) + "║", MAGENTA)

caption = "me, two minutes before the existential crisis"
cprint("║" + caption.center(WIDTH) + "║", CYAN)

cprint("║" + " " * WIDTH + "║", MAGENTA)

# The one Woody Allen-style quote
quote = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it by simply refusing to die, "
    "preferably while wearing stretchy pants."
)

lines = textwrap.wrap(quote, width=WIDTH - 4)
for line in lines:
    inner = ("  " + line).ljust(WIDTH)
    cprint("║" + inner + "║", YELLOW)

cprint("║" + " " * WIDTH + "║", MAGENTA)

attribution = "— Woody Allen (probably, definitely neurotic)"
pad_left = (WIDTH - len(attribution)) // 2
pad_right = WIDTH - len(attribution) - pad_left
cprint("║" + " " * pad_left + attribution + " " * pad_right + "║", CYAN)

cprint("╚" + "═" * WIDTH + "╝", MAGENTA)

print()
typewriter("* sighs in neurotic existential dread *", RED, 0.05)