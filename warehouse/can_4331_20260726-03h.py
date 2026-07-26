"""
Campbell's Soup Can #4331
Produced: 2026-07-26 03:59:01
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes (bright colors)
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"

# Woody Allen‑style quote
QUOTE = (
    "I don't fear death; I just don't want to be there when it "
    "asks for my Wi‑Fi password."
)

def colorize(text):
    return random.choice(COLORS) + text + RESET

def print_with_delay(text, delay=0.005):
    for ch in text:
        print(colorize(ch), end="", flush=True)
        time.sleep(delta if (delta := delay) else 0)
    print()

def draw_box(lines, width):
    # Top border
    print(colorize("╔" + "═" * (width - 2) + "╗"))
    time.sleep(0.1)
    # Content lines
    for line in lines:
        padded = line.ljust(width - 2)
        print(colorize("║") + padded + colorize("║"), flush=True)
        time.sleep(0.15)
    # Bottom border
    print(colorize("╚" + "═" * (width - 2) + "╝"))

def main():
    # Clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Prepare quote lines (wrap manually for simplicity)
    # We'll split by spaces to fit a max width of 60 chars inside the box
    max_inner = 56
    words = QUOTE.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= max_inner:
            current += (" " if current else "") + w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # Determine box width (including borders)
    inner_width = max(len(line) for line in lines)
    box_width = inner_width + 2  # for left/right borders

    draw_box(lines, box_width)
    # Final newline for clean exit
    print()

if __name__ == "__main__":
    main()