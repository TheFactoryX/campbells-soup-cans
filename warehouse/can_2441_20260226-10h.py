"""
Campbell's Soup Can #2441
Produced: 2026-02-26 10:07:01
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
from itertools import cycle

def typewriter_effect(text, delay=0.05, color_code=None):
    """Simulate typewriter effect with optional color"""
    if color_code:
        sys.stdout.write(color_code)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write('\033[0m')  # Reset color
    sys.stdout.flush()

def print_woody_quote():
    # ANSI color codes
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Woody Allen ASCII portrait (simplified)
    woody = [
        "    ___________",
        "   |  O   O   |",
        "   |     ^    |",
        "   |    ---   |",
        "   |\\________/|",
        "   |  |  |  | |",
        "   |  |  |  | |",
        "   |__|__|__|_|",
        "      |  |  |",
        "     /|__|__|\\",
        "    /___|___|\\"
    ]
    
    # Quote
    quote = "I'd like to say I'm an optimist, but I'm afraid I'm not that confident in my self-assessment."
    
    # ASCII frame
    frame_top = "╔" + "═" * 70 + "╗"
    frame_bottom = "╚" + "═" * 70 + "╝"
    frame_side = "║" + " " * 70 + "║"
    
    # Print portrait
    for line in woody:
        typewriter_effect(f"{frame_side[:3]}{line}{frame_side[-3:]}\n", 0.01, BLUE)
    
    # Print top of frame
    typewriter_effect(f"\n{frame_top}\n", 0.02, YELLOW)
    
    # Print quote with typewriter effect
    typewriter_effect(frame_side + "\n", 0.01, YELLOW)
    typewriter_effect("  ", 0.01, YELLOW)
    
    # Print the quote with emphasis on certain words
    for word in quote.split():
        if word in ["optimist", "afraid"]:
            typewriter_effect(word + " ", 0.05, RED)
        elif word in ["not", "but"]:
            typewriter_effect(word + " ", 0.05, GREEN)
        else:
            typewriter_effect(word + " ", 0.03)
    
    typewriter_effect("\n", 0.01, YELLOW)
    typewriter_effect(frame_side + "\n", 0.01, YELLOW)
    
    # Print bottom of frame
    typewriter_effect(frame_bottom + "\n\n", 0.02, YELLOW)
    
    # Add a philosophical flourish
    typewriter_effect("— Woody Allen\n", 0.05, GREEN)
    
    # Add a self-deprecating footnote
    time.sleep(0.5)
    typewriter_effect("Note: This quote may or may not have been written after my analyst suggested I 'lighten up'.\n", 0.03, BLUE)

if __name__ == "__main__":
    print_woody_quote()