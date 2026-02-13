"""
Campbell's Soup Can #2194
Produced: 2026-02-13 07:14:54
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_quote.py - A visually interesting Woody Allen style philosophical quote

import time
import sys

# ANSI escape codes for colors and styles
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"

# Woody Allen style quote
quote = (
    "I don't want to achieve immortality through my work;\n"
    "I want to achieve it through not dying.\n\n"
    "- Woody Allen"
)

# ASCII art border
border = (
    "╔═══════════════════════════════════════════════════════╗\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "║                                                       ║\n"
    "╚═══════════════════════════════════════════════════════╝"
)

def print_colored(text, color):
    """Print text in specified color"""
    print(color + text + END)

def animate_quote(quote, border):
    """Animate the quote appearing with a border"""
    print_colored(border, YELLOW)
    
    # Split the quote into lines
    lines = quote.split("\n")
    
    # Position to start printing the quote (row 2, column 5)
    row = 2
    col = 5
    
    # Clear the screen
    print("\033[H\033[J", end="")
    
    # Print the border
    print_colored(border, YELLOW)
    
    # Animate each line of the quote
    for line in lines:
        # Move cursor to the correct position
        print(f"\033[{row};{col}H", end="")
        
        # Print each character with a small delay
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.02)
        
        # Move to the next line
        row += 1
        print()
        time.sleep(0.1)
    
    # Wait a bit before exiting
    time.sleep(2)

if __name__ == "__main__":
    animate_quote(quote, border)