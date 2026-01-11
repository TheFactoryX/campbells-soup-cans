"""
Campbell's Soup Can #1547
Produced: 2026-01-11 21:30:32
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
from itertools import cycle

def typewriter_effect(text, delay=0.03, color=33):
    """Print text with typewriter effect and color"""
    sys.stdout.write(f"\033[{color}m")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()

def colored_bar(char, color, length=60):
    """Print a colored bar of characters"""
    sys.stdout.write(f"\033[{color}m{char * length}\033[0m\n")
    sys.stdout.flush()

def woody_quote():
    """Display a Woody Allen style quote with visual effects"""
    
    # Clear screen and move cursor to top
    print("\033[2J\033[H", end="")
    
    # Title
    typewriter_effect("WOODY ALLEN'S PHILOSOPHICAL MUSINGS", delay=0.02, color=35)
    
    # Top border
    colored_bar("═", 36)
    
    # Quote box
    print("\033[34m" + "║" + " " * 58 + "║\033[0m")
    print("\033[34m║" + " " * 15 + "\033[33mI'm not afraid of death; I just don't want to be there\033[34m" + " " * 10 + "║\033[0m")
    print("\033[34m║" + " " * 23 + "\033[33mwhen it happens.\033[34m" + " " * 24 + "║\033[0m")
    print("\033[34m" + "║" + " " * 58 + "║\033[0m")
    
    # Bottom border
    colored_bar("═", 36)
    
    # Author
    typewriter_effect("\n                                    — Woody Allen", delay=0.03, color=32)
    
    # Blinking cursor effect
    blink_chars = cycle(["|", "/", "-", "\\"])
    for _ in range(20):
        sys.stdout.write(f"\033[36m\n\n                                    Thinking{next(blink_chars)}\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\033[2J\033[H")
    
    # Final quote with fade-in effect
    quotes = [
        "Life is divided into the horrible and the miserable.",
        "The heart is the loneliest part of the body.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    ]
    
    # Randomly select a quote
    import random
    selected_quote = random.choice(quotes)
    
    # Fade in effect
    for opacity in range(0, 100, 5):
        print("\033[2J\033[H", end="")
        print(f"\033[38;2;{opacity};{opacity};{opacity}m" + "─" * 70 + "\033[0m")
        print("\033[38;2;{opacity};{opacity};{opacity}m" + "│" + " " * 68 + "│\033[0m")
        
        # Split quote into lines if needed
        words = selected_quote.split()
        lines = []
        current_line = []
        for word in words:
            if " ".join(current_line + [word]).length() <= 60:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))
        
        for line in lines:
            print(f"\033[38;2;{opacity};{opacity};{opacity}m" + "│" + " " * 15 + line + " " * (60 - len(line) - 15) + "│\033[0m")
        
        print("\033[38;2;{opacity};{opacity};{opacity}m" + "│" + " " * 68 + "│\033[0m")
        print(f"\033[38;2;{opacity};{opacity};{opacity}m" + "─" * 70 + "\033[0m")
        
        time.sleep(0.1)

if __name__ == "__main__":
    woody_quote()