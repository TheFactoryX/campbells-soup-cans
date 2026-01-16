"""
Campbell's Soup Can #1651
Produced: 2026-01-16 18:49:44
Worker: Mistral: Devstral 2 2512 (free) (mistralai/devstral-2512:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_woody_quote():
    # Woody Allen style quote
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."

    # ASCII art of Woody Allen's glasses
    glasses = r"""
        ________________________________________
       /                                        \
      |   \________________________________/    |
      |    |                                  |    |
      |    |   I'm not afraid of dying;     |    |
      |    |   I just don't want to be     |    |
      |    |   there when it happens.      |    |
      |    |__________________________________|
      |                                          |
       \________________________________________/
            \___________________________/
             |                         |
             |   - Woody Allen         |
             |_________________________|
    """

    # Print the glasses with color
    print_colored(glasses, "33")  # Yellow color

    # Print the quote with a typewriter effect
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

    # Print a funny footer
    footer = "Remember: The key to immortality is first living a life worth remembering... or at least not tripping on the way to the bathroom at night."
    print_colored("\n" + footer, "35")  # Magenta color

if __name__ == "__main__":
    print_woody_quote()