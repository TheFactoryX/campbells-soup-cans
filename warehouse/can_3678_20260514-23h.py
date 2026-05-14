"""
Campbell's Soup Can #3678
Produced: 2026-05-14 23:11:51
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def colored_text(text, color_code=37):
    """Return text with ANSI color code"""
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03, color=37):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, border_char='█'):
    """Draw a decorative frame"""
    top_border = border_char * width
    side_border = border_char + ' ' * (width - 2) + border_char
    
    print(colored_text(top_border, 36))
    for _ in range(height):
        print(colored_text(side_border, 36))
    print(colored_text(top_border, 36))

def main():
    # Woody Allen style quote
    quote = "I tried to find meaning in life, but all I found was a dusty shelf with a half-eaten bagel and existential dread. At least the bagel was sesame."
    
    # Clear screen at start
    clear_screen()
    
    # Title
    print("\n" * 3)
    typewriter_effect("  WOODY ALLEN ON LIFE", 0.05, 35)
    print("\n" * 2)
    
    # Draw frame
    draw_frame(70, 5)
    print("\n")
    
    # Animated quote with different colors
    colors = [33, 34, 35, 36]  # Yellow, Blue, Magenta, Cyan
    color_index = 0
    
    # Add some neurotic prelude
    prelude = [
        colored_text("You know, I was up all night...", 33),
        colored_text("Thinking about... you know... things", 34),
        colored_text("Big things. Cosmic things. Bagel things.", 35),
        colored_text("\nThis is what I came up with:", 36)
    ]
    
    for line in prelude:
        print(line.center(70))
        time.sleep(1)
    
    print("\n")
    
    # Print the quote with typewriter effect
    typewriter_effect(quote, 0.02, colors[color_index % len(colors)])
    color_index += 1
    
    # Add a Woody Allen-esque signature
    print("\n" * 2)
    signature = colored_text("  - Woody Allen (probably)", 31)
    print(signature.center(70))
    
    # Add a small ASCII art Woody silhouette
    woody_silhouette = [
        "      o",
        "     /|\\",
        "     / \\",
        "   __|__",
        "  /     \\",
        " /       \\"
    ]
    
    print("\n" * 3)
    for line in woody_silhouette:
        print(line.center(70), colored_text(line, 33))
    
    # Add a final neurotic thought
    final_thought = colored_text("\nWhat if I'm not really Woody Allen? What if I'm just a simulation created by a depressed computer?", 31)
    print(final_thought.center(70))
    time.sleep(2)
    
    # Clear screen and end with a simple message
    clear_screen()
    print("\n" * 10)
    typewriter_effect(" existential dread.exe has stopped working ", 0.05, 31)
    print("\n" * 5)

if __name__ == "__main__":
    main()