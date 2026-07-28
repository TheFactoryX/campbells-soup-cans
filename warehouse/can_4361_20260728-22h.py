"""
Campbell's Soup Can #4361
Produced: 2026-07-28 22:16:35
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED   = "\033[31m"
CYAN  = "\033[36m"
BOLD  = "\033[1m"
RESET = "\033[0m"

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

def typewriter(text, speed=0.02):
    """Prints text character by character for a playful effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# Build the visual presentation
border_top    = f"{RED}╔{'─'*40}╗{RESET}"
border_bottom = f"{RED}╚{'─'*40}╚{RESET}"
quote_line    = f"{CYAN}{BOLD}{quote}{RESET}"

# Animate the output
typewriter(border_top)
time.sleep(0.05)
typewriter(quote_line)
time.sleep(0.05)
typewriter(border_bottom)