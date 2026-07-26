"""
Campbell's Soup Can #4336
Produced: 2026-07-26 15:29:12
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def slow_print(text, color="", delay=0.04):
    """Print characters one by one for a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    # Move to next line after finishing this line
    print()

def main():
    # Build the ASCII box with Woody‑Allen‑style quote
    top = f"{YELLOW}╔════════════════════════════════════════════════════════╗{RESET}"
    middle = f"{YELLOW}║{CYAN}   {BOLD}\"I'm not afraid of death; I just don't want to be invited to dinner alone.\"{RESET}   {YELLOW}║{RESET}"
    bottom = f"{YELLOW}╚════════════════════════════════════════════════════════╝{RESET}"

    # Animate the box appearing
    slow_print(top)
    slow_print(middle)
    slow_print(bottom)

if __name__ == "__main__":
    main()