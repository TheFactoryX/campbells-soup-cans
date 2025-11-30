"""
Campbell's Soup Can #621
Produced: 2025-11-30 11:26:36
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def clear_screen():
    print("\033[2J\033[H", end="")

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border():
    print("\033[38;5;214m" + "=" * 60 + "\033[0m")

def print_woody_quote():
    clear_screen()
    
    # Top of frame
    print("\033[38;5;214m" + "┌" + "─" * 58 + "┐\033[0m")
    
    # Empty line
    print("\033[38;5;214m│\033[0m" + " " * 58 + "\033[38;5;214m│\033[0m")
    
    # Quote text with typewriter effect
    quote = "\033[38;5;220mI'm not afraid of death; I just don't want to be there when it happens.\033[0m"
    padding = " " * ((58 - len("I'm not afraid of death; I just don't want to be there when it happens.")) // 2)
    print("\033[38;5;214m│\033[0m" + padding, end="")
    typewriter(quote, 0.04)
    print("\033[38;5;214m│\033[0m" + " " * len(padding) + "\033[38;5;214m│\033[0m")
    
    # Empty line
    print("\033[38;5;214m│\033[0m" + " " * 58 + "\033[38;5;214m│\033[0m")
    
    # Woody Allen signature
    print("\033[38;5;214m│\033[0m\033[38;5;117m" + " " * 40 + "- Woody Allen" + " " * 5 + "\033[38;5;214m│\033[0m")
    
    # Bottom of frame
    print("\033[38;5;214m└" + "─" * 58 + "┘\033[0m")
    
    # Decorative elements
    print()
    print(" " * 15 + "\033[38;5;201m☆\033[0m" + " " * 5 + "\033[38;5;154m existential dread since 1935 \033[0m" + " " * 5 + "\033[38;5;201m☆\033[0m")
    print()
    
    # Little neurotic footnote
    print("\033[38;5;240m" + " " * 10 + "P.S. I would've made a better immortal than this." + "\033[0m")

if __name__ == "__main__":
    print_woody_quote()