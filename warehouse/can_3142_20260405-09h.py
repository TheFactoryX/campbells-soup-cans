"""
Campbell's Soup Can #3142
Produced: 2026-04-05 09:56:32
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys

# ANSI color codes
RED = "\033[31m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def color(text, code):
    """Wrap text in the given ANSI color code."""
    return f"{code}{text}{RESET}"

def slow_print(text, delay=0.03):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_frame():
    """Print a colorful box around the quote."""
    width = 58
    top_bottom = color("*" * width, YELLOW)
    middle = " " + color("│", CYAN) + " " * (width - 2) + color("│", CYAN)
    print(color(top_bottom, YELLOW))
    print(color(middle, CYAN))
    print(color("│ " + " " * (width - 4) + " │" + RESET + "   ", CYAN))
    print(color("│ " + " " * (width - 4) + " │   " + color("Enjoy the absurd!", YELLOW) + "   │" + RESET, CYAN))
    print(color("│ " + " " * (width - 4) + " │", CYAN))
    print(color(top_bottom, YELLOW))

def main():
    quote = (
        "I’m not afraid of death; I just don’t want to be there when it happens—"
        "especially when I’m still trying to find my car keys."
    )

    draw_frame()
    slow_print(color("\n   ", CYAN), delay=0)                # just a line break
    for line in quote.split("\n"):
        slow_print(color("   " + line + "   ", MAGENTA), delay=0)  # keep alignment    slow_print(color("   ", CYAN), delay=0)
    slow_print(color("   Press Enter to exit...", GREEN), delay=0)
    input()  # wait for user

if __name__ == "__main__":
    main()