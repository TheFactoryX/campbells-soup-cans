"""
Campbell's Soup Can #4952
Produced: 2026-09-12 22:18:40
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

def neurotic_typewriter(text, delay=0.04):
    """Prints text character by character with chaotic neurotic colors."""
    for char in text:
        # Randomly pick a color to simulate a neurotic mind
        color = random.choice([RED, YELLOW, GREEN, CYAN, MAGENTA])
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    
    # Blinking underscore cursor at the end
    for _ in range(4):
        sys.stdout.write(BOLD + YELLOW + "_" + RESET)
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\b" + " " + "\b") # Erase the underscore
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write(" ") # Final space for clean spacing

def print_brain():
    """Prints a simple ASCII art brain."""
    art = """
              _....._
             /       \\
            |  O   O  |
             \\  ><  /
              \\  __ /
               \\/  \\/
               (_____)
    """
    print(BLUE + art + RESET)

def main():
    # Title with a flashy border
    border = BOLD + RED + "***" + YELLOW + " WOODY'S EXISTENTIAL ANXIETY " + RED + "***" + RESET
    print(f"\n\n{border}\n")
    
    # Print the neurotic brain
    print_brain()
    time.sleep(0.5)

    # The Woody Allen style philosophical quote
    quote = (
        "I'm not afraid of death; "
        "I just don't want to be there when it happens. "
        "Unless there's a decent restaurant on the other side."
    )
    
    print(f"\n{DIM}--- Neuronal Output ---{RESET}\n")
    neurotic_typewriter(quote)
    
    print(f"\n\n{DIM}--- End of Transmission ---{RESET}\n")

if __name__ == "__main__":
    main()