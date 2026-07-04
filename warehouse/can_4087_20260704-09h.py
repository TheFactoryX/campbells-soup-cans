"""
Campbell's Soup Can #4087
Produced: 2026-07-04 09:32:00
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

# ANSI escape sequences for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
FADE = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

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


def typewriter(text: str, delay: float = 0.04):
    """Print text character‑by‑character, like a typewriter."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def colorful_box(quote: str):
    """Wrap the quote in a rainbow‑colored box."""
    lines = quote.split("\n")
    width = max(len(line) for line in lines) + 4  # padding

    # Create a rotating color cycle for the borders
    border_colors = itertools.cycle([FG["red"], FG["yellow"], FG["green"],
                                     FG["cyan"], FG["blue"], FG["magenta"]])

    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"

    # Print top border with animated colors
    for segment in top_border:
        sys.stdout.write(next(border_colors) + segment + RESET)
    sys.stdout.write("\n")

    # Print each line padded, also colored
    for line in lines:
        padded = f"  {line.ljust(width - 4)}  "
        line_color = next(border_colors)
        sys.stdout.write(line_color + "║" + RESET)
        sys.stdout.write(FG["white"] + BOLD + padded + RESET)
        sys.stdout.write(line_color + "║" + RESET + "\n")

    # Print bottom border
    for segment in bottom_border:
        sys.stdout.write(next(border_colors) + segment + RESET)
    sys.stdout.write("\n")


def main():
    quote = (
        f"{ITALIC}I'm terrified of eternity, but I'm even more terrified of the silence that follows "
        f"when I finally stop overthinking.{RESET}"
    )
    # First, a brief "loading" animation
    for i in range(3):
        sys.stdout.write(FG["cyan"] + "Loading philosophical insight" + "." * (i + 1) + "\r")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n" + RESET)

    colorful_box(quote)
    # Finally, type out a witty after‑thought
    typewriter(FG["magenta"] + BOLD + "— a neurotic mind at peace... for exactly five seconds." + RESET)


if __name__ == "__main__":
    main()