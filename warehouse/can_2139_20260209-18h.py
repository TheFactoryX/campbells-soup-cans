"""
Campbell's Soup Can #2139
Produced: 2026-02-09 18:05:40
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
GREEN   = "\033[32m"
BLUE    = "\033[34m"

# Woody‑Allen‑style quote
QUOTE = "I think I'm allergic to success; my nervous system just can't handle the applause."

# Cycle through a few colors for a jazzy typing effect
COLOR_CYCLE = [YELLOW, MAGENTA, GREEN, BLUE]

def colorful_type(text: str, delay: float = 0.04) -> None:
    """Print `text` one character at a time, cycling through colors."""
    for i, ch in enumerate(text):
        color = COLOR_CYCLE[i % len(COLOR_CYCLE)]
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def print_boxed(text: str) -> None:
    """Print `text` inside a cyan ASCII box, with a lively typing animation."""
    width = len(text) + 2          # padding on each side
    top    = f"{CYAN}┌{'─' * width}┐{RESET}"
    middle = f"{CYAN}│ {RESET}"
    bottom = f"{CYAN}└{'─' * width}┘{RESET}"

    sys.stdout.write(top + "\n")
    sys.stdout.write(middle)
    colorful_type(text)
    sys.stdout.write(f"{CYAN} │{RESET}\n")
    sys.stdout.write(bottom + "\n")

def main() -> None:
    # A little pause before the show begins
    time.sleep(0.5)
    print_boxed(QUOTE)

if __name__ == "__main__":
    main()