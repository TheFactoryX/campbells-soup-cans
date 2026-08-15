"""
Campbell's Soup Can #4594
Produced: 2026-08-15 01:49:14
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Simple typing animation effect
def type_print(text, delay=0.03, color=WHITE):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

# Woody Allen‑style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# ASCII art border (a neurotic little cloud)
border_top    = f"{CYAN}╔{'═' * (len(quote) + 4)}╗{RESET}"
border_mid    = f"{CYAN}║{RESET}  {quote}  {CYAN}║{RESET}"
border_bottom = f"{CYAN}╚{'═' * (len(quote) + 4)}╝{RESET}"

# Optional tiny animated cloud (just for fun)
cloud = [
    f"{WHITE}   .--.{RESET}",
    f"{WHITE} .-(    ).{RESET}",
    f"{WHITE}(  Woody ){RESET}",
    f"{WHITE} '-(____)'-{RESET}"
]

def main():
    print()  # some space
    for line in cloud:
        print(line)
        time.sleep(0.1)
    print()
    # Print top border
    print(border_top)
    # Print the quote with typing effect inside the box
    sys.stdout.write(f"{CYAN}║{RESET}  ")
    type_print(quote, delay=0.04, color=YELLOW)
    sys.stdout.write(f"{CYAN}  ║{RESET}\n")
    # Print bottom border
    print(border_bottom)
    print()  # final newline

if __name__ == "__main__":
    main()