"""
Campbell's Soup Can #1309
Produced: 2025-12-31 21:30:42
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic philosophical quote in Woody Allen's style, presented with a
nervous, jittery text animation.
"""

import sys
import time
import random
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text, delay=0.03):
    """Print text character by character with a slight delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        # Add a tiny random delay to simulate nervous typing
        if random.random() < 0.1:
            time.sleep(random.uniform(0.01, 0.05))

def jittery_box(text, width=60):
    """Print text inside a jittery, nervous box."""
    # Create the top border with jitter
    top_border = ""
    for _ in range(width):
        if random.random() < 0.7:
            top_border += "═"
        else:
            top_border += "─"
    
    # Create the bottom border with jitter
    bottom_border = ""
    for _ in range(width):
        if random.random() < 0.7:
            bottom_border += "═"
        else:
            bottom_border += "─"
    
    # Center the text
    left_padding = (width - len(text)) // 2
    centered_text = " " * left_padding + text
    
    # Print with jittery animation
    for _ in range(3):  # Shake the box
        print(f"  {MAGENTA}╔{top_border}╗{RESET}")
        for line in centered_text.split('\n'):
            print(f"  {MAGENTA}║{RESET}{line:<{width}}{MAGENTA}║{RESET}")
        print(f"  {MAGENTA}╚{bottom_border}╝{RESET}")
        time.sleep(0.1)
        clear_screen()
        time.sleep(0.05)

def main():
    """Main function to display the Woody Allen-style quote."""
    # Clear the screen first
    clear_screen()
    
    # The quote (Woody Allen style - neurotic, funny, existential)
    quote = "I'm not afraid of death; I'm just afraid of arriving at the pearly gates and being told there's been a mistake and they meant to take my neighbor instead. I'd feel terrible about it, but also a little relieved."
    
    # Print a jittery, nervous introduction
    print("\n" * 5)
    print_slowly(f"{CYAN}    *clears throat nervously*{RESET}\n")
    time.sleep(0.5)
    print_slowly(f"{CYAN}    Listen, I've been thinking about mortality...{RESET}\n")
    time.sleep(0.8)
    print_slowly(f"{CYAN}    And frankly, it's been keeping me up at night.{RESET}\n")
    time.sleep(1.0)
    
    # Print the quote in a jittery box
    clear_screen()
    print("\n" * 8)
    jittery_box(f"{BOLD}{WHITE}{quote}{RESET}")
    
    # Print attribution with a shaky effect
    time.sleep(0.5)
    print(f"\n{ITALIC}{YELLOW}    - Woody Allen (probably){RESET}")
    print(f"{ITALIC}{CYAN}    (or at least someone who worries about everything){RESET}")
    
    # Add some final nervous ticks
    time.sleep(1.0)
    print(f"\n{RED}    *fidgets with glasses*")
    print(f"    *checks watch*")
    print(f"    *sighs*{RESET}")

if __name__ == "__main__":
    main()