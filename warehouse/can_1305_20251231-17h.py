"""
Campbell's Soup Can #1305
Produced: 2025-12-31 17:33:20
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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
import random

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def typewriter(text, color=37, delay=0.03):
    for char in text:
        sys.stdout.flush()
        time.sleep(delay)
        print_color(char, color)
    print()

def animate_emojis():
    emojis = [" 😰", " 😅", " 🤔", " 😬"]
    for _ in range(8):
        time.sleep(0.2)
        print_color(random.choice(emojis), 93)
        sys.stdout.flush()

def main():
    # Clear screen
    print("\033[2J\033[H", end='')
    
    # ASCII frame
    print_color("╔" + "═"*58 + "╗\n", 36)
    print_color("║", 36)
    print_color(" " * 58, 30)
    print_color("║\n", 36)
    
    # Quote
    print_color("║  ", 36)
    typewriter("My therapist says I suffer from existential FOMO -", 96)
    print_color("║  ", 36)
    typewriter("I keep worrying there might be a better meaning of", 96)
    print_color("║  ", 36)
    typewriter("life happening somewhere else without me.          ", 96)
    
    # Subtitle with style
    print_color("║", 36)
    print_color(" " * 58, 30)
    print_color("║\n", 36)
    print_color("║  ", 36)
    print_color("          (from 'Midnight Crises in Manhattan')", 90)
    print()
    
    # Bottom frame
    print_color("║", 36)
    print_color(" " * 58, 30)
    print_color("║\n", 36)
    print_color("╚" + "═"*58 + "╝\n", 36)
    
    # Animated reaction
    print("\n")
    print("                        ", end='')
    animate_emojis()
    print("\n")

if __name__ == "__main__":
    main()