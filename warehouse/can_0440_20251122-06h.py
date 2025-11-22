"""
Campbell's Soup Can #440
Produced: 2025-11-22 06:42:09
Worker: Qwen: Qwen3 Max (qwen/qwen3-max)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

def print_with_delay(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote_art():
    # Woody Allen style quote
    quote = "I don't believe in an afterlife, though I am bringing a change of underwear just in case."
    
    # ANSI color codes
    RESET = "\033[0m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    
    # Top border with Woody's name
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD}             WOODY ALLEN'S EXISTENTIAL WISDOM{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    
    # ASCII Art Glasses (Woody's signature look)
    glasses = [
        f"{YELLOW}    .-''-.    .-''-.    ",
        f"{YELLOW}   /  _  \\  /  _  \\   ",
        f"{YELLOW}   | / \\ |  | / \\ |   ",
        f"{YELLOW}   \\ \\_/ /  \\ \\_/ /   ",
        f"{YELLOW}    '-'-'    '-'-'    "
    ]
    
    for line in glasses:
        print(line)
    
    print(f"\n{MAGENTA}{'~'*60}{RESET}\n")
    
    # Animate the quote appearing
    print_with_delay(f"{WHITE}{BOLD}\"{quote}\"{RESET}", 0.04)
    
    print(f"\n{MAGENTA}{'~'*60}{RESET}")
    
    # Philosophical tagline
    tagline = "Existential dread served with a side of bagels."
    print(f"\n{CYAN}{BOLD}{tagline.center(60)}{RESET}\n")
    
    # Bottom border
    print(f"{CYAN}{'='*60}{RESET}")

if __name__ == "__main__":
    woody_quote_art()