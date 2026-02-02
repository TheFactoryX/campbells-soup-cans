"""
Campbell's Soup Can #2006
Produced: 2026-02-02 17:02:19
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os
from itertools import cycle

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_quote():
    # Define colors
    YELLOW = 33
    BLUE = 34
    RED = 31
    GREEN = 32
    PURPLE = 35
    CYAN = 36
    WHITE = 37
    
    # ASCII art frame with bagel theme
    top_border = "═════════════════════════════════════════════════════════════════════════════"
    
    # Bagel-themed ASCII art
    bagel_art = [
        "      ____   ",
        "     /    \\  ",
        "    | () |  ",
        "     \\____/  "
    ]
    
    # Woody Allen-style quote
    quote = "Life is like a bagel—hard on the outside, sometimes hollow in the middle, and best when you smear it with cream cheese and existential dread."
    
    # Author
    author = "— Woody Allen"
    
    # Animation: multiple elements
    clear_screen()
    
    # Print animated title
    title = "WOODY ALLEN'S BAGEL PHILOSOPHY"
    for i in range(len(title) + 1):
        clear_screen()
        
        # Print title
        print(colored_text(title[:i].center(70), YELLOW))
        
        # Print bagel art
        for line in bagel_art:
            print(colored_text(line.center(70), WHITE))
        
        # Print separator
        print(colored_text(top_border.center(70), BLUE))
        
        # Print partially revealed quote
        revealed_quote = quote[:i]
        print(colored_text(revealed_quote.center(70), CYAN))
        
        # Print author placeholder
        print(colored_text(" ".center(70), GREEN))
        
        time.sleep(0.03)
    
    # Continue with author animation
    for i in range(len(author) + 1):
        clear_screen()
        
        # Print title
        print(colored_text(title.center(70), YELLOW))
        
        # Print bagel art
        for line in bagel_art:
            print(colored_text(line.center(70), WHITE))
        
        # Print separator
        print(colored_text(top_border.center(70), BLUE))
        
        # Print quote
        print(colored_text(quote.center(70), CYAN))
        
        # Print partially revealed author
        revealed_author = author[:i]
        print(colored_text(revealed_author.center(70), GREEN))
        
        time.sleep(0.03)
    
    # Add animated elements
    clear_screen()
    print(colored_text(title.center(70), YELLOW))
    
    for line in bagel_art:
        print(colored_text(line.center(70), WHITE))
    
    print(colored_text(top_border.center(70), BLUE))
    print(colored_text(quote.center(70), CYAN))
    print(colored_text(author.center(70), GREEN))
    
    # Animated cream cheese smear effect
    smear_chars = cycle(["~", "*", "+", ".", "o"])
    for _ in range(20):
        smear = next(smear_chars) * 30
        print(colored_text(f" {smear}".center(70), PURPLE), end="\r")
        time.sleep(0.1)
    
    # Final message
    print("\n" + colored_text("Food for thought...".center(70), RED))

if __name__ == "__main__":
    display_quote()