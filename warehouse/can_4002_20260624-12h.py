"""
Campbell's Soup Can #4002
Produced: 2026-06-24 12:00:51
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

# ANSI escape codes for colors
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RED = "\033[31m"

def typewriter(text, color=RESET, delay=0.04):
    """Print text character by character with a delay for an animated effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ASCII art: a quirky, glasses‑wearing character (Woody‑style)
art = f"""{CYAN}
   .-''''-.
  /  '.-'  \\\\
 (  ( o )  )
  \\  `v'  /
   `._.'
{RESET}
"""

print(art)

# Decorative line
decor = f"{GREEN}//{'='*38}\\n{RESET}"
print(decor)

# Woody’s philosophical quote, printed with a typewriter animation
quote = f'{YELLOW}"I don\'t fear death; I just don\'t want to be there when it happens."{RESET}'
typewriter(quote, color=MAGENTA, delay=0.05)