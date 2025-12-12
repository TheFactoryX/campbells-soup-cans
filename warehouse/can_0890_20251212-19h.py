"""
Campbell's Soup Can #890
Produced: 2025-12-12 19:28:55
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes
BOLD = "\033[1m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
BLINK = "\033[5m"
RESET = "\033[0m"

# Clear screen
os.system('cls||clear')

# Title
print(f"\n{BOLD}{YELLOW}=== Woody Allen's Existential Crisis Machine ==={RESET}\n")

# ASCII art
print(f"{CYAN}")
print("       .--------.       ")
print("      /   O  O   \\     ")
print("     |    ⌒ ⌒    |      ")
print("      \\  '▱▱'  /       ")
print("       '--------'        ")
print(f"        {BLINK}??{RESET}{CYAN}      ")
print(f"{RESET}")

# Quote box
quote = "Life is meaningless, but at least my therapist thinks I'm making progress."
box_width = len(quote) + 4

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(f"{RED}╔{'═' * box_width}╗{RESET}")
print(f"{RED}║{RESET}  {YELLOW}", end='')
typewriter(quote, 0.04)
print(f"{RED}║{RESET}")
print(f"{RED}╚{'═' * box_width}╝{RESET}")

# Blinking punchline
print(f"\n{BLINK}(Maybe I'll cancel my next appointment...){RESET}")
time.sleep(0.5)
print(f"\033[2K\r{RESET}", end='')
print(f"\n{BLINK}(Maybe I'll cancel my next appointment...){RESET}")
time.sleep(0.5)
print(f"\033[2K\r{RESET}", end='')