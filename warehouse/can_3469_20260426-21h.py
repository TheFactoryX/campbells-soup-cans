"""
Campbell's Soup Can #3469
Produced: 2026-04-26 21:54:15
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

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]
RESET = "\033[0m"
BOLD = "\033[1m"

def colorize(text, color):
    return f"{color}{text}{RESET}" if sys.stdout.isatty() else text

def typewriter_effect(text, delay=0.03, color=None):
    for ch in text:
        sys.stdout.write(colorize(ch, color) if color else ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after finished

def print_boxed_quote():
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "If I could live forever, I'd still be late for my own funeral."
    )
    width = len(quote) + 4
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"

    # Pick a random color for the box
    box_color = random.choice(COLORS)

    # Print top border with a little flash
    for _ in range(2):
        sys.stdout.write("\r" + colorize(top_border, box_color) + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r" + " " * len(top_border) + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    print(colorize(top_border, box_color))

    # Print quote with typewriter effect in a contrasting color
    quote_color = random.choice([c for c in COLORS if c != box_color])
    sys.stdout.write(colorize("║ ", box_color))
    typewriter_effect(quote, color=quote_color)
    sys.stdout.write(colorize(" ║", box_color))
    print()  # newline after the quote line

    # Print bottom border with a slight wiggle
    for offset in [-1, 0, 1, 0]:
        sys.stdout.write("\r" + (" " * max(offset, 0)) + colorize(bottom_border, box_color) + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print(colorize(bottom_border, box_color))

    # Add a playful Woody Allen-esque footer
    footer = random.choice([
        "...and that's why I never trust elevators.",
        "...which explains my therapist's hourly rate.",
        "...so I stick to indoor hobbies, like worrying."
    ])
    print(colorize("\n  " + footer, random.choice(COLORS)))

if __name__ == "__main__":
    print_boxed_quote()