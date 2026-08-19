"""
Campbell's Soup Can #4692
Produced: 2026-08-19 07:54:02
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

# ANSI color codes (foreground)
COLORS = [
    31,  # red
    32,  # green
    33,  # yellow
    34,  # blue
    35,  # magenta
    36,  # cyan
    90,  # bright black (gray)
    91,  # bright red
    92,  # bright green
    93,  # bright yellow
    94,  # bright blue
    95,  # bright magenta
    96,  # bright cyan
]

def colorize(text, code):
    """Wrap text with ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def main():
    quote = "I'm not afraid of the void; I'm just terrified it has Wi‑Fi."
    # Simple border
    border = "═" * (len(quote) + 4)

    # Print top border in cyan
    print(colorize(border, 36))
    print()  # space

    # Typing effect with random colors
    for ch in quote:
        sys.stdout.write(colorize(ch, random.choice(COLORS)))
        sys.stdout.flush()
        time.sleep(0.04)  # tweak speed for feel

    print()  # newline after quote
    print()  # space

    # Bottom border in cyan
    print(colorize(border, 36))

    # Optional tiny Woody‑Allen‑style doodle
    doodle = r"""
      _____
     /     \   (I think, therefore I am... late for therapy)
    | o o |  
     > ^ <   
    """
    print(colorize(doodle, 33))

if __name__ == "__main__":
    main()