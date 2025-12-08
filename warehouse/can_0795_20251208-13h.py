"""
Campbell's Soup Can #795
Produced: 2025-12-08 13:04:21
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_quote():
    # ANSI color codes
    colors = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'ITALIC': '\033[3m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m'
    }
    
    # Woody Allen quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # ASCII art of Woody Allen with glasses
    woody = [
        "       .-.",
        "      (o o)",
        "    ,--'--',",
        "   /   :   \\",
        "  |    :    |",
        "   \\   :   /",
        "    '. : .'",
        "      '-'"
    ]
    
    # Decorative elements
    decor = [
        "    ✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧",
        "    *:･ﾟ✧*:･ﾟ✧ *:･ﾟ✧*:･ﾟ✧",
        "    ✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧"
    ]
    
    # Frame
    frame_top = "╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    frame_bottom = "╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
    frame_side = "║"
    
    # Random color scheme
    color_scheme = random.choice([
        {'intro': colors['RED'], 'contemplation': colors['YELLOW'], 'punchline': colors['GREEN'], 'frame': colors['CYAN'], 'woody': colors['BLUE'], 'decor': colors['MAGENTA']},
        {'intro': colors['BLUE'], 'contemplation': colors['MAGENTA'], 'punchline': colors['CYAN'], 'frame': colors['GREEN'], 'woody': colors['YELLOW'], 'decor': colors['RED']},
        {'intro': colors['GREEN'], 'contemplation': colors['CYAN'], 'punchline': colors['YELLOW'], 'frame': colors['MAGENTA'], 'woody': colors['RED'], 'decor': colors['BLUE']},
    ])
    
    # Print the decorative elements
    print("\n" * 2)
    for line in decor:
        type_text(color_scheme['decor'] + line.center(80) + colors['END'] + "\n")
    
    # Print the Woody Allen ASCII art
    for line in woody:
        type_text(color_scheme['woody'] + line.center(80) + colors['END'] + "\n")
    
    # Print the frame
    type_text(color_scheme['frame'] + frame_top + colors['END'] + "\n")
    
    # Print the quote with different colors for different parts
    intro = color_scheme['intro'] + "I'm not afraid of death; " + colors['END']
    contemplation = color_scheme['contemplation'] + "I just don't want to be there " + colors['END']
    punchline = color_scheme['punchline'] + "when it happens." + colors['END']
    
    type_text(frame_side + " " + colors['BOLD'] + colors['ITALIC'] + intro + colors['END'])
    type_text(frame_side + " " + colors['BOLD'] + colors['ITALIC'] + contemplation + colors['END'])
    type_text(frame_side + " " + colors['BOLD'] + colors['ITALIC'] + punchline + colors['END'] + "\n")
    
    type_text(color_scheme['frame'] + frame_bottom + colors['END'] + "\n")
    
    # Add a signature with small animation
    signature = "                                 - Woody Allen"
    type_text("\n" + colors['WHITE'])
    for char in signature:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    type_text(colors['END'] + "\n")
    
    # Blinking cursor effect
    for i in range(5):
        time.sleep(0.5)
        sys.stdout.write(" \b")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("✨\b")
        sys.stdout.flush()
    sys.stdout.write(" \b")
    sys.stdout.flush()

if __name__ == "__main__":
    clear_screen()
    print_quote()