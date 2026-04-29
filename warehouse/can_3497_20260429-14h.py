"""
Campbell's Soup Can #3497
Produced: 2026-04-29 14:30:54
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_typewriter(text, color='\033[92m', reset='\033[0m', delay=0.03):
    for char in text:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(delay)

def main():
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
    quote = "I save energy for existential crises. It's tiring."
    
    print(f"{BLUE}+{'-'*50}+{RESET}")  # Top border
    
    print(f"{BLUE}|{RESET}" + ' ' * 50 + f"{BLUE}|{RESET}")  # Empty line
    
    # Quote line
    print(f"{BLUE}|{RESET}", end='')  # Start with border
    print_typewriter(quote, GREEN, RESET)
    print(f"{BLUE}|{RESET}")  # End with border
    
    print(f"{BLUE}|{RESET}" + ' ' * 50 + f"{BLUE}|{RESET}")  # Empty line
    
    print(f