"""
Campbell's Soup Can #788
Produced: 2025-12-08 05:38:28
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Woody glasses ASCII art
GLASSES = f"""
{UNDERLINE}      
   ⎛•_•⎞ {' '*18}⎛•_•⎞ 
  ⎛   ⎞ {' '*22}⎛   ⎞ 
   ⎝   │ {' '*7}{GREEN}Mental Breakdown{RESET}{' '*12}│   ⎠ 
"""

def typewriter(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Print animated ASCII glasses
    print(f"\n{YELLOW}{BOLD}")
    for line in GLASSES.split('\n'):
        typewriter(line, delay=0.01)
    print(RESET)

    # The quote with color highlights
    quote_parts = [
        (f"{RED}Life", 0.3),
        (" is basically ", 0.02),
        (f"{CYAN}a restaurant", 0.1),
        (" where you're both\n", 0.02),
        ("the waiter ", 0.04),
        (f"{YELLOW}(constantly worrying)", 0.08),
        (" and the customer ", 0.04),
        (f"{MAGENTA}(never satisfied)", 0.1),
        (" —", 0.2),
        (f"\n\n{GREEN}and no one", 0.2),
        (" leaves ", 0.1),
        (f"{RED}a tip.{RESET}", 0.4)
    ]

    # Typing animation with differential speed
    for text, speed in quote_parts:
        typewriter(text, delay=speed)

    # Wait before showing attribution
    time.sleep(0.5)
    print(f"\n{' '*18}— {BOLD}Neurotic Philosopher{RESET}\n")

if __name__ == "__main__":
    main()