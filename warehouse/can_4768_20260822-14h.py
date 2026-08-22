"""
Campbell's Soup Can #4768
Produced: 2026-08-22 14:38:17
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def main():
    quote = "I don't want to achieve immortality through my work; I want to achieve it by not dying."
    red = "\033[31m"
    yellow = "\033[33m"
    reset = "\033[0m"

    border_top = f"{red}┌{'─'*40}┐{reset}"
    border_bottom = f"{red}└{'─'*40}┘{reset}"
    box_mid = f"{red}│{yellow}{quote}{reset}{red}│{reset}"

    print(border_top)
    print(box_mid)
    print(border_bottom)

if __name__ == "__main__":
    main()