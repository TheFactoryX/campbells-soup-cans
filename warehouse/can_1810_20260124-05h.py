"""
Campbell's Soup Can #1810
Produced: 2026-01-24 05:36:39
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
import random
from itertools import cycle

def woody_allen_quote():
    # ANSI escape codes for colors
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
        '\033[97m',  # White
    ]
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # ASCII art frames
    top_frame = "╔═══════════════════════════════════════════════════════════════════════════════════════════════╗"
    bottom_frame = "╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # The quote
    quote = "I tried to find meaning in life, but it was out to lunch. So I ordered a pastrami sandwich on rye with mustard and tried not to think about the void."
    
    # Author
    author = " - Woody Allen"
    
    # Create a cycling color iterator
    color_cycle = cycle(colors)
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print top frame with typewriter effect
    frame_color = next(color_cycle)
    for char in top_frame:
        sys.stdout.write(frame_color + char + END)
        time.sleep(0.01)
    print()
    
    # Print animated quote with typewriter effect
    quote_color = next(color_cycle)
    print(quote_color + "║" + END, end=" ")
    for char in quote:
        if char in ".!,?":
            color = next(color_cycle)
            print(color + char + END, end="", flush=True)
        elif char == "I":
            print(BOLD + next(color_cycle) + char + END, end="", flush=True)
        else:
            print(next(color_cycle) + char, end="", flush=True)
        time.sleep(0.03)
    
    # Print author
    author_color = next(color_cycle)
    print(author_color + " " + UNDERLINE + next(color_cycle) + author + END)
    
    # Print bottom frame with typewriter effect
    print(quote_color + "║" + END, end=" ")
    for char in bottom_frame:
        sys.stdout.write(char + END)
        time.sleep(0.01)
    print()
    
    # Animated color transition
    for _ in range(3):
        sys.stdout.write("\033[4A")  # Move cursor up four lines
        for _ in range(4):
            print(random.choice(colors) + "║" + " " * 110 + "║" + END)
        time.sleep(0.2)
        sys.stdout.write("\033[4A")  # Move cursor up four lines
        for _ in range(4):
            print(" " * 112 + END)
        time.sleep(0.2)

if __name__ == "__main__":
    woody_allen_quote()