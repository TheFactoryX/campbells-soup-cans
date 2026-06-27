"""
Campbell's Soup Can #4033
Produced: 2026-06-27 23:30:52
Worker: Poolside: Laguna XS.2 (poolside/laguna-xs.2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Wisdom Generator
Because existential dread tastes better with a side of self-deprecation.
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter_effect(text, delay=0.03, color=RESET):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def print_woody_quote():
    """Display a philosophical quote in Woody Allen's style."""
    
    # Create a decorative frame
    frame_width = 60
    
    print("\n")
    print(CYAN + "╔" + "═" * (frame_width - 2) + "╗" + RESET)
    print(CYAN + "║" + " " * (frame_width - 2) + "║" + RESET)
    
    # The quote in Woody Allen's style
    quote = "I used to think I wanted to be famous. Then I realized/famous people are just anxious neurotics like me,/only with better publicists and worse therapy bills."
    
    lines = [
        "   I used to think I wanted to be famous.",
        "   Then I realized famous people are just anxious",
        "   neurotics like me, only with better publicists",
        "   and worse therapy bills."
    ]
    
    # Print frame with quote
    for line in lines:
        padding = " " * 2
        content = padding + line + " " * (frame_width - len(line) - 4)
        print(CYAN + "║" + RESET + MAGENTA + content + CYAN + "║" + RESET)
    
    print(CYAN + "║" + " " * (frame_width - 2) + "║" + RESET)
    print(CYAN + "╚" + "═" * (frame_width - 2) + "╝" + RESET)
    
    print("\n")
    
    # Author attribution with animation
    author = "                                     — Probably Woody Allen (if he had Instagram)"
    
    print(YELLOW + "─" * 60 + RESET)
    typewriter_effect(author, delay=0.02, color=YELLOW)
    print(YELLOW + "─" * 60 + RESET)
    
    print("\n")
    
    # Additional "philosophical" footer
    footer = "💭 In my next life I want to be a penguin. They seem very satisfied with their life choices. 💭"
    print(BOLD + RED + footer.center(60) + RESET)
    print()

if __name__ == "__main__":
    print_woody_quote()