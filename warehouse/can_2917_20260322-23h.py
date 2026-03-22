"""
Campbell's Soup Can #2917
Produced: 2026-03-22 23:44:01
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

python#!/usr/bin/env python3
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

quote = "I'm not afraid of death; I just don't want to be there."
quote_line = f"│ {quote} │"
width = len(quote_line)
border_top = "┌" + "─" * (width - 2) + "┐"
border_bottom = "└" + "─" * (width - 2) + "┘"
print(f"{GREEN}{border_top}{RESET}")
print(f"{YELLOW}{quote_line}{RESET}")
print(f"{GREEN}{border_bottom}{RESET}")