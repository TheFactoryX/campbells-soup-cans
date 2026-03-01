"""
Campbell's Soup Can #2507
Produced: 2026-03-01 16:45:06
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# The Woody Allen‑style philosophical punchline
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# ANSI colour codes
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
RESET  = "\033[0m"

# Frame size
WIDTH  = 62

# Build coloured borders
border = RED + "+" + "-" * (WIDTH - 2) + "+" + RESET
quote_line = YELLOW + quote.center(WIDTH - 2) + RESET
full_output = [border, f"| {quote_line} |", border]

# Print with a tiny pause between lines for a “typewriter” vibe
for line in full_output:
    sys.stdout.write(line + "\n")
    sys.stdout.flush()
    time.sleep(0.3)

# Reset colour at the very end
sys.stdout.write(RESET)