"""
Campbell's Soup Can #5045
Produced: 2026-09-30 06:43:57
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



#!/usr/bin/env python3
import time
import sys

# ANSI color codes
YELLOW = '\033[93m'
RESET = '\033[0m'

# Woody Allen style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Create a decorative border
border = "─" * 60

# Print top border
print(YELLOW + "┌" + border + "┐" + RESET)

# Typewriter effect
sys.stdout.write(YELLOW)
for char in quote:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write(RESET)
print()

# Print bottom border
print(YELLOW + "└" + border + "┘" + RESET)