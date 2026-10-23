"""
Campbell's Soup Can #5153
Produced: 2026-10-23 15:04:37
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
    width = 80
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    
    top_bottom = GREEN + "+" + "-" * (width - 2) + "+" + RESET
    sides = GREEN + "|" + " " * (width - 2) + "|" + RESET
    middle = YELLOW + "|" + " " * 3 + quote + " " * 4 + "|" + RESET
    
    print("\n" + top_bottom)
    print(sides)
    print(middle)
    print(top_bottom)

if __name__ == "__main__":
    main()