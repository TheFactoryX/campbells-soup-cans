"""
Campbell's Soup Can #4063
Produced: 2026-07-01 16:39:38
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

# ANSI color definitions
RED = '\033[31m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "Life is like an old movie — boring plot, terrible special effects, but I keep watching because the popcorn is endless."

# Box dimensions
WIDTH = 60
border = "+" + "-" * (WIDTH-2) + "+"
empty  = "|" + " " * (WIDTH-2) + "|"

# Wrap the quote to the box width
words = quote.split()
lines = []
cur = ""
for w in words:
    test = cur + (" " if cur else "") + w
    if len(test) <= WIDTH-4:   # leave room for the "| " and " |"
        cur = test
    else:
        lines.append(cur)
        cur = w
if cur:
    lines.append(cur)

# Pad each line to full width
lines = [l.ljust(WIDTH-4) for l in lines]

# Animation delay
delay = 0.3

# Optional opening “sparkle” animation
for _ in range(3):
    sys.stdout.write("\r" + ("*" * WIDTH) + "\n")
    sys.stdout.flush()
    time.sleep(delay)

print()  # blank line before the box

# Print each line with alternating colors and a short pause
for i, line in enumerate(lines):
    color = RED if i % 2 == 0 else YELLOW
    sys.stdout.write(f"| {color}{line}{RESET} |\n")
    sys.stdout.flush()
    time.sleep(delay if i < len(lines)-1 else 0)

# Bottom border
sys.stdout.write(border + "\n")
sys.stdout.flush()

# Final punch‑line in bold cyan
final = f"{CYAN}{BOLD}...and that's why I never trust a storyboard.{RESET}"
sys.stdout.write(final + "\n")