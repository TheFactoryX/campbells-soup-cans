"""
Campbell's Soup Can #320
Produced: 2025-11-16 17:29:57
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
import os

def typewriter(text, delay=0.03):
    """Simulate a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def woody_quote():
    # Define the quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying. It's a much simpler approach, though slightly less effective. Unless, of course, you're good at procrastination - then you might just achieve both."
    
    # ASCII art frame
    frame_top = "╔══════════════════════════════════════════════════════════════════════════════════════════════════╗"
    frame_side = "║"
    frame_bottom = "╚══════════════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'dim': '\033[2m',
        'reset': '\033[0m'
    }
    
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Print decorative top border
    print(colors['yellow'] + "╔══════════════════════════════════════════════════════════════════════════════════════════════════╗" + colors['reset'])
    
    # Print title
    title = " Woody Allen's Neurotic Wisdom "
    padding = (len(frame_top) - len(title) - 2) // 2
    print(colors['red'] + frame_side + ' ' * padding + title + ' ' * padding + frame_side + colors['reset'])
    
    # Print empty line
    print(colors['yellow'] + frame_side + ' ' * (len(frame_top) - 2) + frame_side + colors['reset'])
    
    # Print quote with typewriter effect
    quote_lines = [
        colors['cyan'] + frame_side + " " + colors['white'],
        colors['cyan'] + frame_side + " " + colors['white'] + quote,
        colors['cyan'] + frame_side + " " + colors['white'],
        colors['cyan'] + frame_side + " " * (len(frame_top) - 2) + frame_side + colors['reset']
    ]
    
    for line in quote_lines:
        typewriter(line)
        print()
    
    # Print bottom frame
    print(colors['yellow'] + frame_bottom + colors['reset'])
    
    # Add Woody Allen's signature
    time.sleep(0.5)
    signature = "- Woody Allen"
    padding = (len(frame_top) - len(signature) - 2) // 2
    print(colors['dim'] + frame_side + ' ' * padding + signature + ' ' * padding + frame_side + colors['reset'])

if __name__ == "__main__":
    woody_quote()