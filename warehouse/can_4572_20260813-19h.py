"""
Campbell's Soup Can #4572
Produced: 2026-08-13 19:20:57
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[0m'

def type_print(text, delay=0.05, color=""):
    """Print text character by character with a delay for animation."""
    colored = f"{color}{text}{RESET}"
    for ch in colored:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()  # move to new line after the animation

# ASCII art: a neurotic thinking face (Woody Allen style)
art = f"""
{YELLOW}   .-'''''-.
  /  * *  \\
 |   o o   |
  \\  `~'  /
   `~~~~`
{RESET}
"""

type_print(art)

# Woody Allen style philosophical quote (single line)
quote = f"{GREEN}I'm terrified of death, but I also don't want to be there when it happens.{RESET}"
type_print(quote)