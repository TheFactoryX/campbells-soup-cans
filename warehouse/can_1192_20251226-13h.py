"""
Campbell's Soup Can #1192
Produced: 2025-12-26 13:44:53
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI color codes
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
BLINK = "\033[5m"
RESET = "\033[0m"

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = (
        "The universe is expanding at an alarming rate, "
        "which really just makes me feel worse about \n"
        "all those unused gym memberships and unread books."
    )

    # Clear screen
    print("\033[H\033[J", end="")

    # ASCII art decoration
    print(f"{ORANGE}╔{'═' * 63}╗{RESET}")
    print(f"{ORANGE}║{RESET}{' ' * 63}{ORANGE}║{RESET}")

    # Center the quote visually
    print(f"{ORANGE}║{RESET}  ", end="")
    slow_print(f"{YELLOW}{BLINK}✨ {RESET}{YELLOW}{quote}{RESET}", 0.04)
    
    print(f"{ORANGE}║{RESET}{' ' * 63}{ORANGE}║{RESET}")
    print(f"{ORANGE}╚{'═' * 63}╝{RESET}")

    # Footer
    time.sleep(0.5)
    slow_print(f"\n{' ' * 30}{ORANGE}— Woody Allen's anxiety{RESET}\n", 0.07)

if __name__ == "__main__":
    main()