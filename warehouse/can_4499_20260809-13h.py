"""
Campbell's Soup Can #4499
Produced: 2026-08-09 13:15:14
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # ANSI color codes
    RED   = "\033[31m"
    YELLOW= "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    # A nervous little face
    face = [
        "   _____   ",
        "  /     \\  ",
        " |  o o  | ",
        " |  >_<  | ",
        "  \\_____/  "
    ]

    # The Woody Allen‑style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens - the ultimate punchline to a joke I never got to finish."

    # Box dimensions
    width = 58          # inner width (between the '|')
    border = RED + "+" + "-" * width + "+" + RESET
    top    = RED + "|" + " " * width + "|" + RESET

    lines = []
    lines.append(border)
    lines.append(top)

    # Print the face centered inside the box
    for f in face:
        padded = f.center(width)
        lines.append(RED + "|" + padded + "|" + RESET)

    # Wrap the quote to fit the box
    max_quote_width = width - 2   # account for the two '|' characters
    words = quote.split()
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= max_quote_width:
            current = (" " + w) if current else w
        else:
            lines.append(YELLOW + "|" + current.center(width) + "|" + RESET)
            current = w
    if current:
        lines.append(YELLOW + "|" + current.center(width) + "|" + RESET)

    lines.append(border)

    # Output
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()