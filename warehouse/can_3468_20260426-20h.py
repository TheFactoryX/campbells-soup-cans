"""
Campbell's Soup Can #3468
Produced: 2026-04-26 20:57:34
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
A tiny, colorful, animated console quote in the neurotic style of Woody Allen.
Run this script directly – no external libraries required.
"""

import sys
import time
import itertools

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

FG_COLORS = [
    "\033[31m",  # red
    "\033[33m",  # yellow
    "\033[32m",  # green
    "\033[36m",  # cyan
    "\033[34m",  # blue
    "\033[35m",  # magenta
]

# The quote – one line, Woody‑Allen‑ish
QUOTE = (
    "I’m not scared of death; I’m just terrified that "
    "it will show up late and ruin my deadline."
)

# A simple box drawing function
def boxed(text: str) -> str:
    """Return the text inside a simple ASCII art box."""
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    top = "╔" + "═" * (width + 2) + "╗"
    bottom = "╚" + "═" * (width + 2) + "╝"
    middle = "\n".join(f"║ {line.ljust(width)} ║" for line in lines)
    return f"{top}\n{middle}\n{bottom}"

# Animated typewriter effect with rainbow colors
def typewriter(text: str, delay: float = 0.04):
    """Print `text` one character at a time, cycling through colors."""
    color_cycle = itertools.cycle(FG_COLORS)
    for ch in text:
        sys.stdout.write(next(color_cycle) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main() -> None:
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    # Print a fancy title
    title = f"{BOLD}{DIM}~*~*~ {RESET}{BOLD}Woody‑Allen Philosophy{RESET}{DIM} ~*~*~{RESET}"
    print(title.center(80))
    print()
    # Print the quote inside a box, colored line by line
    boxed_quote = boxed(QUOTE)
    for line in boxed_quote.split("\n"):
        # each line gets a different foreground color
        color = next(itertools.cycle(FG_COLORS))
        sys.stdout.write(color + line + RESET + "\n")
        time.sleep(0.2)
    print()
    # Finally, animate the quote in typewriter style
    typewriter(QUOTE, delay=0.03)

if __name__ == "__main__":
    main()