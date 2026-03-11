"""
Campbell's Soup Can #2706
Produced: 2026-03-11 18:05:58
Worker: DeepSeek: R1 0528 (deepseek/deepseek-r1-0528)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style quote printer with visual effects

import sys
import time
import random

def print_delayed(text, delay=0.03):
    """Prints text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wobble_char(char):
    """Returns a wobbling version of a character using randomness"""
    wobble = random.randint(0, 1)
    if wobble == 0:
        return f"\033[1m{char}\033[0m"
    return char

def wobble_text(text):
    """Applies wobble effect to text"""
    return ''.join(wobble_char(c) if c.isalpha() else c for c in text)

def print_colorful_text(text, colors):
    """Prints text with cycling colors"""
    for i, char in enumerate(text):
        color_idx = i % len(colors)
        print(f"\033[{colors[color_idx]}m{char}\033[0m", end='', flush=True)
        time.sleep(0.02)
    print()

def main():
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # ANSI escape codes for colors
    colors_top = [38, 5, 166, 226, 228, 229]  # Yellow/orange spectrum
    colors_text = [93, 94, 95, 96, 97, 98]     # Bright color spectrum
    quote_colors = [91, 93, 95, 97]            # Purple/pink spectrum
    
    # Generate ASCII tree with wobble
    tree = [
        "\033[32m    _\\/_    \033[0m",
        "\033[32m     /\\     \033[0m",
        "\033[32m     /\\     \033[0m",
        "\033[32m    /  \\    \033[0m"
    ]
    
    # Print animated colorful top border
    top_border = "═" * 60
    print("\033[1m")
    print_colorful_text(f"★ {wobble_text('WOODY ALLEN INSIGHTS')} ★".center(60), colors_top)
    print("\033[0m")
    
    # Print the fancy tree
    for i, line in enumerate(tree):
        print(line.center(60))
        time.sleep(0.1)
    
    # Print quote in a wobble effect with colored text
    print()
    print("\033[34m╔" + "═" * 58 + "╗")
    print("\033[34m║\033[0m", end="")
    
    words = quote.split()
    for i, word in enumerate(words):
        if i == len(words) - 1:  # Last word
            color = random.choice(quote_colors)
            print(f'\033[{color}m {word}\033[0m', end='\033[34m ║\n\033[0m')
        else:
            color = random.choice(quote_colors)
            print(f'\033[{color}m {wobble_text(word)}\033[0m', end='')
            sys.stdout.flush()
            time.sleep(0.2)
    
    print("\033[34m╚" + "═" * 58 + "╝\033[0m")
    print()
    
    # Print trembling footer
    footer = "« Life: Not even close to being worth the anxiety »"
    chars = list(wobble_text(footer))
    for _ in range(2):
        for char in chars:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print("\r" + " " * 70, end='\r')
        time.sleep(0.5)
    
    print(wobble_text(footer).center(60))
    print()
    time.sleep(1)

if __name__ == "__main__":
    main()