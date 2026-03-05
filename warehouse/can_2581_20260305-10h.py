"""
Campbell's Soup Can #2581
Produced: 2026-03-05 10:01:51
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# The philosophical quip in classic Woody Allen neurotic flavor
quote = "I'm not afraid of death; I just don't want to be there when it steals my last éclair."

# Simple decorative border
border = "┌" + "─" * 60 + "┐"
bottom = "└" + "─" * 60 + "┘"
side = "│"

def typewriter(s, delay=0.02):
    """Prints a string character‑by‑character for a typewriter effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Print the bordered, colored output
typewriter("\033[95m" + border + "\033[0m")  # magenta border
typewriter("\033[95m" + side + "   \"" + quote + "\"   \033[0m")
typewriter("\033[95m" + side + " — a Woody Allen‑style existential sigh — \033[0m")
typewriter("\033[95m" + side + "\033[0m")
typewriter("\033[95m" + bottom + "\033[0m")  # reset color afterwards