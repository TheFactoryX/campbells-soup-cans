"""
Campbell's Soup Can #1764
Produced: 2026-01-22 02:34:24
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import math

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05, color=34):
    for char in text:
        sys.stdout.write(color_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def draw_border(width, height, color=36):
    # Top border
    sys.stdout.write(color_text("╔" + "═" * (width - 2) + "╗\n", color))
    
    # Middle part
    for _ in range(height):
        sys.stdout.write(color_text("║", color) + " " * (width - 2) + color_text("║\n", color))
    
    # Bottom border
    sys.stdout.write(color_text("╚" + "═" * (width - 2) + "╝\n", color))

def animate_quote():
    # Clear screen
    sys.stdout.write("\033[H\033[J")
    
    # Title
    title = "WOODY ALLEN ON LIFE"
    sys.stdout.write("\n")
    sys.stdout.write(" " * 20 + color_text(title, 35) + "\n")
    sys.stdout.write("\n")
    
    # Animated border
    for i in range(3):
        draw_border(70, 5, 36)
        time.sleep(0.3)
        draw_border(70, 5, 32)
        time.sleep(0.3)
    
    # Main quote with typewriter effect
    quote = "I tried to find meaning in life, but I got distracted by the sale at Macy's."
    typewriter_effect(quote, 0.03, 33)
    
    quote2 = "Now I have a sweater that symbolizes my existential emptiness - 40% off!"
    typewriter_effect(quote2, 0.03, 33)
    
    # Signature with fade-in effect
    time.sleep(1)
    for i in range(5):
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.write("\n")
        sys.stdout.write(" " * 20 + color_text("WOODY ALLEN ON LIFE", 35) + "\n")
        sys.stdout.write("\n")
        
        # Draw border
        for j in range(3):
            draw_border(70, 5, 36)
            time.sleep(0.1)
            draw_border(70, 5, 32)
            time.sleep(0.1)
        
        # Quote
        sys.stdout.write(color_text(" " * 5 + quote + "\n", 33))
        sys.stdout.write(color_text(" " * 5 + quote2 + "\n", 33))
        
        # Signature with increasing opacity
        sig = " — Woody"
        sys.stdout.write("\n" * 2)
        for k in range(i + 1):
            sys.stdout.write(" " * 30 + color_text(sig, 31))
            sys.stdout.write("\n")
            time.sleep(0.1)
        
        time.sleep(0.5)
    
    # Final display
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write("\n")
    sys.stdout.write(" " * 20 + color_text("WOODY ALLEN ON LIFE", 35) + "\n")
    sys.stdout.write("\n")
    
    draw_border(70, 5, 36)
    
    sys.stdout.write(color_text(" " * 5 + quote + "\n", 33))
    sys.stdout.write(color_text(" " * 5 + quote2 + "\n", 33))
    
    sys.stdout.write("\n" * 2)
    sys.stdout.write(" " * 30 + color_text(" — Woody", 31))
    
    sys.stdout.write("\n\n\n")
    
    # Blinking cursor at the end
    for _ in range(5):
        sys.stdout.write(" " * 25 + color_text("☺", 33))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(" " * 25 + " ")
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    animate_quote()