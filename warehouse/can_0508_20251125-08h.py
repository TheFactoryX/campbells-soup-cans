"""
Campbell's Soup Can #508
Produced: 2025-11-25 08:44:02
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

def colored_text(text, color_code):
    """Print text with specified color using ANSI escape codes"""
    print(f"\033[{color_code}m{text}\033[0m", end='')
    sys.stdout.flush()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03, color=33):
    """Print text with typewriter effect"""
    for char in text:
        colored_text(char, color)
        time.sleep(delay)
    print()

def draw_line(char, length, color=37):
    """Draw a line with specified character and color"""
    colored_text(char * length, color)
    print()

def main():
    # Clear screen first
    clear_screen()
    
    # Draw top border
    draw_line('╔', 80, 36)  # Cyan
    draw_line('║', 80, 36)
    
    # Title
    colored_text("     ", 36)
    typewriter_effect("WOODY ALLEN ON LIFE AND PHILOSOPHY", 0.02, 33)  # Yellow
    
    # Draw separator
    draw_line('╟', 80, 36)
    
    # Main quote box
    colored_text("     ║", 36)
    typewriter_effect("     ", 0.01, 37)
    
    # The main quote with different colors for emphasis
    quote = "I tried to practice mindfulness once, but my mind kept wandering to the fact"
    colored_text("     ║  ", 36)
    typewriter_effect(quote, 0.02, 37)
    
    quote = "that I was probably going to die alone and be eaten by cats."
    colored_text("     ║  ", 36)
    typewriter_effect(quote, 0.02, 37)
    
    quote = "So I guess I'm more of a 'mind-full-ness' kind of guy."
    colored_text("     ║  ", 36)
    typewriter_effect(quote, 0.02, 31)  # Red for the punchline
    
    typewriter_effect("     ", 0.01, 37)
    colored_text("     ║", 36)
    
    # Draw bottom border
    draw_line('╚', 80, 36)
    draw_line('', 80, 36)
    
    # Add a small animation with ellipsis
    for i in range(3):
        time.sleep(0.5)
        colored_text("     ", 37)
        typewriter_effect("." * (i + 1), 0.1, 33)
        print("\r", end='')
    
    colored_text("     ", 37)
    typewriter_effect("- Woody Allen", 0.03, 35)  # Magenta
    
    # Final thought
    time.sleep(1)
    colored_text("\n     ", 37)
    typewriter_effect("P.S. I'm not worried about death, I just don't want to be there when it happens.", 0.02, 36)

if __name__ == "__main__":
    main()