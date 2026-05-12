"""
Campbell's Soup Can #3652
Produced: 2026-05-12 04:05:58
Worker: Free Models Router (openrouter/free)
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

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"

def type_char(ch, color):
    """Print a single character with the given color and flush immediately."""
    sys.stdout.write(color + ch + RESET)
    sys.stdout.flush()

def main():
    # Clear the terminal (works on most Unix-like terminals)
    sys.stdout.write("\033[2J\033[H")

    # ASCII art: a little Woody with a thought bubble
    art = """
        .-------.
       /         \\
      |  ( o o )  |
       \\   ^   /
        '-----'
   [ ??? ]"""
    sys.stdout.write(CYAN + art + RESET + "\n")

    # The quote – Woody Allen style
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Type the quote letter‑by‑letter with a warm yellow glow
    for ch in quote:
        type_char(ch, BOLD + YELLOW)
        time.sleep(0.03)   # typewriter speed

    sys.stdout.write("\n")   # line break after the quote

    # Signature – a humble Woody Allen sign‑off
    sys.stdout.write(RED + "— Woody Allen" + RESET + "\n")

    # Small pause so the user can read it
    time.sleep(1)

if __name__ == "__main__":
    main()