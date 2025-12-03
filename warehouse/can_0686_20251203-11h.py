"""
Campbell's Soup Can #686
Produced: 2025-12-03 11:30:29
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def color_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def woody_allen_quote():
    # Clear screen
    clear_screen()
    
    # Title with ASCII art
    title = " WOODY ALLEN'S PHILOSOPHICAL MUSINGS "
    border = "+" + "-" * (len(title) - 2) + "+"
    
    # Print title with colors
    color_print(border, "36")
    print()
    color_print(f"|{title}|", "35;1")
    print()
    color_print(border, "36")
    print()
    
    # The philosophical quote
    quote = "To be or not to be? That is the question. But honestly, I'd rather be in bed with a good book and a bad movie. At least then I know what I'm getting into."
    
    # Animated color transition for the quote
    colors = cycle(["31", "32", "33", "34", "35", "36"])
    words = quote.split()
    
    print()
    print(" " * 5 + "❝", end='')
    time.sleep(0.2)
    
    for i, word in enumerate(words):
        color_print(" " + word, next(colors))
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(" ❝", end='')
    time.sleep(0.2)
    print("\n")
    
    # Footer with ASCII art
    footer = "+" + "-" * (len(title) - 2) + "+"
    color_print(footer, "36")
    
    # Animated attribution
    time.sleep(1)
    print("\n")
    attribution = [
        "     - Woody Allen",
        "     (Probably overthinking this too)",
        "     " + "─" * 20,
        "     Existential crisis: $19.99",
        "     Therapy not included"
    ]
    
    for line in attribution:
        color_print(line, "31" if line.startswith("     -") else "32")
        time.sleep(0.5)
    
    # Another small animation
    time.sleep(1)
    print("\n")
    color_print("Press Ctrl+C to exit...", "33")
    try:
        time.sleep(10)  # Wait 10 seconds before clearing
    except KeyboardInterrupt:
        clear_screen()

if __name__ == "__main__":
    woody_allen_quote()