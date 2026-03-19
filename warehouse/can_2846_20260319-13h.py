"""
Campbell's Soup Can #2846
Produced: 2026-03-19 13:42:44
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import math

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, color):
    corners = {
        'top_left': '╭',
        'top_right': '╮',
        'bottom_left': '╰',
        'bottom_right': '╯',
        'horizontal': '─',
        'vertical': '│'
    }
    
    # Top border
    print(colored_text(corners['top_left'] + corners['horizontal'] * width + corners['top_right'], color))
    
    # Empty lines with side borders
    for _ in range(height):
        print(colored_text(corners['vertical'] + ' ' * width + corners['vertical'], color))
    
    # Bottom border
    print(colored_text(corners['bottom_left'] + corners['horizontal'] * width + corners['bottom_right'], color))

def main():
    # Woody Allen style quote
    quote = "Life is like a bad movie - the plot is confusing, the acting is terrible, and you're desperately waiting for the popcorn to run out so you can make a dignified exit."
    
    # Animation phase 1: Typing the quote
    print("\n" * 3)
    typewriter_effect(colored_text("WOODY ALLEN ON LIFE:", '1;36'), 0.05)
    time.sleep(0.5)
    
    print("\n" * 2)
    typewriter_effect(colored_text("⌛", '33') + " " + colored_text("Preparing existential wisdom...", '90'), 0.03)
    time.sleep(1)
    
    print("\n" * 2)
    typewriter_effect(colored_text("✨", '33') + " " + colored_text("Loading neurotic insights...", '90'), 0.03)
    time.sleep(0.8)
    
    print("\n" * 3)
    
    # Calculate frame dimensions
    quote_lines = [quote[i:i+50] for i in range(0, len(quote), 50)]
    max_line_len = max(len(line) for line in quote_lines)
    frame_width = max_line_len + 4
    frame_height = len(quote_lines) + 4
    
    # Draw frame
    draw_frame(frame_width, frame_height, '1;35')
    
    # Print quote with padding and color
    print("\033[1;35m│\033[0m" + " " * ((frame_width - max_line_len) // 2) + colored_text("WOODY ALLEN:", '1;36') + " " * ((frame_width - max_line_len) // 2) + "\033[1;35m│\033[0m")
    
    for line in quote_lines:
        padding = " " * ((frame_width - len(line)) // 2)
        print("\033[1;35m│\033[0m" + padding + colored_text(line, '37') + padding + "\033[1;35m│\033[0m")
    
    print("\033[1;35m│\033[0m" + " " * ((frame_width - 20) // 2) + colored_text("- Woody Allen", '36') + " " * ((frame_width - 20) // 2) + "\033[1;35m│\033[0m")
    
    draw_frame(frame_width, frame_height, '1;35')
    
    print("\n" * 2)
    
    # Add a footer with animation
    for i in range(3):
        print(colored_text("⋆" * 30, '33'))
        time.sleep(0.2)
        print(colored_text("⋆" + " " * 28 + "⋆", '33'))
        time.sleep(0.2)
    
    print(colored_text("\n\nIf you're not terrified of life, you're not paying attention.\n", '1;37'))
    
    # Add a blinking cursor effect
    for _ in range(5):
        print(colored_text("ꙮ", '33') + " " * 5, end='\r')
        time.sleep(0.3)
        print(" " * 7, end='\r')
        time.sleep(0.3)

if __name__ == "__main__":
    main()