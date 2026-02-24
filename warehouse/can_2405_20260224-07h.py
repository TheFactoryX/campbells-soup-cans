"""
Campbell's Soup Can #2405
Produced: 2026-02-24 07:17:46
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

# ANSI colour codes
GREEN  = "\033[92m"
MAGENTA = "\033[95m"
RESET  = "\033[0m"

# The Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."
inner_width = 80
spaces_needed = inner_width - 1 - len(quote)  # 8 spaces after the quote

# Build coloured box components
top    = GREEN + "╔" + "═" * inner_width + "╗" + RESET
middle = (GREEN + "║ " + MAGENTA + quote + RESET + 
          GREEN + (" " * spaces_needed) + "║" + RESET)
bottom = GREEN + "╚" + "═" * inner_width + "╝" + RESET

# Assemble the full frame (including newlines)
frame = top + "\n" + middle + "\n" + bottom + "\n"

def animate_print(s, delay=0.02):
    """Print each character of s with a tiny delay for a typing effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Animate the whole box
animate_print(frame)