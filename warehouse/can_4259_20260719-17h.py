"""
Campbell's Soup Can #4259
Produced: 2026-07-19 17:17:33
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
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    width = 100
    cyan = "\033[96m"
    yellow = "\033[93m"
    reset = "\033[0m"

    top = f"{cyan}+{'-' * (width - 2)}{reset}+"
    middle = f"|{yellow}{quote:<{width - 2}}{reset}|"

    print(top)
    print(middle)
    print(top)

if __name__ == "__main__":
    main()