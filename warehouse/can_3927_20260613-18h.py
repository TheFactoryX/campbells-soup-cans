"""
Campbell's Soup Can #3927
Produced: 2026-06-13 18:43:44
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # ANSI color codes
    CYAN   = "\033[36m"
    YELLOW = "\033[33m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

    quote = "I'm not afraid of death; I just don't want to be there when it happens, because I'm still finishing my existential to-do list."

    width = 130
    top    = f"{CYAN}{BOLD}+{'─'*(width-2)}+{RESET}"
    middle = f"| {YELLOW}{quote}{RESET} |"
    bottom = f"{CYAN}{BOLD}+{'─'*(width-2)}+{RESET}"

    print("\n")
    print(top)
    print(middle)
    print(bottom)
    print("\n")

if __name__ == "__main__":
    main()