"""
Campbell's Soup Can #4902
Produced: 2026-09-05 00:06:57
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_with_delay(text, delay=0.03, end='\n'):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(end, end='')

def create_ascii_head():
    """Create a simple ASCII art head."""
    return """
    ┌─────┐
    │  o  │
    │  o  │
    │  _  │
    │     │
    └─────┘
    """

def main():
    # Clear screen (works on most systems)
    print('\033[2J\033[H', end='')
    
    # Colors
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Print title
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}")
    print(f"{CYAN}{BOLD}           A WOODY ALLEN PHILOSOPHICAL MOMENT{RESET}")
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}\n")
    
    # Print ASCII head
    print(f"{PURPLE}{create_ascii_head()}{RESET}\n")
    
    # The quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. \
Actually, that's not true. I am afraid of death, but more than that, I'm afraid of \
not existing before I was born, and then after death, just... nothing. It's like \
being canceled mid-sentence. And the worst part? I'll probably spend my entire \
life worrying about it while eating a sandwich that's not even that good."
    
    author = "— Woody Allen (probably)"
    
    # Print quote with typewriter effect
    print(f"{YELLOW}{BOLD}The philosopher ponders:{RESET}\n")
    
    # Break quote into lines for better display
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= 70:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Print each line with delay
    for line in lines:
        print_with_delay(f"{YELLOW}{line}{RESET}", delay=0.02)
        time.sleep(0.1)
    
    # Print author with dramatic pause
    time.sleep(0.5)
    print(f"\n{RED}{BOLD}{author}{RESET}")
    
    # Print some existential decorations
    print(f"\n{BLUE}{'~' * 60}{RESET}")
    print(f"{BLUE}  Existential Crisis Level: ██████████ 100%{RESET}")
    print(f"{BLUE}  Anxiety Level: ██████████████ 120%{RESET}")
    print(f"{BLUE}  Cheese Sandwich Quality: ██████░░░░ 60%{RESET}")
    print(f"{BLUE}{'~' * 60}{RESET}")
    
    # Final philosophical touch
    time.sleep(0.5)
    print(f"\n{GREEN}{BOLD}  ...and that's why I order extra pickles.  {RESET}")
    print(f"{GREEN}{BOLD}  You never know when you'll need them.  {RESET}\n")

if __name__ == "__main__":
    main()