"""
Campbell's Soup Can #2535
Produced: 2026-03-03 03:14:03
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"

def print_with_typewriter(text, color, delay=0.02):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)

def print_heart():
    heart = [
        "  **    **  ",
        " *  *  *  * ",
        "*    **    *",
        "*          *",
        " *        * ",
        "  *      *  ",
        "   *    *   ",
        "    *  *    ",
        "     **     "
    ]
    for line in heart:
        print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.05)

def main():
    # Create a Woody Allen-style quote
    quote = "I've discovered that the best way to deal with existential dread is to avoid it at all costs. If that fails, I just pretend I'm a character in a French film and brood accordingly. It's not that I'm afraid of death - I just don't want to be there when it happens to my health insurance."
    
    # Calculate terminal width for centering
    width = 60
    inner_width = 50
    
    # Create decorative frame
    top = f"{YELLOW}┌{'─' * (width-2)}┐{RESET}"
    bottom = f"{YELLOW}└{'─' * (width-2)}┘{RESET}"
    
    # Print top border
    print(top)
    
    # Print neurotic ASCII art
    print(f"{YELLOW}│{RESET}{' ' * ((width-18)//2)}{RED}*(^_^)*{RESET}{' ' * ((width-18)//2)}{YELLOW}│{RESET}")
    print(f"{YELLOW}│{RESET}{' ' * ((width-32)//2)}{GREEN}I'm not a hypochondriac,{RESET}{' ' * ((width-32)//2)}{YELLOW}│{RESET}")
    print(f"{YELLOW}│{RESET}{' ' * ((width-32)//2)}{GREEN}I just know things!{RESET}{' ' * ((width-32)//2)}{YELLOW}│{RESET}")
    
    # Print the quote with typewriter effect
    for line in [quote[i:i+inner_width] for i in range(0, len(quote), inner_width)]:
        padded = line.ljust(inner_width)
        print(f"{YELLOW}│{RESET} ", end='')
        print_with_typewriter(padded, CYAN, 0.015)
        print(f" {YELLOW}│{RESET}")
    
    # Print the heart animation
    print(f"{YELLOW}│{RESET}{' ' * ((width-2)//2 - 5)}", end='')
    print_heart()
    print(f"{YELLOW}│{RESET}{' ' * ((width-2)//2 - 5)}{MAGENTA}♥{RESET}{' ' * ((width-2)//2 - 5)}{YELLOW}│{RESET}")
    
    # Print philosophical footer
    footer = "— A neurotic thought bubble, probably"
    print(f"{YELLOW}│{RESET}{' ' * ((width - len(footer))//2)}{RED}{footer}{RESET}{' ' * ((width - len(footer))//2)}{YELLOW}│{RESET}")
    
    # Print bottom border
    print(bottom)
    
    # Add a final neurotic thought
    time.sleep(0.5)
    print(f"\n{BOLD}{CYAN}Why is this program printing existential dread?{RESET}")
    time.sleep(0.3)
    print(f"{BOLD}{RED}It's probably because I wrote it while avoiding my taxes.{RESET}")

if __name__ == "__main__":
    # Clear screen for better effect
    print("\033[2J\033[H", end='')
    main()
    # Add a blinking cursor effect at the end
    for _ in range(3):
        print(f"{BOLD}{YELLOW}_ {RESET}", end='\r')
        time.sleep(0.3)
        print(f"{BOLD}{YELLOW} {RESET}", end='\r')
        time.sleep(0.3)