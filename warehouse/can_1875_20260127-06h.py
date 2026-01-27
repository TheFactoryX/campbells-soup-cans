"""
Campbell's Soup Can #1875
Produced: 2026-01-27 06:54:38
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
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
    # ANSI escape codes for colors
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Woody Allen-ish quote
    quote = (
        f"\n{YELLOW}╔{'═'*68}╗{RESET}\n"
        f"{YELLOW}║{RESET}  Life is {RED}absolutely meaningless{RESET}, but hey – {BLUE}at least "
        f"the{RESET}\n{YELLOW}║{RESET}  {BLUE}cosmic insignificance{RESET} comes with {MAGENTA}complimentary "
        f"baggage{RESET}\n{YELLOW}║{RESET}  {MAGENTA}anxiety{RESET} and {RED}free cancellation{RESET} "
        f"before {BOLD}death{RESET}.  {YELLOW}║{RESET}\n"
        f"{YELLOW}╚{'═'*68}╝{RESET}\n\n"
        f"{' '*20}– {BOLD}Woody \"Probably\" Allen{RESET}"
    )

    # Typewriter animation with colors preserved
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char not in ['\n', ' ']:
            time.sleep(0.03)
        else:
            time.sleep(0.01)
    print()

if __name__ == "__main__":
    main()