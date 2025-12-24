"""
Campbell's Soup Can #1137
Produced: 2025-12-24 02:22:38
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
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

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

def print_typewriter(text, delay=0.05, color='white'):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_heart():
    """Draw a simple ASCII heart"""
    heart = [
        "   ***     ***   ",
        " *****   *****  ",
        "******* ******* ",
        " *************  ",
        "  ***********   ",
        "   *********    ",
        "    *******     ",
        "     *****      ",
        "      ***       ",
        "       *        "
    ]
    
    for line in heart:
        print(f"{COLORS['red']}{line}{COLORS['reset']}")
        time.sleep(0.1)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Title sequence
    print(f"\n{COLORS['magenta']}{COLORS['bold']}")
    print("╔══════════════════════════════════════════════════╗")
    print("║           WOODY ALLEN PHILOSOPHY                 ║")
    print("║         (The Neurotic Edition)                   ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{COLORS['reset']}")
    
    # Draw a heart with the quote inside
    print(f"\n{COLORS['yellow']}{COLORS['bold']}Your Daily Dose of Existential Dread:{COLORS['reset']}\n")
    
    # The heart animation
    draw_heart()
    
    # The quote with a neurotic Woody Allen flair
    quote = "I'm not afraid of death; I'm afraid of dying in traffic while worrying about my cholesterol."
    
    print(f"\n{COLORS['cyan']}{COLORS['bold']}")
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                    ║")
    
    # Print quote with typewriter effect
    print("║  ", end="")
    print_typewriter(quote, 0.08, 'white')
    print("║                                                    ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{COLORS['reset']}")
    
    # Signature
    print(f"\n{COLORS['magenta']}{COLORS['bold']}— Woody Allen (probably written on a napkin in a deli){COLORS['reset']}")
    
    # Add some neurotic blinking text at the bottom
    print(f"\n{COLORS['yellow']}{COLORS['bold']}[Blinking Neurotically...]{COLORS['reset']}")
    
    # Quick blink effect
    for _ in range(3):
        print(f"{COLORS['red']}WORRY{COLORS['reset']}", end=" ")
        time.sleep(0.3)
        print(f"{COLORS['blue']}WORRY{COLORS['reset']}", end=" ")
        time.sleep(0.3)
        print(f"{COLORS['green']}WORRY{COLORS['reset']}", end=" ")
        time.sleep(0.3)
        print("   ", end="\r")
    
    print(f"\n{COLORS['white']}Life is short. Worry about it. {COLORS['reset']}")

if __name__ == "__main__":
    main()