"""
Campbell's Soup Can #3588
Produced: 2026-05-06 22:08:34
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.02, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def print_colorful_quote():
    # ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'dim': '\033[2m',
        'italic': '\033[3m',
        'underline': '\033[4m',
        'reset': '\033[0m'
    }
    
    # Woody Allen style quote
    quote = "I've spent so much time worrying about the meaning of life that I've forgotten to actually live it. I suppose that's my contribution to existential philosophy - proving that you can think yourself out of existence."
    
    # Create a dramatic reveal
    clear_screen()
    
    # ASCII art border
    border_top = "╔════════════════════════════════════════════════════════════════════════════════════════╗"
    border_bottom = "╚════════════════════════════════════════════════════════════════════════════════════════╝"
    
    # Print border with animation
    typewriter_effect(colors['cyan'] + border_top + colors['reset'], 0.01)
    
    # Print quote with color coding and animation
    typewriter_effect(colors['cyan'] + "║" + colors['reset'], 0.01)
    typewriter_effect("  ", 0.01)
    
    # Split quote into parts for color coding
    quote_parts = [
        ("I've spent so much time worrying about the meaning of life", colors['yellow']),
        ("that I've forgotten to actually live it.", colors['red']),
        ("I suppose that's my contribution to existential philosophy", colors['green']),
        ("-", colors['white']),
        ("proving that you can think yourself out of existence.", colors['magenta'])
    ]
    
    for i, (part, color) in enumerate(quote_parts):
        typewriter_effect(color + part + colors['reset'], 0.03)
        if i < len(quote_parts) - 1:
            typewriter_effect(" ", 0.01)
    
    typewriter_effect("\n" + colors['cyan'] + "║" + colors['reset'], 0.01)
    
    # Print border bottom
    typewriter_effect(colors['cyan'] + border_bottom + colors['reset'], 0.01)
    
    # Print author with animation
    typewriter_effect("\n", 0.1)
    typewriter_effect(colors['green'] + "─" * 70 + colors['reset'], 0.01)
    
    # Blinking author name
    for _ in range(3):
        typewriter_effect(colors['green'] + "│" + colors['white'] + "  Woody Allen  " + colors['green'] + "│" + colors['reset'], 0.02)
        time.sleep(0.3)
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
        typewriter_effect(colors['green'] + "│" + colors['yellow'] + "  Woody Allen  " + colors['green'] + "│" + colors['reset'], 0.02)
        time.sleep(0.3)
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
    
    typewriter_effect(colors['green'] + "─" * 70 + colors['reset'], 0.01)
    
    # Add a philosophical flourish
    typewriter_effect("\n", 0.1)
    typewriter_effect(colors['dim'] + "    (Don't think too hard about this... or anything else for that matter.)" + colors['reset'], 0.02)

if __name__ == "__main__":
    print_colorful_quote()