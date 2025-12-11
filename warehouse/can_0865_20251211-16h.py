"""
Campbell's Soup Can #865
Produced: 2025-12-11 16:49:11
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
from math import sin

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_box_border(width, height, color):
    print(color_text("╔" + "═" * (width - 2) + "╗", color))
    for _ in range(height):
        print(color_text("║" + " " * (width - 2) + "║", color))
    print(color_text("╚" + "═" * (width - 2) + "╝", color))

def print_centered(text, line, color, width):
    padding = (width - len(text)) // 2
    print(color_text("║" + " " * padding + text + " " * (width - len(text) - padding - 2) + "║", color))

def draw_woody():
    # Woody Allen ASCII art
    woody = [
        "    ___",
        "   /o o\\",
        "  |  >  |",
        "   \\ - /",
        "    \\./",
        "   ( Woody )",
        "    | Allen |",
        "    |______|"
    ]
    return "\n".join(woody)

def animate_quote():
    # The quote in Woody Allen's style
    quote = "I tried to be normal once. The worst ten minutes of my life. Turns out normal is just a setting on the washing machine that doesn't work very well."
    
    # Colors for different parts of the quote
    colors = [34, 36, 35, 33, 32, 31, 93]  # Blue, Cyan, Magenta, Yellow, Green, Red, Bright Yellow
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title
    print(color_text("\n\t\tWOODY ALLEN'S PHILOSOPHICAL MUSINGS\n", 91))
    
    # Animated border
    for i in range(10, 0, -1):
        print("\033[2J\033[H", end="")
        box_color = 90 + (i % 6)  # Varying gray shades
        print_box_border(70, 8, box_color)
        time.sleep(0.1)
    
    # Print the quote with colors
    words = quote.split()
    current_line = ""
    current_color = 0
    line_count = 1
    
    for word in words:
        if len(current_line) + len(word) + 1 > 60:
            print_centered(current_line, line_count, colors[current_color % len(colors)], 70)
            current_line = word
            current_color += 1
            line_count += 1
        else:
            current_line += " " + word if current_line else word
    
    # Print the last line
    if current_line:
        print_centered(current_line, line_count, colors[current_color % len(colors)], 70)
    
    # Bottom border
    print_box_border(70, 8, 90)
    
    # Print Woody Allen art
    woody_art = draw_woody()
    woody_lines = woody_art.split("\n")
    max_len = max(len(line) for line in woody_lines)
    
    print("\n")
    for i, line in enumerate(woody_lines):
        padding = (70 - max_len) // 2
        print(color_text(" " * padding + line, 90 + i % 3))
    
    # Add pulsing text
    for i in range(3):
        pulse_text = color_text("\n\n\t\"Life is full of neurosis, anxiety, and self-doubt...\"", int(90 + 5 * abs(sin(i))))
        print(pulse_text, end="", flush=True)
        time.sleep(0.5)
        print("\033[2K\033[1A", end="", flush=True)  # Clear line and move up
    
    # Final pulsing text
    final_text = color_text("\n\n\t\"Life is full of neurosis, anxiety, and self-doubt...\"", 95)
    print(final_text)

if __name__ == "__main__":
    animate_quote()