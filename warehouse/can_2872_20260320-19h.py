"""
Campbell's Soup Can #2872
Produced: 2026-03-20 19:49:13
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

def C(c, s):
    return f"\033[{c}m{s}\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens."
border = C(36, "╔═════════════════════════════════╗")
inner  = C(36, "║   " + " " * 46 + "   ║")
quote_line = C(33, f"║   {quote}   ║")
empty = inner
bottom = C(36, "╚═════════════════════════════════╝")

def main():
    print(border)
    print(inner)
    print(quote_line)
    print(inner)
    print(bottom)
    stars = C(32, "*" * 20)
    for _ in range(5):
        print(C(31 + _ % 6, stars))
        time.sleep(0.2)

if __name__ == "__main__":
    main()