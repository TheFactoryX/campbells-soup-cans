"""
Campbell's Soup Can #5242
Produced: 2026-11-14 18:02:36
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def slow_print(text, delay=0.03, color=Colors.RESET):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_border(width=70, char="═"):
    """Create a decorative border"""
    return f"{Colors.CYAN}{char * width}{Colors.RESET}"

def animate_ellipsis(text, iterations=3):
    """Animate ellipsis dots"""
    for _ in range(iterations):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r{text}{dots}   ")
            sys.stdout.flush()
            time.sleep(0.5)
    print()

def main():
    # Clear screen (works on most systems)
    print("\03c", end="")
    
    # Woody Allen style quote
    quote = (
        "I don't mind being alone. In fact, I prefer it. "
        "At least when I'm alone, I don't have to pretend "
        "to be interested in someone else's existential dread. "
        "The universe is indifferent, I'm neurotic, "
        "and my therapist is on vacation. What more do you want?"
    )
    
    # Header
    print("\n")
    print(create_border())
    print(f"{Colors.BOLD}{Colors.MAGENTA}           WOODY ALLEN'S NEUROTIC WISDOM{Colors.RESET}")
    print(create_border())
    print("\n")
    
    # Animated intro
    intro = f"{Colors.YELLOW}{Colors.BOLD}A philosophical thought by Woody Allen{Colors.RESET}"
    for i in range(3):
        sys.stdout.write(f"\r{intro}{'.' * (i+1)}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")
    
    # Print quote with typewriter effect
    slow_print(f"{Colors.GREEN}\"{quote}\"{Colors.RESET}", delay=0.02)
    
    print("\n")
    
    # Animated existential dread meter
    print(f"{Colors.RED}Existential Dread Level: ", end="")
    dread_level = random.randint(87, 99)
    for i in range(dread_level):
        sys.stdout.write(f"{Colors.RED}█{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f" {dread_level}%")
    
    # Animated footer
    print("\n")
    print(create_border())
    footer_text = "Life is full of misery, loneliness, and suffering - and it's all over much too soon."
    slow_print(f"{Colors.CYAN}{footer_text}{Colors.RESET}", delay=0.04)
    
    # Animated exit
    print("\n")
    animate_ellipsis("Press Enter to continue your existential journey", iterations=2)
    input()
    
    # Final message
    print("\n")
    print(f"{Colors.BLUE}{Colors.BOLD}Remember: The universe doesn't care about your anxiety. Neither do I.{Colors.RESET}")
    print(f"{Colors.MAGENTA}But at least you're not alone in your suffering... probably.{Colors.RESET}")
    print("\n")
    print(create_border())

if __name__ == "__main__":
    main()