"""
Campbell's Soup Can #3650
Produced: 2026-05-11 23:12:06
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# Woody Allen style quote with philosophical neurosis
QUOTE = """
I've spent years trying to achieve immortality through my work, 
but I'm starting to think not dying would be easier.
Also, my dentist is getting old, and I have a wisdom tooth 
that needs extracting before I achieve either of those things.
"""

def print_woodys_quote():
    # ANSI color codes
    RESET = '\033[0m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Calculate maximum line length for the box
    lines = [line for line in QUOTE.strip().split('\n') if line.strip()]
    max_length = max(len(line) for line in lines)
    
    # Print top border with animation
    print(f"{BOLD}{RED}{'═' * (max_length + 6)}{RESET}")
    time.sleep(0.2)
    
    # Print each line with typing effect and color
    for line in lines:
        padded_line = f"{CYAN}{line.center(max_length)}{RESET}"
        print(f"{RED}║ {RESET}{padded_line}{RED} ║{RESET}")
        time.sleep(0.4)
    
    # Print bottom border with animation
    print(f"{BOLD}{RED}{'═' * (max_length + 6)}{RESET}")
    time.sleep(0.3)
    
    # Add a neurotic flourish at the end
    neurotic_endings = [
        f"\n{YELLOW}...I'm also low on existential dread today.{RESET}",
        f"\n{GREEN}...At least my anxiety is consistent.{RESET}",
        f"\n{CYAN}...Did I leave the stove on in my past life?{RESET}"
    ]
    
    print(f"{random.choice(neurotic_endings)}")

if __name__ == "__main__":
    print_woodys_quote()