"""
Campbell's Soup Can #3237
Produced: 2026-04-11 11:46:07
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

"""
A one‑liner Woody‑Allen‑style philosophical joke,
displayed with a splash of color and a tiny type‑writer effect.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI escape sequences for colors & styles
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"

FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}
BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}


def slow_type(text: str, delay: float = 0.04, *, end="\n"):
    """Print *text* one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def flashing_border(width: int, height: int, cycles: int = 6):
    """Yield a sequence of frames that flash a colorful border."""
    colors = itertools.cycle([FG["red"], FG["green"], FG["yellow"], FG["blue"], FG["magenta"], FG["cyan"]])
    for _ in range(cycles):
        color = next(colors)
        line = color + "+" + "-" * (width - 2) + "+" + RESET
        middle = color + "|" + " " * (width - 2) + "|" + RESET
        frame = [line] + [middle for _ in range(height - 2)] + [line]
        yield "\n".join(frame)


def clear_screen():
    """Clear the terminal (works on most ANSI terminals)."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def main():
    quote = (
        f"{BOLD}{FG['magenta']}\"I think, therefore I'm neurotic. "
        f"If existence is a comedy, I'm the punchline I never asked for.\"{RESET}"
    )
    width = 70
    height = 7

    # Animate a flashing border around the future quote
    for frame in flashing_border(width, height):
        clear_screen()
        print(frame)
        time.sleep(0.15)

    # Print the quote centered inside the box
    clear_screen()
    top_bottom = FG["cyan"] + "+" + "-" * (width - 2) + "+" + RESET
    empty = FG["cyan"] + "|" + " " * (width - 2) + "|" + RESET
    # Build the box lines
    box_lines = [top_bottom] + [empty for _ in range((height - 3) // 2)]

    # Insert the quote line (centered)
    quote_line = quote.center(width - 2)
    box_lines.append(FG["cyan"] + "|" + quote_line + "|" + RESET)

    # Fill the remainder of the box
    box_lines += [empty for _ in range((height - 3) // 2 + (height - 3) % 2)] + [top_bottom]

    # Render the box
    for line in box_lines:
        print(line)

    # Type‑out a tiny reflection after a pause
    time.sleep(0.8)
    slow_type(f"{FAINT}{FG['yellow']}— maybe that's why I never finish a novel.{RESET}")

    # Keep the screen for a moment before exiting
    time.sleep(2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit on Ctrl‑C
        sys.exit(0)