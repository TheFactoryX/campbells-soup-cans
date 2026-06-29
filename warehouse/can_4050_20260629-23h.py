"""
Campbell's Soup Can #4050
Produced: 2026-06-29 23:15:57
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
Woody Allen's Philosophical Quote Generator
Because existential crisis deserves some style.
"""

import time
import sys

# ANSI Color Codes
RESET = '\033[0m'
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter(text, delay=0.03, color=RESET):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_box(text, color=CYAN):
    """Print text inside a decorative box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    print(color + '┌' + '─' * (max_len + 2) + '┐' + RESET)
    for line in lines:
        print(color + '│' + RESET + ' ' + line.ljust(max_len) + ' ' + color + '│' + RESET)
    print(color + '└' + '─' * (max_len + 2) + '┘' + RESET)

def main():
    # The quote that sums up my relationship with existence
    quote = "I used to think I wanted immortality...\nthen I realized I'm not even good at mortality."
    
    # Header with some existential dread
    print("\n" * 2)
    header = f"{RED}{BOLD}   _ _ _   _ _ _   _ _ _   _ _ _   _ _ _   _ _ _   _ _ _  {RESET}"
    subheader = f"{YELLOW}  |   | |_|   | |_|   | |_|   | |_|   | |_|   | |_|   | |_| {RESET}"
    print(header)
    print(subheader)
    print(f"{MAGENTA}{BOLD}    WOODY ALLEN-STYLE PHILOSOPHY GENERATOR v1.0    {RESET}")
    print(f"{BLUE}         (Because thinking is hard, let me do it for you)         {RESET}")
    print()
    
    # Animated intro
    intro_text = f"{GREEN}Calculating the meaning of life...{RESET}"
    for i in range(3):
        typewriter(intro_text + ".", delay=0.2, color=GREEN)
        time.sleep(0.3)
        sys.stdout.write('\b')
    
    print()
    time.sleep(0.5)
    
    # Print the philosophical box of doom
    print()
    print_box(quote, MAGENTA)
    print()
    
    # Signature with neurotic flair
    signature = f"{RED}{BOLD}                                                               \n" \
                f"{RED}                                                               \n" \
                f"{RED}                                                               \n" \
                f"{RED}                                                               \n" \
                f"{RED}    I'm not saying I'm lazy, I'm just conducting a comprehensive{RESET}\n" \
                f"{RED}    study on the amount of effort required to care about things.{RESET}\n" \
                f"{YELLOW}                                                           \n" \
                f"{YELLOW}    --- The Great Existentialist (probably)\n"
    
    print(signature)
    
    # Footer joke
    print()
    footer = f"{CYAN}This program has found meaning in 0.0001 seconds.{RESET}"
    typewriter(footer, delay=0.05, color=CYAN)
    print(f"{YELLOW}Probably should go now. I have a date with my therapist.{RESET}")

if __name__ == "__main__":
    main()