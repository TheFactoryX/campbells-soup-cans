"""
Campbell's Soup Can #5182
Produced: 2026-10-29 07:06:21
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, printed with ANSI rainbow flair."""
import sys, time

quote = "I don't want immortality. I just want to vanish before the punchline lands."

# ANSI palette for a psychedelic typewriter effect
COLORS = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
]
RST = "\033[0m"

# Clear screen and snap cursor to home
sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()

# Print the quote one character at a time, each in a cycling color
for i, ch in enumerate(quote):
    sys.stdout.write(COLORS[i % len(COLORS)] + ch)
    sys.stdout.flush()
    time.sleep(0.006)

# Reset terminal colors and finish with a newline
print(RST)