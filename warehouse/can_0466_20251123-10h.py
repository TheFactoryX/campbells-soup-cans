"""
Campbell's Soup Can #466
Produced: 2025-11-23 10:33:54
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
    """Print text with ANSI color code"""
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gradient_text(text, start_color=31, end_color=36, steps=10):
    """Print text with a color gradient effect"""
    for i, char in enumerate(text):
        progress = i / len(text)
        color = int(start_color + (end_color - start_color) * progress)
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def draw_frame(width=70, height=15):
    """Draw an ASCII art frame"""
    # Top border with gradient
    print(colored_text("╔" + "═" * (width-2) + "╗", 36))
    
    # Side borders
    for _ in range(height-2):
        print(colored_text("║" + " " * (width-2) + "║", 36))
    
    # Bottom border
    print(colored_text("╚" + "═" * (width-2) + "╝", 36))

def typewriter_effect(text, delay=0.05):
    """Print text character by character with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    clear_screen()
    
    # Title
    title = colored_text("WOODY ALLEN ON EXISTENCE", 33)
    print("\n" * 3)
    print(title.center(70))
    print("\n" * 2)
    
    # Draw initial frame
    draw_frame()
    
    # Print the quote with typewriter effect
    quote = "To be or not to be? That is the question. But I've already decided to be, mostly because not being seems like such a hassle with all the paperwork and the DMV waiting lines."
    
    # Position for the quote (centered in the frame)
    print("\n" * 4)
    typewriter_effect(quote.center(60))
    
    # Add Woody Allen's signature
    print("\n" * 3)
    signature = colored_text("- Woody Allen", 35)
    print(signature.center(60))
    
    # Add a philosophical flourish
    print("\n" * 2)
    flourish = "Also, I'm pretty sure there's no Wi-Fi in the afterlife."
    print_gradient_text(flourish.center(60), 35, 33)
    
    # Blinking cursor effect
    while True:
        sys.stdout.write(colored_text("\n\n\t> ", 32))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b\b\b\b    \b\b\b\b")
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    main()