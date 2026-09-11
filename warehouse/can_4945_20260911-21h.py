"""
Campbell's Soup Can #4945
Produced: 2026-09-11 21:43:26
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def type_out(text, delay=0.05):
    """Print text character by character with a delay for a typing effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Build the ASCII art with colors
    top = CYAN + "╔═════════════════════════════════════════════════════════╗" + RESET
    bottom = CYAN + "╚═════════════════════════════════════════════════════════╝" + RESET

    # The quote in Woody Allen's style
    quote = YELLOW + "\"Life is a tragedy for those who think too much, but a comedy for those who don't notice they're the punchline.\"" + RESET

    middle = CYAN + "║  " + quote + "  ║" + RESET

    # Print top line with effect
    type_out(top + "\n")
    # Print middle line with effect
    type_out(middle + "\n")
    # Print bottom line with effect
    type_out(bottom + "\n")

if __name__ == "__main__":
    main()