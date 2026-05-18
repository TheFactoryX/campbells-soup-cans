"""
Campbell's Soup Can #3718
Produced: 2026-05-18 04:42:03
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
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
import itertools

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
FG_CYAN = "\033[36m"
FG_YELLOW = "\033[33m"
FG_MAGENTA = "\033[35m"
FG_GREEN = "\033[32m"

# The Woody‑Allen‑style quote
QUOTE = (
    "I have a deep, existential dread that I’m "
    "just a nervous nervous‑breakdown waiting to "
    "happen—"
    "and the worst part is, I’m really good at "
    "anticipating it."
)

# Fancy border characters
TL, TR, BL, BR, H, V = "╔", "╗", "╚", "╝", "═", "║"

def colourize(text, colour):
    return f"{colour}{text}{RESET}"

def typewriter(text, delay=0.03):
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def animated_border(width, height, colour):
    """Yield lines that draw a box with a moving “glitch” line."""
    top = colourize(TL + H * width + TR, colour)
    bottom = colourize(BL + H * width + BR, colour)
    middle_template = colourize(V + " " * width + V, colour)

    # Create a simple moving dash on the left side
    dash_positions = itertools.cycle(range(height))
    for line_no in range(height):
        line = list(middle_template)
        # Replace one space with a dash to simulate motion
        dash_idx = 1 + next(dash_positions) % width
        line[dash_idx] = colourize("─", FG_MAGENTA)
        yield top if line_no == 0 else bottom if line_no == height - 1 else "".join(line)

def main():
    # Determine box size based on quote length
    lines = []
    max_len = 0
    for raw in QUOTE.split():
        if not lines or len(lines[-1]) + len(raw) + 1 > 60:
            lines.append(raw)
        else:
            lines[-1] += " " + raw
    # Pad lines to the same width
    max_len = max(len(l) for l in lines)
    padded = [l.ljust(max_len) for l in lines]

    box_width = max_len
    box_height = len(padded) + 2  # top & bottom borders

    # Print animated border while “typing” the quote
    border_gen = animated_border(box_width, box_height, FG_CYAN)
    for i in range(box_height):
        line = next(border_gen)
        if i == 1:  # top border already printed
            print(line)
        elif 1 < i < box_height - 1:
            # interior line with text
            text_line = padded[i - 2]
            interior = colourize(V, FG_CYAN) + " " + colourize(text_line, FG_YELLOW) + " " + colourize(V, FG_CYAN)
            print(interior)
        else:
            print(line)

    # Add a small pause then re‑print the quote with typewriter effect
    time.sleep(0.7)
    print()
    typewriter(colourize(QUOTE, FG_GREEN))

if __name__ == "__main__":
    main()