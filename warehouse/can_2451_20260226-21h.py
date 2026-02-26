"""
Campbell's Soup Can #2451
Produced: 2026-02-26 21:47:13
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys, random

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Woody Allen‑style quote (single line)
QUOTE = "I'm not afraid of death — I just don't want to be there when it happens."

# Simple ASCII art representing a cerebral figure (no external assets)
ASCII = r"""
  ____ 
 / ___ \
| /   \ |
 \____/ 
 / WW \
"""

def print_ascii():
    """Print the ASCII art intro."""
    print(ASCII)

def flash_top_border(count=3, width=48):
    """Flash the top border in random colors for visual flair."""
    left = "│"
    right = "│"
    border = "┌" + "─" * width + "┐"
    for _ in range(count):
        col = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
        print(f"{col}{border}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)

def animate_words():
    """Print the quote word‑by‑word, each in a random color."""
    words = QUOTE.split()
    # Determine a width that fits the longest word comfortably
    max_word_len = max(len(w) for w in words) if words else 0
    width = max_word_len + 8
    left = "│"
    right = "│"
    border_top = "┌" + "─" * width + "┐"
    border_bot = "└" + "─" * width + "┘"
    print(border_top)
    for w in words:
        col = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
        pad_len = max(0, width - len(w) - 2)
        pad = " " * pad_len
        print(f"{col}{left}{pad}{w}{pad}{right}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print(border_bot)

def draw_box(text):
    """Print the quote inside a colorful static box."""
    width = 48
    left = "│"
    right = "│"
    border_top = "┌" + "─" * width + "┐"
    border_bot = "└" + "─" * width + "┘"
    pad_len = max(0, width - len(text) - 2)
    pad = " " * pad_len
    print(border_top)
    print(left + pad + text + pad + right)
    # Three empty interior lines
    for _ in range(3):
        print(left + " " * width + right)
    print(border_bot)

def main():
    print_ascii()
    flash_top_border()        # quick colorful border flash
    animate_words()          # word‑by‑word colored reveal
    draw_box(QUOTE)          # final nicely‑boxed quote

if __name__ == "__main__":
    main()