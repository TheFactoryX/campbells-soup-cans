"""
Campbell's Soup Can #3102
Produced: 2026-04-03 05:50:05
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

def typewriter_effect(text, delay=0.03, color_code=None):
    for char in text:
        if color_code:
            sys.stdout.write(color_code)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m')  # Reset color
    sys.stdout.flush()

def print_quote():
    # Define colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reset': '\033[0m'
    }
    
    # ASCII art border
    border = colors['cyan'] + "╔" + "═" * 70 + "╗" + colors['reset']
    side = colors['cyan'] + "║" + colors['reset']
    
    print("\n")
    print(border)
    print(side + " " * 70 + side)
    
    # Title
    typewriter_effect(side + " " * 25 + colors['yellow'] + "WOODY ALLEN ON EXISTENCE" + colors['reset'] + " " * 25 + side, 0.03)
    print("\n" + side + " " * 70 + side)
    
    # Main quote with typewriter effect
    quote = "I spend so much time analyzing my life, I forget to actually live it. "
    typewriter_effect(side + " " + colors['white'] + quote, 0.03, colors['bold'])
    
    quote2 = "It's like being at the movies and spending the entire film analyzing the "
    typewriter_effect(quote2, 0.03, colors['white'])
    
    quote3 = "projector quality instead of watching the film. And then I worry that I'm "
    typewriter_effect(quote3, 0.03, colors['white'])
    
    quote4 = "wasting time worrying about not living, which means I'm not living even more... "
    typewriter_effect(quote4, 0.03, colors['white'])
    
    quote5 = "which makes me want to have a cigarette, even though I don't smoke."
    typewriter_effect(quote5 + " " * (70 - len(quote5)) + side, 0.03, colors['white'])
    
    print("\n" + side + " " * 70 + side)
    
    # Neurotic footer
    typewriter_effect(side + " " * 20 + colors['magenta'] + "~ Existentially yours, Woody ~" + colors['reset'] + " " * 20 + side, 0.03)
    print("\n" + side + " " * 70 + side)
    print(border)
    print("\n")
    
    # Animated existential crisis
    for i in range(5):
        dots = "." * (i + 1)
        sys.stdout.write(colors['red'] + "Is life just a series of anxieties waiting to happen" + dots + " \r")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n" + colors['green'] + "Or maybe I'm overthinking it." + colors['reset'] + "\n")

if __name__ == "__main__":
    print_quote()