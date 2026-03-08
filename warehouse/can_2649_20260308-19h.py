"""
Campbell's Soup Can #2649
Produced: 2026-03-08 19:35:18
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

# ANSI color helpers
def c(text, code): return f"\033[{code}m{text}\033[0m"

# colorful border
border = c("─" * 50, "33")  # yellow
empty  = c("│ " + " " * 48 + " │", "37")  # white
quote  = [
    "I’m not afraid of death;",
    "I just don’t want to be there when it happens."
]

cls = "\033[2J\033[H"   # clear screen

def slow_print(s, delay=0.05):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Start
slow_print(cls, 0.1)

# Print header
slow_print(border, 0)
for _ in range(3):
    slow_print(empty, 0)

# Typewriter animation for the quote
for line in quote:
    slow_print(c("│ " + line.ljust(48) + " │", "35"), 0.07)  # magenta

# Footer
slow_print(empty, 0)
slow_print(border, 0)
slow_print(c("\nEnjoy the absurdity.\n", "32"), 0)

sys.exit(0)