"""
Campbell's Soup Can #3190
Produced: 2026-04-08 09:19:16
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
A tiny, self‑contained script that prints a single, neurotic‑like Woody Allen
quote with a splash of color and a tiny “typing” animation.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is to find a good excuse "
    "for why we keep messing it all up.  And maybe, just maybe, "
    "to enjoy the anxiety while we’re at it."
)

# ANSI colour palette
FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
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
STYLE = {
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "reset": "\033[0m",
}

# Choose a random colour for each line (cycling through a fixed list)
LINE_COLORS = itertools.cycle([
    FG["magenta"], FG["cyan"], FG["yellow"], FG["green"], FG["blue"]
])

# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def slow_print(text: str, delay: float = 0.02) -> None:
    """Print `text` one character at a time, creating a typing effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def boxed(text: str) -> str:
    """Wrap `text` in a simple ASCII box."""
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    top_bottom = "┌" + "─" * (width + 2) + "┐"
    bottom = "└" + "─" * (width + 2) + "┘"
    boxed_lines = [top_bottom]
    for line in lines:
        padded = line + " " * (width - len(line))
        boxed_lines.append(f"│ {padded} │")
    boxed_lines.append(bottom)
    return "\n".join(boxed_lines)


def colorize_box(box: str) -> str:
    """Apply a cycling colour to each line of the box."""
    colored = []
    for line, col in zip(box.split("\n"), LINE_COLORS):
        colored.append(col + line + STYLE["reset"])
    return "\n".join(colored)


# ----------------------------------------------------------------------
# Main execution
# ----------------------------------------------------------------------
def main() -> None:
    # Create the ASCII art box
    ascii_art = (
        "   ____        _    _                 _ \n"
        "  / __ \\__  __| |  | | ___  ___  ___ | |\n"
        " / / _` \\ \\/ /| |  | |/ _ \\/ __|/ _ \\| |\n"
        "| | (_| |>  < | |__| |  __/\\__ \\ (_) | |\n"
        " \\ \\__,_/_/\\_\\ \\____/ \\___||___/\\___/|_|\n"
        "  \\____/                                 "
    )
    # Colour the art in a bright cyan
    colored_art = FG["cyan"] + ascii_art + STYLE["reset"]

    # Print the art
    print(colored_art)
    print()

    # Build the box with the quote
    quote_box = boxed(QUOTE)
    colored_box = colorize_box(quote_box)

    # Type‑out the box slowly for drama
    for line in colored_box.split("\n"):
        slow_print(line, delay=0.015)

    # End with a playful wink
    print(FG["yellow"] + STYLE["bold"] + "  ;) " + STYLE["reset"])


if __name__ == "__main__":
    main()