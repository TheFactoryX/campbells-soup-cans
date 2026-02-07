"""
Campbell's Soup Can #2099
Produced: 2026-02-07 14:45:33
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
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
BOLD   = '\033[1m'
RESET  = '\033[0m'

# Classic Woody Allen neurotic quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

def colored(text, *colors):
    """Wrap text in the given ANSI color codes and reset at the end."""
    return ''.join(colors) + text + RESET

def typewriter(txt, delay=0.03):
    """Print text character‑by‑character with a tiny delay (typing effect)."""
    for ch in txt:
        sys.stdout.write(colored(ch, CYAN, BOLD))
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET, end='')

# Box dimensions
w = 70

# Decorative frame
border = colored('+' + '-'*(w-2) + '+', BLUE, BOLD)
top    = f"| {colored(quote, MAGENTA, BOLD)} |"
separator = '|' + '-'*(w-2) + '|'
punch  = " (Actually, I was kidding. Let’s order ice‑cream.)"

print(border)
print(top)
print(separator)
print(colored(' — a neurotic philosopher who’d rather have dessert ', CYAN, BOLD))
print(separator)
print(border)

# Animate the punchline
typewriter(punch)