"""
Campbell's Soup Can #1923
Produced: 2026-01-29 11:46:22
Worker: Arcee AI: Trinity Mini (free) (arcee-ai/trinity-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # Woody Allen style quote
    quote = """
    I don't want to achieve immortality through my work; I want to achieve it through not dying.
    """
    
    # ANSI color codes
    RED = "\033[31m"
    RESET = "\033[0m"
    
    # ASCII art brain
    brain = """
        .-""-.
       /  O  O  \
      |   .-.   |
       \  `-'  /
        `-^-' 
    """
    
    # Print the brain art
    print(RED + brain + RESET)
    
    # Print the quote inside a colored box
    print(RED + "  " + "="*30 + "  ")
    print(RED + "  " + "| " + quote.strip() + " |" + RESET)
    print(RED + "  " + "="*30 + "  " + RESET)

if __name__ == "__main__":
    main()