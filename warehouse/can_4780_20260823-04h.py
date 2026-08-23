"""
Campbell's Soup Can #4780
Produced: 2026-08-23 04:04:22
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def main():
    # ANSI color codes
    cyan  = "\033[96m"
    yellow = "\033[93m"
    green = "\033[92m"
    reset = "\033[0m"

    # Box dimensions
    width = 70
    top_bottom = cyan + "+" + "-" * width + "+" + reset
    side = cyan + "|" + reset

    # Print the top border
    print(top_bottom)

    # Quote (split for visual comfort)
    line1 = "I’m not afraid of death; I just don’t want to be"
    line2 = "there when it happens – the ultimate inconvenience."

    # Print the framed quote
    print(side + " " + green + "   _______   " + reset)
    print(side + " " + yellow + line1 + reset)
    print(side + " " + yellow + line2 + reset)
    print(side + " " + green + "   (___)   " + reset)   # tiny ASCII face
    print(side + " " + cyan + "   (___)   " + reset)

    # Print the bottom border
    print(top_bottom)

if __name__ == "__main__":
    main()