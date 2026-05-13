"""
Campbell's Soup Can #3660
Produced: 2026-05-13 00:13:25
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os

# ANSI escape sequences for colors and formatting
RESET  = "\033[0m"
BOLD   = "\033[1m"
ITALIC = "\033[3m"
UNDER  = "\033[4m"

# Colors
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
GRAY    = "\033[90m"

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter animation
def typewriter(text, delay=0.04, color=WHITE):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Draw a colorful box around the quote
def draw_box(lines, color1=CYAN, color2=YELLOW, width=None):
    if width is None:
        width = max(len(line) for line in lines) + 2
    top = f"{color1}╭" + "─" * width + "╮{RESET}"
    bottom = f"{color1}╰" + "─" * width + "╯{RESET}"
    print(top)
    for line in lines:
        padded = line.ljust(width)
        print(f"{color2}│{color1} {padded} {color2}│")
    print(bottom)

# Main program
def main():
    clear()
    quote = (
        "I never understand why I'm always sad, "
        "but the universe keeps reminding me "
        "that I’m just a commuter in a veh‑outice."
    )
    # Split quote into lines (simple wrap)
    wrap_width = 60
    lines = []
    words = quote.split()
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 <= wrap_width:
            cur += (" " if cur else "") + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)

    # Title
    title = f"{BOLD}{MAGENTA}Woody‑Waddle Wisdom{RESET}"
    print(title.center(80))
    print()

    # Animated typewriter inside the box
    box_lines = [f"{ITALIC}{GRAY}{l}{RESET}" for l in lines]
    draw_box(box_lines, color1=BLUE, color2=GREEN)

    print()
    typewriter(
        "— Woody Allen (philosophically, neurotically, forever avoiding death) ",
        delay=0.05,
        color=YELLOW
    )

if __name__ == "__main__":
    main()