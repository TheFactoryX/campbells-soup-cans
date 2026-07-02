"""
Campbell's Soup Can #4068
Produced: 2026-07-02 06:09:45
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
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
import os

# ANSI colour codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
BLACK_BG= "\033[40m"

# The Woody‑Allen‑style philosophical quote:
quote = (
    "I find that every moment a manic rehearsal for the universe's big "
    "premiere, and I'm terrified that the final scene will be that I "
    "realise I have no one to laugh with."
)

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_bubble(text, delay=0.03):
    """Print an ASCII art speech bubble containing the given text,
    animating one character at a time."""
    padding = 4
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + padding * 2

    # Top border
    top = f"{CYAN}┌{'─' * width}┐{RESET}\n"
    # Compose middle lines with padding and vertical borders
    middle = ""
    for line in lines:
        padded = line.ljust(max_len)
        middle += f"{CYAN}│{' ' * padding}{YELLOW}{padded}{CYAN}{' ' * padding}│{RESET}\n"

    # Bottom border
    bottom = f"{CYAN}└{'─' * width}┘{RESET}\n"

    bubble = top + middle + bottom

    # Print bubble character by character
    for ch in bubble:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != '\n':
            time.sleep(delay)

def main():
    clear_screen()
    print_bubble(quote)
    # pause before exit
    time.sleep(1.5)

if __name__ == "__main__":
    main()