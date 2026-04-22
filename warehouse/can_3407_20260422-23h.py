"""
Campbell's Soup Can #3407
Produced: 2026-04-22 23:06:49
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
import shutil
import random

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# 7‑color palette (can be expanded)
COLORS = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;118m",  # green
    "\033[38;5;39m",   # blue
    "\033[38;5;93m",   # magenta
    "\033[38;5;129m",  # cyan
]

# Quote in Woody Allen style
QUOTE = (
    "I keep stressing that my favorite philosophical idea is "
    "that the universe is a gigantic comedy club, and we’re "
    "the clowns who keep forgetting the punchlines."
)

# Box parameters
PADDING = 2
HORIZONTAL = "─"
VERTICAL = "│"
DIAGONAL_TL = "┌"
DIAGONAL_TR = "┐"
DIAGONAL_BL = "└"
DIAGONAL_BR = "┘"

# Sleep time for animation (typewriter effect)
DELAY = 0.04

def typewriter(text: str, color_func=None):
    """Print text one character at a time, optionally with a color function."""
    for ch in text:
        if color_func:
            sys.stdout.write(color_func() + ch + RESET)
        else:
            sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(DELAY)
    sys.stdout.write('\n' + RESET)
    sys.stdout.flush()

def random_color():
    return random.choice(COLORS)

def draw_box(lines):
    """Draw a colored box around the given lines."""
    term_width, _ = shutil.get_terminal_size((80, 20))
    max_len = max(len(line) for line in lines)
    box_width = max_len + 2 * PADDING + 2  # borders

    # Ensure the box fits the terminal width; if not, truncate
    if box_width > term_width:
        for i, line in enumerate(lines):
            if len(line) > term_width - 4:
                lines[i] = line[:term_width - 6] + "…"

    # top border
    sys.stdout.write(DIAGONAL_TL + HORIZONTAL * (box_width - 2) + DIAGONAL_TR + "\n")

    # box content
    for line in lines:
        padded = " " * PADDING + line.ljust(box_width - 2 * PADDING - 2) + " " * PADDING
        sys.stdout.write(v_color() + VERTICAL + padded + VERTICAL + RESET + "\n")

    # bottom border
    sys.stdout.write(DIAGONAL_BL + HORIZONTAL * (box_width - 2) + DIAGONAL_BR + "\n")

def v_color():
    """Randomly choose a color for vertical borders."""
    return random.choice(COLORS)

def main():
    """Main function to display the quote in an animated, colorful box."""
    # Split the quote into words to wrap lines nicely
    words = QUOTE.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= 60:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)

    # Draw the box
    draw_box(lines)

    # Give a short pause before revealing the quote line by line
    time.sleep(0.5)
    for line in lines:
        typewriter(line, color_func=random_color)
        time.sleep(0.2)

if __name__ == "__main__":
    main()