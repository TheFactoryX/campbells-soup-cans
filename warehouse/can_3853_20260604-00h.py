"""
Campbell's Soup Can #3853
Produced: 2026-06-04 00:01:02
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
import random

def color_text(text, color_code):
    """Apply color to text using ANSI escape codes"""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.03, color=0):
    """Print text character by character with a typewriter effect"""
    if color != 0:
        sys.stdout.write(color_text("", color))
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if color != 0:
        sys.stdout.write("\033[0m")
    
    sys.stdout.write("\n")
    sys.stdout.flush()

def print_frame(lines, width=70):
    """Print a decorative frame around the text"""
    # ASCII art borders
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"
    side_border = "║"
    
    # Print top border
    print(color_text(top_border, 33))
    
    # Print lines with padding
    for i, line in enumerate(lines):
        padding = (width - len(line)) // 2
        if i == 0:  # Title
            color = 35
        elif i == len(lines) - 1:  # Author
            color = 34
        elif line:  # Quote
            color = 36
        else:  # Empty lines
            color = 0
        
        print(color_text(f"{side_border}{' ' * padding}{line}{' ' * (width - len(line) - padding - 2)}{side_border}", color))
    
    # Print bottom border
    print(color_text(bottom_border, 33))

def woody_ascii():
    """Simple ASCII art of Woody Allen"""
    woody = [
        "    o o o",
        "   o     o",
        "  o  >_<  o",
        " o  -___-  o",
        "o   o   o   o",
        " \       / ",
        "  '-----'  ",
        "    | | |",
        "   -----"
    ]
    
    for line in woody:
        typewriter_effect(line, 0.01, 32)

def neurotic_thinking():
    """Create a neurotic thinking animation"""
    thoughts = [
        "What if this quote isn't profound enough?",
        "Should I have worn a turtleneck today?",
        "What if death comes while I'm printing this?",
        "I think I left the stove on..."
    ]
    
    for thought in thoughts:
        sys.stdout.write(f"\r{color_text(thought, 35)}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.7))
    
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()

def blink_cursor(times=5, delay=0.5):
    """Create a blinking cursor effect"""
    for _ in range(times):
        sys.stdout.write(color_text("█", 32))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Woody Allen style quote
    quote = """
    I tried to be a philosopher, but I kept getting distracted 
    by the existential dread of my own existence. It's like trying 
    to solve the meaning of life while simultaneously worrying 
    about whether I remembered to turn off the iron.
    """
    
    # Title and author
    title = "A MOMENT OF CLARITY"
    author = "- Woody Allen"
    
    # Create lines for the frame
    lines = [title.strip(), "", quote.strip(), "", author.strip()]
    
    # Print the ASCII art of Woody Allen
    woody_ascii()
    print("\n")
    
    # Neurotic thinking
    neurotic_thinking()
    print("\n")
    
    # Print the quote with typewriter effect
    typewriter_effect("Ah! Here it is...", 0.05, 35)
    time.sleep(1)
    
    # Print the framed quote
    print_frame(lines)
    
    # Add a little flourish at the end
    print("\n")
    typewriter_effect("...and I probably left the iron on.", 0.03, 31)
    
    # Blinking cursor effect
    print("\n")
    blink_cursor()
    
    # Final thought
    time.sleep(1)
    typewriter_effect("Or was it the stove? I can never remember.", 0.03, 33)
    
    # Signature
    print("\n")
    typewriter_effect("xoxo, Woody", 0.05, 34)
    print(color_text("PS: I'm not really Woody. I just play him on the internet.", 35))

if __name__ == "__main__":
    main()