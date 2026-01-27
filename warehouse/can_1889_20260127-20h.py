"""
Campbell's Soup Can #1889
Produced: 2026-01-27 20:38:03
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def sleep_print(delay=0.03):
    time.sleep(delay)
    sys.stdout.flush()

def woody_print(text):
    print("\033[2J\033[H")  # Clear screen
    colors = ["\033[38;5;214m", "\033[0m"]
    border = "\033[38;5;153m"
    
    # Calculate box dimensions
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    
    # Top border
    print(border + "╔" + "═" * (width - 2) + "╗" + colors[0])
    
    # Text with borders
    for line in lines:
        padding = width - len(line) - 2
        print(border + "║ " + colors[0], end='')
        for char in line:
            print(char, end='')
            sleep_print(0.06 if char in ",.;" else 0.03)
        print(" " * padding + border + " ║")
    
    # Bottom border
    print(border + "╚" + "═" * (width - 2) + "╝" + colors[0])
    
    # Added flourish
    time.sleep(0.5)
    print("\n" + " " * 36 + "\033[38;5;153m⇣ (Like you needed another reason to worry)\033[0m\n")

quote = """Life is a cosmic Etch A Sketch \033[3m(tm)\033[0m where
some celestial toddler keeps shaking it
just when I start to recognize the pattern,
and honestly? I'm starting to suspect
my therapist is in on it."""

woody_print(quote)