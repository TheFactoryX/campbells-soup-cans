"""
Campbell's Soup Can #4629
Produced: 2026-08-16 13:44:50
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes
C_RESET = "\033[0m"
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_MAGENTA = "\033[95m"
C_CYAN = "\033[96m"
C_WHITE = "\033[97m"

def slow_print(text, color=C_WHITE, delay=0.04):
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay)
    print(C_RESET, end='')

# The philosophical quote in Woody Allen's style
quote = (
    "I don't want to achieve immortality through my work; "
    "I just want to avoid the awkward small talk with the afterlife receptionist."
)

# ASCII art speech bubble
bubble_top = f"{C_CYAN}   _________{C_RESET}"
bubble_mid1 = f"{C_CYAN}  /         \\\\  {C_RESET}"
bubble_mid2 = f"{C_CYAN} | {C_YELLOW}{quote}{C_CYAN} |  {C_RESET}"
bubble_mid3 = f"{C_CYAN}  \\\\         /  {C_RESET}"
bubble_bottom = f"{C_CYAN}