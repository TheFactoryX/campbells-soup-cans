"""
Campbell's Soup Can #4444
Produced: 2026-08-05 21:32:40
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Rainbow colors cycle
RAINBOW = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

def rainbow_print(text, delay=0.02):
    """Print text with a rainbow effect, one character at a time."""
    for i, ch in enumerate(text):
        sys.stdout.write(RAINBOW[i % len(RAINBOW)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(delta)
    print()  # newline after the whole line

# Small Woody Allen‑style ASCII face
woody_face = [
    "   _____",
    "  /     \\",
    " |  o o  |",
    " |   ^   |",
    " |  '-'  |",
    "  \\_____/"
]

# Print the face with a slight delay and rainbow lines
for line in woody_face:
    rainbow_print(line, delay=0.03)

# The philosophical quote in Woody Allen's neurotic style
quote = "Life is a tragedy for those who feel, and a comedy for those who think... unfortunately I do both at once."

# Print the quote with a rainbow typewriter effect
rainbow_print(quote, delay=0.04)

# Final pause so the user can see the output before the script ends (optional)
time.sleep(1)