"""
Campbell's Soup Can #5026
Produced: 2026-09-26 07:43:01
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# A Woody Allen‑style existential quip
quote = "The universe is a bad joke, and I'm the only one who didn't get the punchline."

def type_out(text, delay=0.05):
    """Print text one character at a time, like a typewriter."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Draw a fancy border, then the quote, then close the border
print(CYAN + "+" + "-" * 60 + "+" + RESET)
type_out(BOLD + YELLOW + quote + RESET)
print(CYAN + "+" + "-" * 60 + "+" + RESET)