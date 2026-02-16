"""
Campbell's Soup Can #2254
Produced: 2026-02-16 07:20:01
Worker: Aurora Alpha (openrouter/aurora-alpha)
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

# ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

# Woody‑Allen‑style quote
quote = "I think, therefore I'm terrified of the universe."

# Build a simple boxed layout
def build_box(text: str) -> list[str]:
    # Padding on each side of the text
    pad = 4
    # Width of the inner area (including padding)
    inner_width = max(len(text) + pad, 30)
    # Top / bottom border
    top    = f"┌{'─' * inner_width}┐"
    bottom = f"└{'─' * inner_width}┘"
    # Empty line inside the box
    empty  = f"│{' ' * inner_width}│"
    # Centered text line
    text_line = f"│{' ' * (pad // 2)}{text}{' ' * (inner_width - len(text) - (pad // 2))}│"
    return [top, empty, text_line, empty, bottom]

# Type‑writer effect for a single line
def print_line(line: str, color: str = "", delay: float = 0.02) -> None:
    sys.stdout.write(color)
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()

def main() -> None:
    box = build_box(quote)

    # Animate the box line by line (cyan border, yellow text)
    for i, line in enumerate(box):
        # Use yellow for the line that contains the quote
        if i == 2:
            print_line(line, YELLOW)
        else:
            print_line(line, CYAN)

    # Author line, a little pause after the box
    time.sleep(0.5)
    author = " – Woody Allen"
    print_line(author, MAGENTA, delay=0.05)

if __name__ == "__main__":
    main()