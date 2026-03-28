"""
Campbell's Soup Can #3017
Produced: 2026-03-28 20:48:37
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
from itertools import cycle

def typewriter_effect(text, delay=0.03):
    """Simulate a typewriter effect for printing text"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def colored_print(text, color_code):
    """Print text with ANSI color codes"""
    print(f"\033[{color_code}m{text}\033[0m")

def draw_box(width, height, border_char="█"):
    """Draw a decorative box around text"""
    horizontal_line = border_char * (width + 4)
    
    print(f"\033[36m{horizontal_line}\033[0m")
    for _ in range(height):
        print(f"\033[36m{border_char}  \033[0m{' ' * width}\033[36m  {border_char}\033[0m")
    print(f"\033[36m{horizontal_line}\033[0m")

def main():
    # Woody Allen-style philosophical quote
    quote = """I spent decades searching for the meaning of life,
only to discover that it's probably something like '42,'
but I'm not sure if that's the answer or just a bus route in London.
Either way, I'm probably missing my stop."""
    
    # ASCII Woody Allen caricature
    woody = """
    (O)
   /|\\
   / \\
  /___\\
"""
    
    # Color cycle for the quote
    colors = [
        33,  # Yellow
        35,  # Magenta
        36,  # Cyan
        32,  # Green
        31,  # Red
    ]
    color_cycle = cycle(colors)
    
    print("\033[2J\033[H")  # Clear screen and move cursor to top
    
    # Title
    colored_print("WOODY ALLEN ON LIFE, THE UNIVERSE, AND EVERYTHING", 33)
    print("\n")
    
    # Draw ASCII Woody
    colored_print(woody, 35)
    print("\n")
    
    # Animated quote with color cycling
    lines = quote.split('\n')
    max_line_length = max(len(line) for line in lines)
    box_height = len(lines) + 2
    
    for i in range(3):  # Animate the box appearing
        draw_box(max_line_length, box_height)
        time.sleep(0.1)
        print("\033[{}A".format(box_height + 2))  # Move cursor up
    
    # Print the quote with typewriter effect and color cycling
    for line in lines:
        if line.strip():  # Skip empty lines
            color_code = next(color_cycle)
            colored_print(f"  {line.ljust(max_line_length)}  ", color_code)
            time.sleep(0.5)
        else:
            print("  " + " " * max_line_length + "  ")
    
    draw_box(max_line_length, box_height)
    
    # Sign-off
    print("\n")
    colored_print("— Woody Allen (probably)", 34)
    colored_print("Or at least what he would have said if he were a Python program", 90)
    
    # Blinking cursor effect at the end
    for _ in range(5):
        print("\033[32m▶\033[0m ", end="", flush=True)
        time.sleep(0.3)
        print("\033[31m◀\033[0m ", end="", flush=True)
        time.sleep(0.3)

if __name__ == "__main__":
    main()