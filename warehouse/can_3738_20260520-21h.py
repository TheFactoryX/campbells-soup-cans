"""
Campbell's Soup Can #3738
Produced: 2026-05-20 21:13:28
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Philosophy Generator
Because existential dread tastes better with sprinkles.
"""

import time
import sys

# ANSI Color Codes
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

def typewriter_effect(text, delay=0.03, color=WHITE):
    """Print text with typewriter effect"""
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(RESET)

def print_brain():
    """Print a little brain ASCII art"""
    brain = f"""
{CYAN}    ╭─────────────╮
    │ {YELLOW}             ╽{RESET} │
    │ {YELLOW}  NEURONE  │{RESET} │
    │ {YELLOW}             ╿{RESET} │
    ╰─────┬─────┬─────╯
          │     │
          ╰─────╯{RESET}
"""
    print(brain)

def print_coffee_cup():
    """Print a coffee cup"""
    cup = f"""
{BROWN := '\033[38;5;94m'}    {BROWN}     ╱│
    {BROWN}    ╱ │
    {BROWN}   ╱  │
    {BROWN}  ╱   │
    {BROWN} ╱    │
    {BROWN}│     │{RESET}
    │     │
    │     │
    ╰─────╯{RESET}
"""
    print(cup)

def main():
    # Opening flourish
    print(f"\n{MAGENTA}{'═' * 50}{RESET}")
    print(f"{RED}{BOLD}   WOODY ALLEN'S PHILOSOPHICAL CORNER{RESET}")
    print(f"{MAGENTA}{'═' * 50}{RESET}\n")
    
    # Print brain
    print_brain()
    
    # The quote - Woody Allen style
    quote = "I'm not afraid of death; I just don't want to be there when it happens... \nbut I'll probably show up anyway out of habit."
    
    print(f"{BLUE}{'─' * 60}{RESET}\n")
    
    # Typewriter effect with color cycling
    colors = [YELLOW, CYAN, WHITE, BLUE]
    for i, line in enumerate(quote.split('\n')):
        color = colors[i % len(colors)]
        typewriter_effect(line, delay=0.04, color=color)
    
    print(f"\n{BLUE}{'─' * 60}{RESET}")
    
    # Author attribution
    author = " — Some neurotic philosopher"
    print(f"\n{GREEN}{author:>40}{RESET}")
    
    # Coffee cup for contemplation
    print("\n")
    print_coffee_cup()
    
    # Footer
    print(f"\n{YELLOW}{'═' * 50}{RESET}")
    print(f"{RED}Next time: Why I don't believe in destiny...{RESET}")
    print(f"{YELLOW}{'═' * 50}{RESET}\n")

if __name__ == "__main__":
    main()