"""
Campbell's Soup Can #1946
Produced: 2026-01-30 15:51:26
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# [31m = Red, [33m = Yellow, [0m = Reset

RED   = '\033[31m'
YELLOW= '\033[33m'
RESET = '\033[0m'

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
border = "+" + "-" * (len(quote) + 2) + "+"

print(f"{RED}{border}")
print(f"|{YELLOW} {quote}{RESET} |")
print(f"{RED}{border}{RESET}")