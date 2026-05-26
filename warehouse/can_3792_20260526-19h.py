"""
Campbell's Soup Can #3792
Produced: 2026-05-26 19:27:49
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
Woody Allen Philosophical Quote Generator
Because existential dread is more fun with colors!
"""

import time
import sys

# ANSI Color Codes
BLACK = '\033[0;30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
MAGENTA = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
BLINK = '\033[5m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'
RESET = '\033[0m'

def typewriter_effect(text, delay=0.03, color=WHITE):
    """Print text with a typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    print()

def print_box(text, color=CYAN, padding=2):
    """Print text inside a decorative box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    top_border = f"{color}╔{'═' * (max_len + 2 * padding)}╗{RESET}"
    bottom_border = f"{color}╚{'═' * (max_len + 2 * padding)}╝{RESET}"
    
    print(top_border)
    for line in lines:
        print(f"{color}║{RESET}{' ' * padding}{line}{' ' * (max_len - len(line) + padding)}{color}║{RESET}")
    print(bottom_border)

def main():
    # Clear screen (works on most terminals)
    print('\033[2J\033[H', end='')
    
    # Title with animation
    title = f"{MAGENTA}{BOLD} existential crisis {RESET}{DIM}...{RESET}"
    print()
    typewriter_effect(title, 0.1, MAGENTA)
    print()
    
    # The Woody Allen quote
    quote = f"{RED}{ITALIC}I'm not afraid of death; I just don't want to be there when it happens.{RESET}"
    
    # Print with box
    print_box(" woody allen philosophy ", quote, YELLOW)
    
    print()
    print()
    
    # Additional existential commentary
    commentary = f"{DIM}...and that's why I'm sitting here writing Python scripts instead of living life.{RESET}"
    typewriter_effect(commentary, 0.05, DIM)
    
    print()
    print(f"{GREEN}{BOLD}Press Enter to existentially contemplate again...{RESET}", end='')
    input()
    
    # Second quote for good measure
    print()
    print(f"{CYAN}{BOLD}{'='*50}{RESET}")
    print()
    
    quote2 = f"{BLUE}{BOLD}Life is full of misery, loneliness, and suffering - and it's all over much too soon.{RESET}"
    print_box(" alternate universe woody", quote2, BLUE)
    
    print()
    print(f"{RED}{BLINK}{BOLD} But hey, at least we have internet! {RESET}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Wise choice. Run away from existential dread!{RESET}")
    except Exception as e:
        print(f"\n{GREEN}Ah, but what is reality, really? Even my code is confused: {e}{RESET}")