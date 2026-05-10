"""
Campbell's Soup Can #3640
Produced: 2026-05-10 22:05:18
Worker: Owl Alpha (openrouter/owl-alpha)
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

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_effect(text, iterations=3):
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[95m', '\033[94m']
    for _ in range(iterations):
        color = random.choice(colors)
        sys.stdout.write(f'\r{color}{text}\033[0m')
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def draw_box(text, width=60):
    border = '═' * width
    print(f'\033[96m╔{border}╗')
    print(f'║\033[0m {text:^{width-2}}\033[96m ║')
    print(f'╚{border}╝\033[0m')

def main():
    # Clear screen
    print('\033[2J\033[H')
    
    # Title with glitch effect
    title = "THE PHILOSOPHICAL QUOTE GENERATOR"
    glitch_effect(title)
    time.sleep(0.5)
    
    # Draw fancy box
    print('\033[95m')
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║  🎭  Woody Allen Style Philosophical Quote Generator  🎭  ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print('\033[0m')
    time.sleep(0.3)
    
    # The quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Animated reveal
    print('\033[93m')
    slow_print("  " + "▌" * 58, 0.02)
    print('\033[0m')
    time.sleep(0.2)
    
    # The quote in a box
    draw_box(quote, 58)
    time.sleep(0.3)
    
    # Attribution
    print('\033[92m')
    attribution = "  — Woody Allen, from \"Without Feathers\" (1975)"
    slow_print(attribution, 0.04)
    print('\033[0m')
    time.sleep(0.3)
    
    # Footer
    print('\033[94m')
    footer = "  " + "▌" * 58
    slow_print(footer, 0.02)
    print('\033[0m')
    
    # Final message
    print('\033[91m')
    final = "  " + "★" * 28
    slow_print(final, 0.03)
    print('\033[0m')
    time.sleep(0.2)
    
    # Ending message
    print('\033[96m')
    ending = "  " + "~ fin ~"
    slow_print(ending, 0.05)
    print('\033[0m')
    
    # Reset
    print('\033[0m')

if __name__ == "__main__":
    main()