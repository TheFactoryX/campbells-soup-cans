"""
Campbell's Soup Can #4001
Produced: 2026-06-24 08:33:02
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

def print_slowly(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_experience():
    # ANSI Colors
    GOLD = "\033[33m"
    CYAN = "\033[36m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # The quote
    quote = "I've spent my whole life preparing for a catastrophe that I'm now terrified is actually just a very boring Tuesday."

    # ASCII art of a neurotic-looking figure (simplified)
    art = [
        f"{GOLD}      (o_o)  {RESET}",
        f"{GOLD}      <) )>  {RESET}",
        f"{GOLD}      /  \\    {RESET}"
    ]

    # Border elements
    top_border = "╔" + "═" * 75 + "╗"
    bottom_border = "╚" + "═" * 75 + "╝"
    
    print("\n" * 2)
    
    # Animated intro
    for _ in range(3):
        sys.stdout.write(f"{CYAN}Loading existential dread... {RED}■{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"{CYAN}■{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"{CYAN}■{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        print("")

    print("\n")
    
    # Layout the masterpiece
    print(f"{BOLD}{GOLD}{top_border}{RESET}")
    
    # Center the ASCII art
    for line in art:
        print(f"{BOLD}{GOLD}║{RESET}" + line.center(73) + f"{BOLD}{GOLD}║{RESET}")
    
    print(f"{BOLD}{GOLD}╠" + "═" * 75 + "╣{RESET}")
    
    # Print the quote with a typewriter effect
    # Padding the quote to fit inside the box
    padding = " " * 3
    print(f"{BOLD}{GOLD}║{RESET}{padding}", end="")
    
    # We simulate the typewriter inside the box border
    # Since we can't easily do a typewriter inside a fixed border, 
    # we print the quote line and then close the box.
    
    print_slowly(f"{CYAN}{quote}{RESET}", delay=0.07)
    
    print(f"{BOLD}{GOLD}║{RESET}" + " " * 73 + f"{BOLD}{GOLD}║{RESET}")
    print(f"{BOLD}{GOLD}{bottom_border}{RESET}")
    
    print("\n" + f"{RED}   (Pause for dramatic sigh) {RESET}".center(77))
    time.sleep(1.5)
    print(f"{CYAN}   'Anyway, do you think the waiter likes me?'{RESET}".center(77))
    print("\n" * 2)

if __name__ == "__main__":
    try:
        woody_experience()
    except KeyboardInterrupt:
        print(f"\n{RED}Even the program gave up on existence.{RESET}")