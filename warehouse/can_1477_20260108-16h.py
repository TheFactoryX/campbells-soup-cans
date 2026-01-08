"""
Campbell's Soup Can #1477
Produced: 2026-01-08 16:48:52
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# ANSI color codes
RESET   = "\033[0m"
GREEN   = "\033[32m"
CYAN    = "\033[36m"
YELLOW_BOLD = "\033[1;33m"
RED     = "\033[31m"

# Quote to display
quote   = "Life is like an unwritten joke—I keep waiting for the punchline that never comes."
author  = " —Woody Allen (sort of)"
full_line = f' "{quote}" {author}'

# Box dimensions
WIDTH = 70
TOP    = GREEN + "┌" + "─"*(WIDTH-2) + "┐" + RESET
BOTTOM = GREEN + "└" + "─"*(WIDTH-2) + "┘" + RESET
SIDE   = GREEN + "│" + RESET

def pad(line):
    # line includes the surrounding spaces already added
    return SIDE + " " + line.ljust(WIDTH-4) + " " + SIDE + RESET

padded = pad(full_line)

def animate_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Animate the box
animate_print(TOP)
animate_print(padded)
animate_print(BOTTOM)

# Pause and exit prompt
time.sleep(0.5)
print(YELLOW_BOLD + "Press Enter to exit..." + RESET, end='', flush=True)
input()