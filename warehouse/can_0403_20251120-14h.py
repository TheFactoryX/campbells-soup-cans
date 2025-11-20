"""
Campbell's Soup Can #403
Produced: 2025-11-20 14:35:08
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random

# ANSI color codes for vivid output
COLORS = [
    '\033[91m',  # Bright Red
    '\033[92m',  # Bright Green
    '\033[93m',  # Bright Yellow
    '\033[94m',  # Bright Blue
    '\033[95m',  # Bright Magenta
    '\033[96m',  # Bright Cyan
]
RESET = '\033[0m'
BOLD = '\033[1m'

def colored_print(text, delay=0.05):
    """Print `text` one character at a time, each with a random color."""
    for ch in text:
        if ch == ' ':
            # Whitespace stays the default colour
            sys.stdout.write(ch)
        else:
            color = random.choice(COLORS)
            sys.stdout.write(f'{color}{ch}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)

def main():
    quote_lines = [
        "I wonder why I keep fearing my own reflection…",
        "It would be funny if it weren't the sign I'm losing my mind."
    ]

    # Calculate the width of the box
    max_len = max(len(line) for line in quote_lines)
    box_width = max_len + 4   # 2 spaces padding on each side

    # Top border
    sys.stdout.write(f"{BOLD}┌{'─' * box_width}┐{RESET}\n")

    # Quote lines with animated, colorful characters
    for line in quote_lines:
        padded = line.ljust(max_len)  # right‑justify within the box
        sys.stdout.write(f"│ {'")
        colored_print(padded)
        sys.stdout.write(f" }│\n")
        time.sleep(0.3)  # pause between lines

    # Bottom border
    sys.stdout.write(f"{BOLD}└{'─' * box_width}┘{RESET}\n")

if __name__ == "__main__":
    main()
