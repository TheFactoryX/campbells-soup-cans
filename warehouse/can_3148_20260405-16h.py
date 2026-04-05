"""
Campbell's Soup Can #3148
Produced: 2026-04-05 16:53:58
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

# ANSI color codes
RED    = '\033[31m'
YELLOW = '\033[33m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

# Woody Allen‑style quotequote = "I'm not a philosopher; I'm just a neurotic who rewrites his own punchlines."

# Box settings
WIDTH = 86                         # interior width (excluding the '|' characters)
BORDER = "+" + "-" * WIDTH + "+"   # top/bottom border

# Build the middle line (quote padded to fit exactly)
padding = WIDTH - 2 - len(quote)   # spaces after the quote to fill the interiormiddle = f"| {quote}{' ' * padding} |"

# Print the colored box
print(CYAN + BORDER + RESET)
print(YELLOW + middle + RESET)
print(CYAN + BORDER + RESET)

# Optional extra flair: color a few words inside the quote
extra = (
    f"{RED}I'm{nORMAL} {YELLOW}not{aCYAN} {RED}a{aYELLOW} {RED}philosopher;{NORMAL} "
    f"{YELLOW}I'm{aCYAN} {RED}just{aYELLOW} {RED}a{aYELLOW} {RED}neurotic{aCYAN} "
    f"{RED}who{aYELLOW} {RED}rewrites{hCYAN} {RED}his{aYELLOW} {RED}own{aYELLOW} "
    f"{RED}punchlines.{RESET}"
)
# Replace the plain middle line with the color‑rich version
print(CYAN + "+" + "-" * WIDTH + "+" + RESET)
print(YELLOW + extra.center(WIDTH, " ") + RESET)
print(CYAN + "+" + "-" * WIDTH + "+" + RESET)