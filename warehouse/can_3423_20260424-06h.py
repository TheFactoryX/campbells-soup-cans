"""
Campbell's Soup Can #3423
Produced: 2026-04-24 06:20:23
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"
BOLD = "\033[1m"

QUOTE = "I'm not lazy; I'm just in energy‑saving mode… for eternity."
WIDTH = len(QOTE) + 4  # padding inside box

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_boxed(text, color):
    top = f"{color}╔{'═' * (len(text) + 2)}╗{RESET}"
    middle = f"{color}║ {BOLD}{text}{RESET}{color} ║{RESET}"
    bottom = f"{color}╚{'═' * (len(text) + 2)}╝{RESET}"
    print(top)
    print(middle)
    print(bottom)

def animate():
    for i in range(6):
        clear_screen()
        color = COLORS[i % len(COLORS)]
        print_boxed(QUOTE, color)
        time.sleep(0.5)
    # final static version
    clear_screen()
    print_boxed(QUOTE, "\033[97m")  # bright white

if __name__ == "__main__":
    animate()