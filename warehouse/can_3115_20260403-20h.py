"""
Campbell's Soup Can #3115
Produced: 2026-04-03 20:53:40
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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
CYAN = "\033[96m"
YELLOW = "\033[93m"

def typewriter(s, delay=0.05):
    """Print string s character by character without adding a newline."""
    for ch in s:
        print(ch, end="", flush=True)
        time.sleep(delay)

def main():
    quote = "I'm not afraid of death; I just don't want to be the one who has to explain it to the afterlife tech support."
    inner_width = len(quote) + 2  # accounts for the spaces inside the box
    horiz = "═" * inner_width

    # Top border
    print(f"{BOLD}{CYAN}╔{horiz}╗{RESET}")
    # Left border + quote (typewriter effect) + right border
    print(f"{BOLD}{CYAN}║ {RESET}", end="")
    typewriter(quote, 0.07)
    print(f"{BOLD}{CYAN} ║{RESET}")
    # Bottom border
    print(f"{BOLD}{CYAN}╚{horiz}╝{RESET}")

if __name__ == "__main__":
    main()