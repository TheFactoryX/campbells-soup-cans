"""
Campbell's Soup Can #781
Produced: 2025-12-07 20:32:56
Worker: DeepSeek: DeepSeek V3.1 Terminus (exacto) (deepseek/deepseek-v3.1-terminus:exacto)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

def print_slowly(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen"""
    print("\033[2J\033[H", end='')

def set_color(color_code):
    """Set text color using ANSI codes"""
    print(f"\033[{color_code}m", end='')

def reset_color():
    """Reset to default color"""
    print("\033[0m", end='')

def draw_neurotic_brain():
    """Draw a funny ASCII brain with neurotic vibes"""
    brain_art = [
        "         .-~~~~~~~~~-._",
        "        /      🧠     \\",
        "       |   OVERACTIVE  |",
        "       |   THINKER 9000|",
        "        \\_    ⚡    _/",
        "          `-......-'",
        "         /           \\",
        "        / EXISTENTIAL \\",
        "       /    CRISIS     \\",
        "      /    DEPARTMENT   \\"
    ]
    
    colors = [91, 93, 95, 96]  # Red, Yellow, Magenta, Cyan
    
    for i, line in enumerate(brain_art):
        set_color(colors[i % len(colors)])
        print(line)
        time.sleep(0.1)

def create_quote_box(quote, author):
    """Create a visually appealing quote box"""
    width = max(len(quote), len(author)) + 4
    
    set_color(95)  # Magenta
    print("┌" + "─" * (width + 2) + "┐")
    
    set_color(96)  # Cyan
    print("│ " + quote.center(width) + " │")
    
    set_color(93)  # Yellow
    print("│ " + " " * width + " │")
    print("│ " + f"— {author}".center(width) + " │")
    
    set_color(95)  # Magenta
    print("└" + "─" * (width + 2) + "┘")

def main():
    clear_screen()
    
    # Woody Allen style philosophical quote
    quote = "I'm not afraid of existential dread; I'm just worried my therapist will charge extra for it."
    author = "Woody Allen's Neurotic Cousin"
    
    set_color(91)  # Red
    print_slowly("\n" + "="*60)
    print_slowly("         WOODY ALLEN-STYLE PHILOSOPHICAL QUOTE GENERATOR")
    print_slowly("="*60)
    
    time.sleep(1)
    
    set_color(93)  # Yellow
    print_slowly("\nInitializing neurotic thought process...")
    
    # Fake loading animation
    for i in range(3):
        set_color(96)
        print_slowly("." * (i+1), 0.5)
    
    time.sleep(1)
    
    set_color(95)  # Magenta
    print_slowly("\nConsulting the existential crisis department...")
    
    # Animated brain
    print()
    draw_neurotic_brain()
    
    time.sleep(2)
    
    # The main quote reveal
    print("\n")
    create_quote_box(quote, author)
    
    # Additional funny commentary
    time.sleep(1)
    set_color(92)  # Green
    print_slowly("\n" + "~"*40)
    set_color(93)
    print_slowly("(This message will self-destruct in 5 seconds...)")
    
    # Countdown animation
    for i in range(5, 0, -1):
        set_color(91)
        print(f"\r{i}...", end='', flush=True)
        time.sleep(1)
    
    set_color(92)
    print("\rJust kidding! The anxiety lingers forever. 😅")
    
    reset_color()
    print_slowly("\n")

if __name__ == "__main__":
    main()