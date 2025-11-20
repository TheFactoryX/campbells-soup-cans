"""
Campbell's Soup Can #407
Produced: 2025-11-20 18:45:14
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def colored_text(text, color_code):
    """Return text with ANSI color code applied"""
    return f"\033[{color_code}m{text}\033[0m"

def type_text(text, delay=0.02, color=None):
    """Type out text character by character with optional color"""
    if color:
        text = colored_text(text, color)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Colorful title
    type_text("WOODY ALLEN ON LIFE:", 0.05, "33")
    
    # Animated line
    for i in range(41):
        print("\r" + "-" * i, end="")
        time.sleep(0.02)
    print()
    
    # Blinking frame corners
    frame_width = len(quote) + 10
    horizontal = "═" * frame_width
    
    for _ in range(3):
        print(colored_text("╔" + horizontal + "╗", "36"))
        time.sleep(0.1)
        print(" " * (frame_width + 2))
        time.sleep(0.1)
    
    # Final frame
    print(colored_text("╔" + horizontal + "╗", "36"))
    
    # Empty space in frame
    for _ in range(2):
        print(colored_text("║" + " " * frame_width + "║", "36"))
    
    # Quote with emphasis
    type_text("  " + colored_text(quote, "35") + "  ", 0.04)
    
    # Empty space in frame
    for _ in range(2):
        print(colored_text("║" + " " * frame_width + "║", "36"))
    
    # Bottom of frame
    print(colored_text("╚" + horizontal + "╝", "36"))
    
    # Attribution
    type_text("\n                 — Woody Allen", 0.05, "32")
    
    # Final flourish
    type_text("\n" + colored_text("✦", "33") * 20, 0.01)

if __name__ == "__main__":
    main()