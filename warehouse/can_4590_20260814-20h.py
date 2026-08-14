"""
Campbell's Soup Can #4590
Produced: 2026-08-14 20:45:32
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
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAG   = "\033[35m"
CYAN  = "\033[36m"
RESET = "\033[0m"
BOLD  = "\033[1m"

# Woody Allen‑style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Prepare a decorative box
padding = 2
width   = len(quote) + 2 * padding
top    = f"{CYAN}╔{'═' * width}╗{RESET}"
bottom = f"{CYAN}╚{'═' * width}╝{RESET}"
line   = f"{CYAN}║{RESET}{' ' * padding}{YELLOW}{BOLD}{quote}{RESET}{' ' * padding}{CYAN}║{RESET}"

def slow_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    slow_print(top)
    slow_print(line)
    slow_print(bottom)

if __name__ == "__main__":
    main()