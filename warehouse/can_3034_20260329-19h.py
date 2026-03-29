"""
Campbell's Soup Can #3034
Produced: 2026-03-29 19:47:06
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style philosophical quote with ANSI colors

# ANSI escape codes
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
BOLD   = '\033[1m'
RESET  = '\033[0m'

# Quote in Woody Allen's neurotic stylequote = "I am not afraid of death; I just don't want to be there when it happens."
quote = quote.center(58)

# Frame pieces
top_left  = CYAN + BOLD + '┌' + RESET
top_right = CYAN + BOLD + '┐' + RESET
bottom_left = CYAN + BOLD + '└' + RESET
bottom_right = CYAN + BOLD + '┘' + RESET
horizontal = CYAN + BOLD + '─' * 58 + RESET
vertical   = CYAN + BOLD + '│' + RESET

# Build the box
top    = top_left + horizontal + top_right
bottom = bottom_left + horizontal + bottom_right
colored_quote = MAGENTA + BOLD + quote + RESET
middle = vertical + ' ' + colored_quote + ' ' + vertical

# Print everything
print(top)
print(middle)
print(bottom)