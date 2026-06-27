"""
Campbell's Soup Can #4032
Produced: 2026-06-27 22:16:01
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter effect and a specific color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def animate_glasses():
    """A little ASCII animation of neurotic glasses blinking."""
    frames = [
        "  👓  ", 
        "  🕶️  ", 
        "  👓  "
    ]
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r\033[33m{frame} (Thinking about the void...)\033[0m")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")

def main():
    # Colors
    C_BOLD = "\033[1m"
    C_CYAN = "\033[36m"
    C_YELLOW = "\033[33m"
    C_RED = "\033[31m"
    C_RESET = "\033[0m"

    # The Quote
    quote = "I've decided that the secret to a happy life is to maintain a healthy balance between complete existential terror and the hope that there might be a really great deli around the corner."
    author = "- Woody (probably)"

    # Border
    border_char = "◈"
    width = len(quote) + 4
    
    print("\n")
    animate_glasses()
    
    # Visual Frame
    print(f"{C_CYAN}{border_char * (width // 2 + 10)}{C_RESET}")
    print(f"{C_CYAN}{border_char}{C_RESET} ", end="")
    
    # Typing the quote
    typewriter(quote, delay=0.06, color=C_BOLD + C_YELLOW)
    
    print(f"{C_CYAN}{border_char}{C_RESET}")
    print(f"{C_CYAN}{border_char * (width // 2 + 10)}{C_RESET}")
    
    time.sleep(0.5)
    print(f"\n{C_RED}    {author}{C_RESET}")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31m(Panics and leaves the room)\033[0m")