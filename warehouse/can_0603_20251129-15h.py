"""
Campbell's Soup Can #603
Produced: 2025-11-29 15:30:03
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

def woody_print(text):
    colors = ['\033[93m', '\033[95m']
    for i, char in enumerate(text):
        sys.stdout.write(random.choice(colors) + char)
        sys.stdout.flush()
        delay = random.choice([0.04, 0.07, 0.05, 0.1])
        time.sleep(delay * (1 + (i % 3 == 0)))
    print('\033[0m')

def main():
    print('\033[2J\033[H')  # Clear screen
    print('\033[36m' + "╔══════════════════════════════════════════════════╗")
    print("║" + " " * 52 + "║")
    print("║  \033[33m*\033[36m  " + " " * 46 + "  \033[33m*\033[36m  ║")
    quote = "I believe life is meaningless, but what really keeps me up"
    woody_print("\033[36m║      \033[0m" + quote.ljust(44) + "\033[36m║")
    quote = "at night is that I can't find matching socks."
    woody_print("\033[36m║      \033[0m" + quote.ljust(44) + "\033[36m║")
    print("║" + " " * 52 + "║")
    print("║" + " " * 52 + "║")
    author = "─ Woody Allen's Missing Sock"
    print(f"\033[36m║\033[0m{author:>50}\033[36m  ║")
    print("╚══════════════════════════════════════════════════╝\033[0m")
    time.sleep(1)
    print("\n\033[5m?\033[0m", end=" ")  # Blinking cursor

if __name__ == "__main__":
    main()