"""
Campbell's Soup Can #3521
Produced: 2026-05-01 17:14:01
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

# ANSI colors
RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"

def color(text, code):
    """Wrap text with ANSI color code."""
    return f"{code}m{text}{RESET}"

# Woody Allen style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens… especially when I’m still waiting for the pizza."
border = "*" * 70

# Top border (cyan)
print(color(border, CYAN))

# Left side of the box
sys.stdout.write(color("| ", CYAN), end="")

# Print each character in a rotating rainbow of colors
for i, ch in enumerate(quote):
    sys.stdout.write(color(ch, [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN][i % 6]))

# Right side and newline
sys.stdout.write(color(" |", CYAN))
print()

# Bottom border (cyan)
print(color(border, CYAN))

# The quote itself, displayed in bold magenta for emphasis
print(color(BOLD + quote + RESET, MAGENTA))