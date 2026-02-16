"""
Campbell's Soup Can #2256
Produced: 2026-02-16 10:11:57
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
CYAN   = '\033[96m'
YELLOW = '\033[93m'
MAGENTA= '\033[95m'
RESET  = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

def slow_print(s, color='', delay=0.03):
    """Print each character with a small pause for a typing effect."""
    for ch in s:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_boxed(txt):
    """Print the quote inside a colored ASCII box."""
    border = '+' + '-'*(len(txt)+2) + '+'
    top    = '| ' + txt + ' |'
    mid    = '| ' + '-'*(len(txt)) + ' |'

    print(YELLOW + border + RESET)
    print(YELLOW + top    + RESET)
    print(YELLOW + mid    + RESET)
    print(YELLOW + border + RESET)
    slow_print(MAGENTA + " — Woody Allen (ish)" + RESET, delay=0.02)

print_boxed(quote)