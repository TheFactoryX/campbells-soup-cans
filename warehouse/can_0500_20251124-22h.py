"""
Campbell's Soup Can #500
Produced: 2025-11-24 22:34:01
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

def colored_text(text, color_code):
    """Print text with specified color using ANSI escape codes."""
    return f"\033[{color_code}m{text}\033[0m"

def typewriter_effect(text, delay=0.05):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody():
    """Draw a simple ASCII art Woody Allen."""
    return r"""
     .-.
    (o o)  Woody Allen
    ==o==
     |||
    // \\
   //   \\
  //_____\\
"""

def main():
    # Color codes
    BLUE = '94'
    YELLOW = '93'
    RED = '91'
    GREEN = '92'
    
    # Quote in Woody Allen's style
    quote = "I'm not afraid of dying, I'm just afraid of not having enough time to worry about it."
    attribution = "- Woody Allen"
    
    # Print ASCII art Woody
    print(colored_text(draw_woody(), YELLOW))
    
    # Create a decorative border
    border = colored_text("─" * 60, BLUE)
    print(border)
    
    # Print the quote with typewriter effect
    typewriter_effect(colored_text("  " + quote, GREEN))
    
    # Print attribution
    typewriter_effect(colored_text("    " + attribution, RED))
    
    # Print bottom border
    print(border)
    
    # Add a neurotic footnote
    time.sleep(1)
    typewriter_effect(colored_text("\n  *Disclaimer: I wrote this quote myself. If it sounds profound, it's purely accidental.", YELLOW))

if __name__ == "__main__":
    main()