"""
Campbell's Soup Can #3183
Produced: 2026-04-07 21:03:59
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, color_code='\033[0m', delay=0.05):
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote():
    # ASCII art frame
    frame_top = "╔════════════════════════════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚════════════════════════════════════════════════════════════════════════════════════╝"
    
    # Woody Allen silhouette
    woody = [
        "    o    ",
        "   /|\\   ",
        "   / \\   ",
        "  /   \\  ",
        " /_____\\ ",
        "|       |",
        "|  ???  |",
        "|_______|"
    ]
    
    # Color codes
    blue = '\033[94m'
    yellow = '\033[93m'
    red = '\033[91m'
    green = '\033[92m'
    purple = '\033[95m'
    cyan = '\033[96m'
    reset = '\033[0m'
    
    # The Woody Allen quote
    quote = "I tried to be a philosopher, but I kept getting distracted by my own neurosis. "
    quote += "It's like trying to meditate in a room full of anxious thoughts who've all decided "
    quote += "to have a party at the same time."
    
    # Clear screen
    clear_screen()
    
    # Print frame top
    print(f"{blue}{frame_top}{reset}")
    
    # Print title
    print(f"{blue}║{reset} {purple}WOODY ALLEN ON PHILOSOPHY{reset} {blue}║{reset}")
    
    # Print empty line
    print(f"{blue}║{reset}" + " " * 78 + f"{blue}║{reset}")
    
    # Print Woody silhouette
    for line in woody:
        print(f"{blue}║{reset} {cyan}{line}{reset} {blue}║{reset}")
    
    # Print empty line
    print(f"{blue}║{reset}" + " " * 78 + f"{blue}║{reset}")
    
    # Print quote with typewriter effect
    print(f"{blue}║{reset} ", end="")
    typewriter_effect(quote, yellow, 0.03)
    print(f"{blue}║{reset}" + " " * 78 + f"{blue}║{reset}")
    
    # Print footer
    print(f"{blue}║{reset} {red}\"Life is just one neurotic thought away from enlightenment\"{reset} {blue}║{reset}")
    
    # Print frame bottom
    print(f"{blue}{frame_bottom}{reset}")
    
    # Add animated musical notes
    print("\n")
    for _ in range(3):
        print(f"{green}♪{reset} {red}♫{reset}", end="\r")
        time.sleep(0.5)
        print(f"{red}♫{reset} {green}♪{reset}", end="\r")
        time.sleep(0.5)
    print("\n")

if __name__ == "__main__":
    print_quote()