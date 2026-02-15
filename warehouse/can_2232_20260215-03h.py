"""
Campbell's Soup Can #2232
Produced: 2026-02-15 03:22:28
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def print_typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, border_color=36):
    """Draw a simple box with colored borders"""
    horizontal = color_text("─" * width, border_color)
    corners = color_text("┌┐└┘", border_color)
    
    # Top border
    print(color_text("┌" + "─" * (width-2) + "┐", border_color))
    
    # Empty lines
    for _ in range(height-2):
        print(color_text("│" + " " * (width-2) + "│", border_color))
    
    # Bottom border
    print(color_text("└" + "─" * (width-2) + "┘", border_color))

def main():
    # Woody Allen style quote
    quote = ("I went to see a psychic yesterday. She told me I have a great future ahead of me... \n"
             "then she asked me if I wanted to buy a used car.")
    
    # ASCII art representation of Woody Allen
    woody_art = """
   (ᵔᴥᵔ)
    /|\\
   / | \\
  /  |  \\
"""

    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title
    print_typewriter(color_text("WOODY ALLEN ON LIFE", 46), 0.03)
    print()
    
    # Draw box around quote
    draw_box(70, 8, 35)
    
    # Print quote with colors and indentation
    print(color_text("│", 35) + " " * 68 + color_text("│", 35))
    print(color_text("│", 35) + " " * 28 + color_text("❝", 33) + " " * 36 + color_text("❞", 33) + " " * 28 + color_text("│", 35))
    print(color_text("│", 35) + " " * 69 + color_text("│", 35))
    
    # Print the quote line by line with typewriter effect
    lines = quote.split('\n')
    for line in lines:
        print(color_text("│", 35) + " " * 29, end="")
        print_typewriter(line, 0.02)
        print(color_text("│", 35) + " " * 69)
    
    print(color_text("│", 35) + " " * 68 + color_text("│", 35))
    draw_box(70, 2, 35)
    
    # Print Woody Allen art
    print()
    print_typewriter(color_text(woody_art, 36), 0.001)
    print()
    
    # Footer
    print_typewriter(color_text("- Woody Allen, probably while worrying about something", 90), 0.03)
    
    # Blinking cursor at the end
    sys.stdout.write(color_text("\n\n✦ ", 93))
    sys.stdout.flush()
    for _ in range(5):
        time.sleep(0.5)
        sys.stdout.write("✦ ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("  ")
        sys.stdout.flush()
    print()

if __name__ == "__main__":
    main()