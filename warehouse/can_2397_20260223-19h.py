"""
Campbell's Soup Can #2397
Produced: 2026-02-23 19:31:39
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# ANSI color codes
RESET = '\033[0m'
CYAN  = '\033[96m'
YELLOW= '\033[93m'
MAGENTA= '\033[95m'

quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " — Woody Allen"

# Build a simple box
box_top    = "╔" + "═"*66 + "╗"
box_bottom = "╚" + "═"*66 + "╝"
box_middle = "║" + " "*66 + "║"

def colored(text, color):
    return f"{color}{text}{RESET}"

print(colored(box_top, CYAN))
print(colored(box_middle, CYAN))
print(colored(f"║ {YELLOW}{quote}{RESET}   ║", CYAN))
print(colored(f"║ {MAGENTA}{author}{RESET}   ║", CYAN))
print(colored(box_bottom, CYAN))
print(RESET, end='')