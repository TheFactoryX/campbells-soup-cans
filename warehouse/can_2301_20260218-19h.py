"""
Campbell's Soup Can #2301
Produced: 2026-02-18 19:58:01
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
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
from itertools import cycle

# ANSI escape codes
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_BLUE = "\033[34m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"
ANSI_WHITE = "\033[37m"

# ASCII coffee mug with a nervous smile
ASCII_COFFEE = (
    "   _____      \n"
    "  /     \\    \n"
    "  | O O |    \n"
    "  |  *  |    \n"
    "   \\___/      \n"
    "   /\\   \\    \n"
    "  /  \\   \\   \n"
)

# Woody Allen‑style existential quote
WALLACE_QUOTE = """Life is full of misery, loneliness, and suffering — and it's all over much too soon.
I keep procrastinating death because the paperwork involves too many existential questions.
My therapist says I'm overstimulated, but honestly the noise of my thoughts is louder than the city."""

def typewriter(text: str, delay: float = 0.03):
    """Print `text` character by character, giving a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

if __name__ == "__main__":
    # Title
    print(ANSI_BOLD + ANSI_YELLOW + "Woody Allen's Existential Café".center(50) + ANSI_RESET)

    # ASCII coffee art
    print(ANSI_BOLD + ANSI_RED + ASCII_COFFEE + ANSI_RESET)

    # Colorful bracket for the quote
    bracket_cycle = cycle([ANSI_YELLOW + "[", ANSI_YELLOW + "]"])
    line_color_cycle = cycle([ANSI_RED, ANSI_GREEN, ANSI_BLUE,
                             ANSI_MAGENTA, ANSI_CYAN, ANSI_WHITE])

    bracket = next(bracket_cycle)
    sys.stdout.write(bracket + " ")
    sys.stdout.flush()
    sys.stdout.write(ANSI_RESET)

    # Quote lines
    quote_lines = WALLACE_QUOTE.splitlines()
    delay = 0.025
    for line in quote_lines:
        line = line.rstrip()
        if not line:
            continue
        line_color = ANSI_BOLD + next(line_color_cycle)
        for ch in line:
            sys.stdout.write(line_color + ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(ANSI_RESET + "\n")

    # Closing flourish
    print("\n" + ANSI_BOLD + ANSI_CYAN +
          "\n☕️  \"If you're not daring enough to stare at your own coffee, you're missing the point.\"".center(60) + ANSI_RESET)