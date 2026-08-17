"""
Campbell's Soup Can #4650
Produced: 2026-08-17 11:41:09
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

def slow_print(text, delay=0.07):
    """Print each character with a small delay for a dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # ANSI escape codes for colors and styles
    BOLD = "\033[1m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # Woody‑Allen‑style philosophical quote
    quote = f'{BOLD}{YELLOW}"I\'m not afraid of death; I just don\'t want to be the one answering the phone when it happens."{RESET}'

    # Decorative ASCII art box
    top = f"{GREEN}╔════════════════════════════════════════════════════════════╗{RESET}"
    middle = f"{GREEN}║{RESET} {CYAN}{quote}{CYAN} {GREEN}║{RESET}"
    bottom = f"{GREEN}╚════════════════════════════════════════════════════════════╝{RESET}"

    # Print with a little "type‑writer" flair
    print()  # blank line before the show
    slow_print(top)
    slow_print(middle)
    slow_print(bottom)
    print()  # blank line after

    # A cheeky attribution (pretending it's from Woody)
    author = f"{BOLD}{YELLOW}— Woody Allen (sort of){RESET}"
    slow_print(author)

if __name__ == "__main__":
    main()