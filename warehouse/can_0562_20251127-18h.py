"""
Campbell's Soup Can #562
Produced: 2025-11-27 18:42:30
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes for color and style
RESET = '\033[0m'
BOLD = '\033[1m'
FG_CYAN = '\033[36m'
FG_MAGENTA = '\033[35m'
FG_RED = '\033[31m'
FG_YELLOW = '\033[33m'

def main():
    # The Woody‑Allen‑style quote
    quote = (
        "I have learned that existence is a cosmic joke, "
        "and I'm just the punchline trying to outwit existential ennui."
    )

    # Visual header
    header = f"{FG_MAGENTA}{BOLD}╭─────── Woody Allen's Existential Cringe ───────╮{RESET}"
    print(header)

    # Fun little ASCII face
    face = f"{FG_RED}¯\\_(ツ)_/¯{RESET}"
    print(face)

    # Prepare the box dimensions
    box_width = len(quote) + 4  # Padding for borders
    top_bottom = FG_YELLOW + "=" * box_width + RESET
    side_border = FG_YELLOW + '|' + RESET

    # Print the top border
    print(top_bottom)

    # Print the quote with a typing animation inside the box
    sys.stdout.write(f"{side_border} ")
    sys.stdout.flush()
    for ch in quote:
        sys.stdout.write(FG_CYAN + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.04)  # Typing speed

    # Close the box line
    sys.stdout.write(" " + side_border + "\n")
    sys.stdout.flush()

    # Print the bottom border
    print(top_bottom)

if __name__ == "__main__":
    main()
