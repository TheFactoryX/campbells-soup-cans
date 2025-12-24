"""
Campbell's Soup Can #1156
Produced: 2025-12-24 21:30:39
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
import random

# ANSI escape codes for bright colors
BRIGHT_COLORS = [91, 92, 93, 94, 95, 96]
RESET = "\033[0m"

# The Woody‑Allen‑style quote (one line)
QUOTE = ("Life is a series of awkward moments; I wish I could just press the pause button "
         "on my existential crisis.")

# Build a simple box around the quote
box_width = len(QUOTE) + 2  # Padding of 1 space on each side
top_border = f"┌{'─' * box_width}┐"
bottom_border = f"└{'─' * box_width}┘"
empty_line = f"│{' ' * box_width}│"

def colored_char(ch):
    """Return the character wrapped in a random bright ANSI color."""
    color = random.choice(BRIGHT_COLORS)
    return f"\033[{color}m{ch}{RESET}"

def animate_box():
    """Print the box and animate the quote inside."""
    # Print the top border
    print(top_border)
    # Print an empty line (could animate if desired)
    print(empty_line)
    # Animate the quote line
    sys.stdout.write("│")
    for ch in QUOTE:
        sys.stdout.write(colored_char(ch))
        sys.stdout.flush()
        time.sleep(0.03)  # Short delay for animation effect
    sys.stdout.write("│\n")
    # Print an empty line for spacing
    print(empty_line)
    # Print the bottom border
    print(bottom_border)

def main():
    # Clear the screen for a cleaner output (optional)
    print("\033[2J\033[H", end="")  # ANSI clear screen and home cursor
    # Add a little header
    header = "┌───────────────────────┐\n"
    header += "│   Woody Allen’s Box   │\n"
    header += "└───────────────────────┘\n"
    print(header)
    animate_box()
    # A final playful note
    note = ("\nPress Ctrl+C to stop the existential crisis.\n"
            "Or just keep scrolling. Have a good laugh!")
    sys.stdout.write(f"\033[92m{note}{RESET}\n")  # Green note

if __name__ == "__main__":
    main()