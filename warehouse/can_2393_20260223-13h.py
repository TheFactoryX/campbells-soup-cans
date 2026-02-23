"""
Campbell's Soup Can #2393
Produced: 2026-02-23 13:41:27
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
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
import random

# ANSI foreground color palette (reset ends the sequence)
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

def c(text, name):
    """Wrap text with ANSI escape codes for a given colour."""
    return f"{COLORS[name]}{text}{COLORS['reset']}"

def cc(char, name):
    """Return a single coloured character."""
    return f"{COLORS[name]}{char}{COLORS['reset']}"

def print_box():
    """ASCII box with each line coloured randomly (last line stays white)."""
    ascii_art = [
        "┌─────────────────────────────┐",
        "│   🎭 WOODY ALLEN QUOTES   │",
        "│ (One‑liner, neurotic‑proof) │",
        "│   =====================   │",
        "│   'I’m neurotic enough …' │",
        "└─────────────────────────────┘"
    ]
    for line in ascii_art:
        # colour each line except the final border
        colour = random.choice(list(COLORS.keys())) if line != ascii_art[-1] else "white"
        print(c(line, colour))

def clear_terminal():
    """Clear screen (works on Windows & Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(chars, delay=0.012):
    """Print each character of `chars` one‑by‑one with a small delay."""
    for ch in chars:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    clear_terminal()
    print_box()

    # Woody Allen‑style existential joke (single line)
    woody_quote = (
        "I'm neurotic enough to ask my therapist, \"Why am I here?\" "
        "and he replies, \"Because you're asking that.\""
    )
    # Random colour for every character
    coloured_chars = [cc(ch, random.choice(list(COLORS.keys()))) for ch in woody_quote]

    print("\nQuote starts typing…")
    time.sleep(0.3)          # brief pause before the “typewriter” begins
    typewriter(coloured_chars, delay=0.02)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[STOP] Thanks for listening!")