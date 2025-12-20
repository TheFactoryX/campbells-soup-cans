"""
Campbell's Soup Can #1057
Produced: 2025-12-20 10:35:06
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def typewriter(text, delay=0.03, color_code=None, end='\n'):
    """Print text with typewriter effect and optional color"""
    if color_code:
        sys.stdout.write(color_code)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if color_code:
        sys.stdout.write("\033[0m")  # Reset color
    sys.stdout.write(end)

def display_quote():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title with dramatic effect
    typewriter("WOODY ALLEN ON EXISTENTIALISM", delay=0.02, color_code="\033[1;4;36m")  # Bold, underlined, cyan
    print("\n")
    
    # Create a decorative frame with gradient
    frame_colors = ["\033[0;33m", "\033[0;36m", "\033[0;35m"]  # Yellow, cyan, magenta
    quote_color = "\033[1;37m"  # Bright white
    signature_color = "\033[3;35m"  # Italic purple
    reset_color = "\033[0m"
    
    # Top border with gradient
    for i in range(55):
        color_index = min(i // 18, len(frame_colors) - 1)
        sys.stdout.write(frame_colors[color_index] + "═" + reset_color)
    sys.stdout.write("\n")
    
    # Left border with space
    sys.stdout.write(frame_colors[0] + "║" + reset_color + " ")
    
    # Quote with typewriter effect
    quote = "I tried to be a nihilist, but I couldn't get past the paperwork, "
    quote += "and anyway, what's the point of not believing in anything if you just "
    quote += "end up being depressed about it?"
    
    typewriter(quote, delay=0.02, color_code=quote_color)
    
    # Right border
    sys.stdout.write(" " + frame_colors[-1] + "║" + reset_color + "\n")
    
    # Bottom border with gradient
    for i in range(55):
        color_index = min(i // 18, len(frame_colors) - 1)
        sys.stdout.write(frame_colors[color_index] + "═" + reset_color)
    sys.stdout.write("\n")
    
    # Signature
    print("\n")
    typewriter("- Woody Allen", delay=0.02, color_code=signature_color)
    
    # Closing thought in Woody Allen's voice
    print("\n")
    typewriter("You know, I once thought about writing a book on procrastination.", 
               delay=0.02, color_code="\033[0;36m")
    typewriter("But I haven't gotten around to it yet.", 
               delay=0.02, color_code="\033[0;36m")
    typewriter("The deadline is eternal, which is both comforting and terrifying.", 
               delay=0.02, color_code="\033[0;36m")

if __name__ == "__main__":
    display_quote()