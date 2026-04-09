"""
Campbell's Soup Can #3210
Produced: 2026-04-09 21:03:54
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote():
    quote = """
    I don't want to achieve immortality through my work; I want to achieve it through not dying.
    """
    author = " - Woody Allen"

    # ANSI escape codes for colors
    colors = {
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "red": "\033[91m",
        "reset": "\033[0m"
    }

    # Print Woody Allen's face with colors
    woody_face = f"""
    {colors['yellow']}
     .-""""-.       {colors['green']}I don't want to achieve immortality through my work;{colors['reset']}
    /        \\      {colors['green']}I want to achieve it through not dying.{colors['reset']}
    |  _  _  |      {colors['blue']} - Woody Allen{colors['reset']}
    | (o)(o) |
    |  \\../  |
    |  '##'  |
    \\        /
     '-....-'{colors['reset']}
    """
    print(woody_face)

    # Animate the quote
    for char in quote:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)
    print(f"\n{colors['blue']}{author}{colors['reset']}")

if __name__ == "__main__":
    print_quote()