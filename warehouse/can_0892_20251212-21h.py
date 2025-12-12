"""
Campbell's Soup Can #892
Produced: 2025-12-12 21:30:50
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # ASCII art border
    border = color_text("╔═════════════════════════════════════════════════════════════════════════════════════════════╗", "36")
    bottom_border = color_text("╚═════════════════════════════════════════════════════════════════════════════════════════════╝", "36")
    
    # Woody Allen character
    woody = color_text("""
      .--.
     |o_o |
     |:_/ |
    //   \\ \
   (|     | )
  /'\_   _/`\\
   \\___)=(___/
    """, "33")
    
    # The neurotic Woody Allen quote
    quote = color_text("""
    "To be, or not to be? That was Shakespeare.
     My question is: to be, or to be another year older
     without health insurance? It's a true existential
     dilemma, especially when the pizza place asks if I
     want anchovies. Frankly, at this point, I'd rather
     face mortality than face anchovies on my pizza. It's
     a matter of principle... and indigestion."
    """, "35")
    
    # Print the animated display
    print(border)
    print(woody)
    time.sleep(1)
    
    typewriter(quote, delay=0.02)
    
    # Author attribution
    woody_signature = color_text("\n\n\t\t- Woody Allen (probably)", "34")
    typewriter(woody_signature)
    
    print(bottom_border)
    
    # Final neurotic thought
    time.sleep(1)
    final_thought = color_text("\n\nYou know, I just realized I've spent more time worrying about the meaning of life than actually living it. Figures.", "31")
    typewriter(final_thought, delay=0.05)
    
    # Small animation with ellipsis
    sys.stdout.write(color_text("\nMaybe tomorrow I'll start... ", "32"))
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print(color_text(" Nah.", "31"))

if __name__ == "__main__":
    main()