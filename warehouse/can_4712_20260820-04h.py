"""
Campbell's Soup Can #4712
Produced: 2026-08-20 04:53:12
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

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_writer(text: str, delay: float = 0.04, color: str = WHITE):
    """Print text character by character with optional color."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after finished

def print_boxed_quote(quote: str):
    """Print a colorful box around the quote with a typing effect."""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    # Top border
    type_writer("╔" + "═" * (max_len + 4) + "╗", delay=0.01, color=CYAN)
    # Empty line above quote
    type_writer("║" + " " * (max_len + 4) + "║", delay=0.01, color=CYAN)
    # Quote lines
    for line in lines:
        padded = line.ljust(max_len)
        type_writer(f"║  {padded}  ║", delay=0.03, color=YELLOW)
    # Empty line below quote
    type_writer("║" + " " * (max_len + 4) + "║", delay=0.01, color=CYAN)
    # Bottom border
    type_writer("╚" + "═" * (max_len + 4) + "╝", delay=0.01, color=CYAN)

def main():
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Woody Allen‑style philosophical quote (original)
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens.\n"
        "Besides, I always forget where I left my existential dread."
    )

    print_boxed_quote(quote)

    # A tiny neurotic ASCII face for extra flavor
    face = r"""
          _____
        .'     '.
       /  O   O  \
      |    ^     |
      |  '-' '-  |
       \  '__'  /
        '.___.'
    """
    for ch in face:
        sys.stdout.write(MAGENTA + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

if __name__ == "__main__":
    main()