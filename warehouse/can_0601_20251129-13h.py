"""
Campbell's Soup Can #601
Produced: 2025-11-29 13:36:04
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
import random

def typewriter_effect(text, delay=0.03, color_code=""):
    """Simulate a typewriter effect with optional color"""
    for char in text:
        sys.stdout.write(color_code + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def main():
    # ANSI color codes
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
        "\033[97m",  # White
    ]
    
    # ASCII art frames
    top_border = "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    bottom_border = "╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    side_border = "║"
    
    # Woody Allen style quote
    quote = """Life is divided into two parts: the terrible and the miserable. The terrible is something like death, whereas the miserable is something like being alive."""
    
    # Clear screen and move cursor to top
    print("\033[2J\033[H", end="")
    
    # Title
    color = random.choice(colors)
    print(color + top_border + "\033[0m")
    print(color + side_border + " Woody Allen's Philosophical Musings " + side_border + "\033[0m")
    print(color + bottom_border + "\033[0m")
    
    # Animated quote box
    print("\n")
    border_color = random.choice(colors)
    text_color = random.choice([c for c in colors if c != border_color])
    
    # Top line of quote box
    print(border_color + "╔" + "═" * 80 + "╗" + "\033[0m")
    
    # Quote introduction
    print(border_color + "║" + "\033[0m" + " " * 35 + "Today's Wisdom" + " " * 34 + border_color + "║" + "\033[0m")
    print(border_color + "╠" + "═" * 80 + "╣" + "\033[0m")
    
    # Print quote with typewriter effect
    print(border_color + "║" + "\033[0m", end="")
    typewriter_effect(quote, 0.02, text_color)
    print(border_color + "║" + "\033[0m")
    
    # Bottom line of quote box
    print(border_color + "╚" + "═" * 80 + "╝" + "\033[0m")
    
    # Signature
    print("\n")
    typewriter_effect("  - Woody Allen", 0.04, border_color)
    
    # Final philosophical question
    time.sleep(1)
    print("\n")
    typewriter_effect("But what do I know? I'm just a neurotic filmmaker who talks too much.", 0.03, random.choice(colors))
    
    # Exit message
    time.sleep(2)
    print("\n")
    print(border_color + side_border + " Press any key to exit this existential crisis..." + " " * (78 - len(" Press any key to exit this existential crisis...")) + side_border + "\033[0m")
    input()
    print(border_color + bottom_border + "\033[0m")

if __name__ == "__main__":
    main()