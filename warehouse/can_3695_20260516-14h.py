"""
Campbell's Soup Can #3695
Produced: 2026-05-16 14:00:05
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#-*- coding: utf-8 -*-
import sys

def main():
    quote = "I'm scared of death, but I'm more scared of being forgotten."
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    reset = "\033[0m"

    width = 60  # total characters per line (including borders)
    border = magenta + "*" + "-" * (width - 2) + "*" + reset
    print(border)
    print(magenta + "|" + cyan + quote + reset + magenta + "  " + "|" + reset)
    print(border)

if __name__ == "__main__":
    main()