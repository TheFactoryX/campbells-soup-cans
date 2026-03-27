"""
Campbell's Soup Can #2993
Produced: 2026-03-27 16:06:29
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def colored_text(text, color):
    """Print text in specified color using ANSI escape codes"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def print_typewriter(text, color='white', delay=0.03):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(colored_text(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_border(width, height, color='blue'):
    """Draw a decorative border"""
    corners = {
        'top_left': '╔',
        'top_right': '╗',
        'bottom_left': '╚',
        'bottom_right': '╝',
        'horizontal': '═',
        'vertical': '║'
    }
    
    # Top border
    print(colored_text(corners['top_left'] + corners['horizontal'] * (width-2) + corners['top_right'], color))
    
    # Middle section
    for _ in range(height-2):
        print(colored_text(corners['vertical'] + ' ' * (width-2) + corners['vertical'], color))
    
    # Bottom border
    print(colored_text(corners['bottom_left'] + corners['horizontal'] * (width-2) + corners['bottom_right'], color))

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Woody Allen style philosophical quote
    quote = "I'm not afraid of death; I'm just afraid that the afterlife will be one long, awkward dinner party where I have nothing interesting to say and everyone will judge my choice of afterlife appetizers."
    
    # Title
    print_typewriter("\nWOODY ALLEN ON EXISTENTIAL DREAD\n", 'yellow', 0.02)
    
    # Draw border
    draw_border(len(quote) + 6, 7, 'cyan')
    
    # Print quote with different colors for emphasis
    print(colored_text("║", 'cyan'))
    print_typewriter("║", 'cyan')
    print_typewriter("║ ", 'cyan')
    
    # Split quote into parts for coloring
    parts = [
        ("I'm not afraid of death; ", 'red'),
        ("I'm just afraid that the afterlife will be ", 'white'),
        ("one long, awkward dinner party ", 'yellow'),
        ("where I have nothing interesting to say ", 'white'),
        ("and everyone will judge my choice of ", 'green'),
        ("afterlife appetizers.", 'magenta')
    ]
    
    # Print colored parts
    for text, color in parts:
        print_typewriter(text, color)
    
    print_typewriter(" ║", 'cyan')
    print_typewriter("║", 'cyan')
    print_typewriter("║", 'cyan')
    
    # Animated footer
    time.sleep(1)
    print_typewriter("\n...with a side of existential anxiety and a garnish of self-loathing.\n", 'green', 0.02)
    
    # ASCII art shrug
    shrug = colored_text("¯\\_(ツ)_/¯", 'cyan')
    print_typewriter("\n" + shrug + "\n", 'cyan', 0.05)

if __name__ == "__main__":
    main()