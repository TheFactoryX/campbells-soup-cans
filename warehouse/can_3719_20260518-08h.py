"""
Campbell's Soup Can #3719
Produced: 2026-05-18 08:52:22
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/envpython3
import sys

def main():
    RED   = "\033[31m"
    GREEN = "\033[32m"
    YELLOW= "\033[33m"
    CYAN  = "\033[36m"
    RESET = "\033[0m"

    width = 40
    border = f"{CYAN}+{'='*width}+{RESET}"
    top    = f"{CYAN}|{' '*width}{RESET}{CYAN}|{RESET}"
    quote = "I'm terrified of death; I'm always late."
    padded_quote = quote + " " * (width - len(quote))
    middle = f"{CYAN}|{RED}{padded_quote}{RESET}{CYAN}|{RESET}"
    bottom = f"{CYAN}|{' '*width}{RESET}{CYAN}|{RESET}"
    footer = f"{CYAN}+{'-'*width}+{RESET}"

    print(border)
    print(top)
    print(middle)
    print(bottom)
    print(footer)

if __name__ == "__main__":
    main()