"""
Campbell's Soup Can #97
Produced: 2025-11-06 15:35:15
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
from math import sin, pi

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_quote():
    # Colors
    YELLOW = 93
    CYAN = 96
    MAGENTA = 95
    RED = 91
    GREEN = 92
    BLUE = 94
    
    # ASCII border
    border_top = "╔═════════════════════════════════════════════════════════════════╗"
    border_bottom = "╚═════════════════════════════════════════════════════════════════╝"
    border_side = "║"
    
    # Woody Allen style quote
    quote = "To me, life is like a plate of lox without bagels - "
    quote_rest = "it's all there, but it's just not clicking together properly. "
    quote_end = "I keep searching for meaning, but all I find is cream cheese and existential dread."
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print the border and quote with animation
    for i in range(3):
        # Top border
        print(color_text(border_top, CYAN))
        
        # Animated title
        woody = "WOODY ALLEN'S PHILOSOPHY"
        title_spacing = " " * (5 + int(2 * sin(i * pi / 3)))
        print(color_text(f"{border_side}{title_spacing}{color_text(woody, YELLOW)}{title_spacing * 2}{border_side}", MAGENTA))
        
        # Empty lines
        print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
        print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
        
        # Main quote with color shifting
        quote_color = [YELLOW, CYAN, MAGENTA][i % 3]
        print(color_text(f"{border_side}      {color_text(quote, quote_color)}", GREEN))
        
        # Quote continuation with different color
        rest_color = [CYAN, MAGENTA, YELLOW][i % 3]
        print(color_text(f"{border_side}            {color_text(quote_rest, rest_color)}", GREEN))
        
        # Quote end with another color
        end_color = [MAGENTA, YELLOW, CYAN][i % 3]
        print(color_text(f"{border_side}            {color_text(quote_end, end_color)}", GREEN))
        
        # Empty lines
        print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
        print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
        
        # Signature
        signature = " - Woody Allen (probably)"
        sig_spacing = " " * (38 - len(signature) // 2)
        print(color_text(f"{border_side}{sig_spacing}{color_text(signature, RED)}{sig_spacing}{border_side}", GREEN))
        
        # Bottom border
        print(color_text(border_bottom, CYAN))
        
        # Add some delay for animation effect
        time.sleep(0.5)
        print("\033[2J\033[H", end="")
    
    # Final static display
    print(color_text(border_top, CYAN))
    print(color_text(f"{border_side}{' ' * 32}{color_text('WOODY ALLEN\\'S PHILOSOPHY', YELLOW)}{' ' * 32}{border_side}", MAGENTA))
    print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
    print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
    print(color_text(f"{border_side}      {color_text(quote, YELLOW)}", GREEN))
    print(color_text(f"{border_side}            {color_text(quote_rest, CYAN)}", GREEN))
    print(color_text(f"{border_side}            {color_text(quote_end, MAGENTA)}", GREEN))
    print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
    print(color_text(f"{border_side}{' ' * 77}{border_side}", BLUE))
    print(color_text(f"{border_side}{' ' * 38}{color_text(' - Woody Allen (probably)', RED)}{' ' * 38}{border_side}", GREEN))
    print(color_text(border_bottom, CYAN))

if __name__ == "__main__":
    print_quote()