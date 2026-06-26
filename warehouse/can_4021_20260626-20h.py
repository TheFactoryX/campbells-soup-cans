"""
Campbell's Soup Can #4021
Produced: 2026-06-26 20:55:14
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

def slow_print_colored(text, color, delay=0.05):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m")

def main():
    quote = (
        "The only thing that separates us from the animals is our ability to procrastinate... "
        "and also our crippling anxiety about the meaning of life."
    )
    colors = [
        "\033[31m",  # red
        "\033[32m",  # green
        "\033[33m",  # yellow
        "\033[34m",  # blue
        "\033[35m",  # magenta
        "\033[36m",  # cyan
        "\033[97m",  # bright white
    ]
    border_color = random.choice(colors)
    quote_color = random.choice(colors)

    width = len(quote) + 2  # two spaces inside the box
    top = "╔" + "═" * width + "╗"
    bottom = "╚" + "═" * width + "╝"
    side = "║"

    # top border
    sys.stdout.write(border_color + top + "\033[0m\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # left side + space
    sys.stdout.write(border_color + side + "\033[0m ")
    sys.stdout.flush()

    # quote with typing effect
    slow_print_colored(quote, quote_color, delay=0.04)

    # right side + newline
    sys.stdout.write(" " + border_color + side + "\033[0m\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # bottom border
    sys.stdout.write(border_color + bottom + "\033[0m\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()