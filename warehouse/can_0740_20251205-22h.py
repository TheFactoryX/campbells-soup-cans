"""
Campbell's Soup Can #740
Produced: 2025-12-05 22:34:23
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALIC = '\033[3m'
    PURPLE = '\033[35m'
    BACK_BLACK = '\033[40m'
    BACK_WHITE = '\033[47m'

def typewriter_effect(text, color=Colors.CYAN, delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border(width, color=Colors.YELLOW):
    """Draw a decorative border"""
    horizontal = "─" * width
    corners = "╭" + "─" * (width - 2) + "╮"
    middle = "│" + " " * (width - 2) + "│"
    bottom = "╰" + "─" * (width - 2) + "╯"
    
    print(color + corners + Colors.END)
    print(color + middle + Colors.END)
    return bottom

def main():
    # Woody Allen quote
    quote = "I tried to find meaning in life, but I got lost in the existential supermarket and all they had was expired yogurt."
    
    # Set up the visual presentation
    border_width = len(quote) + 10
    
    # Animated opening
    for i in range(3):
        sys.stdout.write(Colors.RED + "." + Colors.END)
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    
    # Title
    typewriter_effect("WOODY ALLEN ON LIFE", Colors.BOLD + Colors.PURPLE, 0.05)
    
    # Drawing border
    bottom_border = draw_border(border_width, Colors.YELLOW)
    
    # Main quote with different colors for emphasis
    sys.stdout.write(Colors.CYAN + "│ " + Colors.END)
    
    # Color different parts of the quote
    parts = [
        Colors.GREEN + "I tried to find meaning in life," + Colors.END + " ",
        Colors.BLUE + "but I got lost in the existential supermarket" + Colors.END + " ",
        Colors.RED + "and all they had was " + Colors.BOLD + Colors.YELLOW + "expired yogurt." + Colors.END
    ]
    
    for part in parts:
        sys.stdout.write(part)
        sys.stdout.flush()
    
    print(Colors.CYAN + " │" + Colors.END)
    
    # Bottom border
    print(Colors.YELLOW + bottom_border + Colors.END)
    
    # Sign-off with neurotic flourish
    time.sleep(1)
    typewriter_effect("\n...Probably.", Colors.ITALIC + Colors.RED, 0.05)
    
    # Final anxious thought
    time.sleep(0.5)
    typewriter_effect("\nWhat if I'm allergic to yogurt? Or meaning? Or both?", Colors.GREEN, 0.02)
    
    # Self-deprecating sign-off
    time.sleep(0.5)
    typewriter_effect("\n- Woody (probably overthinking it)", Colors.BOLD + Colors.UNDERLINE, 0.05)

if __name__ == "__main__":
    main()