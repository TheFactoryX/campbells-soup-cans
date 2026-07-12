"""
Campbell's Soup Can #4168
Produced: 2026-07-12 09:15:50
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Woody Allen‑style quote (one line)
quote = "I asked the universe for a sign, and it gave me a parking ticket."

def typewriter(text, delay=0.05, color=WHITE):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def print_boxed_quote():
    width = len(quote) + 4  # padding inside the box
    top_bottom = f"{CYAN}+{'-' * width}+{RESET}"
    sides = f"{CYAN}|{RESET}"
    
    # Animate the box drawing
    print(top_bottom)
    time.sleep(0.1)
    print(sides + " " * width + sides)
    time.sleep(0.1)
    
    # Typewriter effect for the quote line, centered
    padded_line = " " + quote + " "
    sys.stdout.write(sides)
    typewriter(padded_line, delay=0.07, color=YELLOW + BOLD)
    sys.stdout.write(sides + "\n")
    time.sleep(0.1)
    
    print(sides + " " * width + sides)
    time.sleep(0.1)
    print(top_bottom)

if __name__ == "__main__":
    print_boxed_quote()