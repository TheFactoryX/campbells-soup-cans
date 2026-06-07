"""
Campbell's Soup Can #3881
Produced: 2026-06-07 12:01:50
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

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def typewriter_effect(text, delay=0.03):
    for char in text:
        color = random.choice([Colors.YELLOW, Colors.WHITE, Colors.CYAN])
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border():
    border = "╔" + "═" * 75 + "╗"
    empty_border = "║" + " " * 75 + "║"
    return border, empty_border

def print_quote():
    quote = """I've spent my entire life searching for the meaning of existence, only to realize I should have been searching for a good parking spot. It's all very existential, really. And by that, I mean it's all very frustrating."""
    
    # Draw border
    border, empty_border = draw_border()
    
    print(f"\n{Colors.CYAN}{border}")
    print(empty_border)
    
    # Print quote with typewriter effect
    sys.stdout.write(f"{Colors.WHITE}║{Colors.YELLOW}   ")
    typewriter_effect(quote, delay=0.02)
    sys.stdout.write(f"{Colors.WHITE}║")
    
    print(empty_border)
    print(f"{Colors.CYAN}{border}{Colors.END}")
    print(f"\n{Colors.BOLD}{Colors.GREEN}                                 - Woody Allen{Colors.END}\n")

if __name__ == "__main__":
    # Initial animation
    for i in range(3):
        print(f"{Colors.YELLOW}." * (i+1) + " " * (3-i) + f"{Colors.YELLOW}." * (i+1))
        time.sleep(0.3)
    
    print_quote()