"""
Campbell's Soup Can #4288
Produced: 2026-07-22 09:38:28
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def main():
    RED = '\033[31m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    MAGENTA = '\033[35m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

    quote = "I'm not afraid of dying, but I'm afraid of missing my next existential crisis."
    colors = [RED, CYAN, YELLOW, GREEN, MAGENTA, BLUE]

    print()
    for i, c in enumerate(quote):
        color = colors[i % len(colors)]
        sys.stdout.write(color + c)
        sys.stdout.flush()
        time.sleep(0.03)
    print(RESET)
    print()
    print(RED + " " * 20 + "✦✦✦✦✦")
    print(CYAN + " " * 15 + "╔" + "─" * 30 + "╗")
    print(CYAN + " " * 15 + "║" + " " * 30 + "║")
    print(CYAN + " " * 15 + "╚" + "─" * 30 + "╝")
    print(RESET)

if __name__ == "__main__":
    main()