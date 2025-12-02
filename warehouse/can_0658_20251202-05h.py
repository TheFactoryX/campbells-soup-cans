"""
Campbell's Soup Can #658
Produced: 2025-12-02 05:35:04
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote():
    quote = "I tried to take a day off from worrying, but I kept checking in on it."
    author = "- Woody Allen (probably)"
    width = 60

    # ANSI escape codes
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLINK = "\033[5m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Top border
    print(f"\n{RED}╔{'═' * (width-2)}╗{RESET}")

    # Empty line
    print(f"{RED}║{' ' * (width-2)}║{RESET}")

    # Quote with typing animation
    print(f"{RED}║{RESET} ", end='')
    for char in quote:
        print(f"{YELLOW}{BOLD}{char}{RESET}", end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print(f" {RED}║{RESET}")

    # Empty line
    print(f"{RED}║{' ' * (width-2)}║{RESET}")

    # Author with blinking effect
    print(f"{RED}║{RESET}{' ' * ((width - len(author)) // 2 - 1)}"
          f"{BLINK}{author}{RESET}"
          f"{' ' * ((width - len(author)) // 2 - 1)}{RED}║{RESET}")

    # Bottom border
    print(f"{RED}╚{'═' * (width-2)}╝{RESET}\n")

if __name__ == "__main__":
    print_quote()