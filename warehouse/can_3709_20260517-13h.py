"""
Campbell's Soup Can #3709
Produced: 2026-05-17 13:57:17
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
    quote = "I’m not afraid of death; I’m just terrified I’ll spend eternity listening to my own complaints."
    width = 100
    cyan = "\033[96m"
    yellow = "\033[93m"
    reset = "\033[0m"

    top = f"{cyan}╔{'═'*width}{cyan}╗{reset}"
    bottom = f"{cyan}╚{'═'*width}{cyan}╝{reset}"
    side = f"{cyan}║{' '*width}{cyan}║{reset}"
    padding = width - 4 - len(quote)
    middle = f"{yellow}║ {quote}{' '*padding}{yellow}║{reset}"

    print(top)
    print(side)
    print(middle)
    print(side)
    print(bottom)

if __name__ == "__main__":
    main()