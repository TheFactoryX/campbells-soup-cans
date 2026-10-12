"""
Campbell's Soup Can #5097
Produced: 2026-10-12 07:21:45
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI color codes for pretty output
YELLOW = '\033[1;33m'
GREEN  = '\033[1;32m'
RESET  = '\033[0m'

def slow_print(text, delay=0.05):
    """Print characters one by one with a tiny delay for an animated effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()   # finish the line

# --- Display the Woody‑Allen‑style philosophical quote ---

# A whimsical title
slow_print(YELLOW + "⚡️ Woody's Cosmic Quote ⚡️" + RESET + "\n")

# A decorative box containing the quote
slow_print(YELLOW + "╔══════════════════════════════════════════════════════════╗" + RESET)
slow_print(YELLOW + "║" + GREEN + "  \"I'm not afraid of the universe expanding; I'm just afraid\"  " + YELLOW + "║" + RESET)
slow_print(YELLOW + "║" + GREEN + "  that later it will collapse and everyone will realize   " + YELLOW + "║" + RESET)
slow_print(YELLOW + "║" + GREEN + "  they left the stove on!\"                                     " + YELLOW + "║" + RESET)
slow_print(YELLOW + "╚══════════════════════════════════════════════════════════╝" + RESET)

# A little closing flourish
slow_print(YELLOW + "✨ Inspired by endless worries and a malfunctioning kitchen. ✨" + RESET)