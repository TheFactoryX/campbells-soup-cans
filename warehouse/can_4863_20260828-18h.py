"""
Campbell's Soup Can #4863
Produced: 2026-08-28 18:43:18
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    RED = "\033[1;31;40m"
    GREEN = "\033[1;32;40m"
    CYAN = "\033[1;36;40m"
    YELLOW = "\033[1;33;44m"
    RESET = "\033[0m"

    border = GREEN + "+" + "-" * 58 + "+" + RESET
    side = YELLOW + "|" + " " * 58 + "|" + RESET
    title = CYAN + "   " + quote.center(58) + "   " + RESET

    for line in (border, side, title, side, border):
        print(line)
        time.sleep(0.05)

if __name__ == "__main__":
    main()