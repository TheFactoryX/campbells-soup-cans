"""
Campbell's Soup Can #4027
Produced: 2026-06-27 12:19:24
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
GREEN = '\033[92m'
WHITE = '\033[97m'

def typewriter(text, color, delay=0.03):
    """Prints text with typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_box(content, width=60):
    """Prints content in a decorative box"""
    print(f"\n{CYN}╔{'═' * (width-2)}╗{RESET}")
    print(f"{CYAN}║{RESET}{WHITE}{'':=^{width-2}}{CYAN}║{RESET}")
    
    for line in content.split('\n'):
        padded = f" {line} "
        print(f"{CYAN}║{RESET}{WHITE}{padded:<{width-2}}{CYAN}║{RESET}")
    
    print(f"{CYAN}╚{'═' * (width-2)}╝{RESET}\n")

def main():
    # Animated header
    header = f"{RED}★ {YELLOW}WOODY ALLEN{RESET}{RED} ★{RESET}"
    typewriter(header, RED, 0.1)
    
    time.sleep(0.5)
    
    # Print the philosophical quote
    quote = '"I\'m not afraid of death; I just don\'t want to be there when it happens."\n\n   — A man who understood the existential predicament of our cellular misfortune'
    
    print_box(quote)
    
    time.sleep(1)
    
    # Add some existential commentary
    commentary = f"{MAGENTA}... contemplating the void since {time.strftime('%Y')} ...{RESET}"
    typewriter(commentary, MAGENTA, 0.05)
    
    time.sleep(0.5)
    
    # Final neurotic thought
    final = f"{YELLOW}🌀{RESET}{BLUE}  (still working on the sequel: \"Waiting to Die: A Love Story\")  {YELLOW}🌀{RESET}"
    typewriter(final, BLUE, 0.02)

if __name__ == "__main__":
    main()