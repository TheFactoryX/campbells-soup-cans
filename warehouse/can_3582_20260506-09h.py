"""
Campbell's Soup Can #3582
Produced: 2026-05-06 09:36:33
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_face():
    print(colored_text("""
    
    (°_o)
    /|\\
    / \\""", "33"))
    time.sleep(0.5)

def draw_thought_bubble():
    print(colored_text("""
    
     .-""-.
    /      \\
   |  O O  |
   |   ^   |
    \\  --- /
     `-----'
        |
       /|\\
      / | \\
         |
    """, "36"))
    time.sleep(0.5)

def main():
    clear_screen()
    
    # Title
    print(colored_text("THE WOODY ALLEN PHILOSOPHY", "35"))
    print(colored_text("=" * 30, "35"))
    time.sleep(1)
    
    # Draw Woody's face
    draw_face()
    
    # Draw thought bubble
    draw_thought_bubble()
    
    # The philosophical quote
    quote = "I've spent my entire life worrying about the meaning of existence, only to realize I should have been worrying about my mortgage payments."
    
    # Present the quote with typewriter effect
    print("\n")
    typewriter_effect(colored_text(quote, "33"), 0.02)
    
    # Add a dramatic pause
    time.sleep(2)
    
    # Woody's signature style follow-up
    print("\n")
    typewriter_effect(colored_text("...and now I'm late for therapy.", "31"), 0.03)
    
    # Add a final philosophical note
    time.sleep(1)
    print("\n")
    typewriter_effect(colored_text("It's tough being a neurotic genius.", "32"), 0.03)
    
    # End with a flourish
    time.sleep(1)
    print("\n" + colored_text("THE END", "35"))
    print(colored_text("¯" * 8, "35"))

if __name__ == "__main__":
    main()