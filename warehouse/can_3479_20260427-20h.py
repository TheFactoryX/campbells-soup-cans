"""
Campbell's Soup Can #3479
Produced: 2026-04-27 20:18:54
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/envpython3
import sys

# ANSI colour codesGREEN  = '\033[32m'   # border colour
YELLOW = '\033[33m'   # quote colour
RESET  = '\033[0m'    # reset all attributes

# The Woody Allen‑style philosophical quote
quote = ("I’m not afraid of death; I just don’t want to be there when it "
         "happens... but I keep forgetting where I parked my existential dread.")

# Box dimensions
WIDTH = 78                     # total width of the box
INNER_WIDTH = WIDTH - 4        # usable space inside the side borders
BORDER_TOP    = "+" + "-" * (WIDTH - 2) + "+"
BORDER_BOTTOM = BORDER_TOP
SIDE          = "| " + " " * (WIDTH - 4) + " |"
QUOTE_LINE    = "| " + quote.center(INNER_WIDTH) + " |"

def main():
    # Print coloured box
    sys.stdout.write(GREEN + BORDER_TOP + RESET + "\n")
    sys.stdout.write(YELLOW + QUOTE_LINE + RESET + "\n")
    sys.stdout.write(GREEN + BORDER_BOTTOM + RESET + "\n")

if __name__ == "__main__":
    main()