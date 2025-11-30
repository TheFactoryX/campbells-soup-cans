"""
Campbell's Soup Can #628
Produced: 2025-11-30 18:41:51
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def typing_effect(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    print("\033[H\033[J")
    
    # Coffee cup ASCII art
    print(f"{WHITE}")
    print(r"    ( (")
    print(r"     ) )")
    print(r"  ........")
    print(r"  |      |]")
    print(r"  \      /")
    print(r"   `----'")
    print(f"{RESET}")
    
    # Quote box
    print(f"{YELLOW}╔{'═'*52}╗{RESET}")
    print(f"{YELLOW}║{' '*52}║{RESET}")
    quote = [
        '"Life has no meaning except the temporary relief we get",
        "from complaining about it over coffee - which itself is",
        "just bitter bean water that reminds us how tired we are",
        "of pretending to understand modern art."'
    ]
    
    for line in quote:
        print(f"{YELLOW}║{RESET}  ", end="")
        typing_effect(f"{CYAN}{BOLD}{line}{RESET}", CYAN, 0.03)
        print(f"{YELLOW}║{' '*52}║{RESET}")
    
    print(f"{YELLOW}║{' '*52}║{RESET}")
    print(f"{YELLOW}║{' '*28}{RED}- Woody Allen's Barista{RESET}{' '*14}{YELLOW}║{RESET}")
    print(f"{YELLOW}╚{'═'*52}╝{RESET}")

if __name__ == "__main__":
    main()