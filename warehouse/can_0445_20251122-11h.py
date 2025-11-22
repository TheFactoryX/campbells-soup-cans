"""
Campbell's Soup Can #445
Produced: 2025-11-22 11:25:15
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
import random

def typewriter(text, delay=0.05):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_with_border(text, border_char='~'):
    """Print text with a decorative border"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    print(f"\033[38;5;214m{border_char * (max_len + 4)}\033[0m")
    for line in lines:
        print(f"\033[38;5;214m{border_char}\033[0m \033[38;5;117m{line:<{max_len}}\033[0m \033[38;5;214m{border_char}\033[0m")
    print(f"\033[38;5;214m{border_char * (max_len + 4)}\033[0m")

def print_woody_quote():
    """Print a funny philosophical quote in Woody Allen's style with visual flair"""
    
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # ASCII art of a neurotic brain
    brain_art = [
        "    _____    ",
        "   (     )   ",
        "  (       )  ",
        " ( o   o )   ",
        "  (  V  )    ",
        "  ^^ | ^^    ",
        "     |       ",
        "   ooooo     ",
        "  ooooooo    ",
        " ooooooooo   "
    ]
    
    # Print brain with color
    print("\n" * 2)
    for line in brain_art:
        print(" " * 15 + "\033[38;5;196m" + line + "\033[0m")
        time.sleep(0.1)
    
    # Title
    title = "WOODY ALLEN'S DEEP THOUGHTS"
    print("\n" + " " * 10 + "\033[1;38;5;220m" + "=" * len(title) + "\033[0m")
    print(" " * 10 + "\033[1;38;5;220m" + title + "\033[0m")
    print(" " * 10 + "\033[1;38;5;220m" + "=" * len(title) + "\033[0m\n")
    
    # The philosophical quote
    quote = "I'm not afraid of dying, but I'm in no hurry to become a prototype."
    
    # Decorative elements
    decorations = ["★", "♪", "✿", "✦", "✧", "❦", "❧"]
    deco = random.choice(decorations)
    
    # Print with fancy border
    print_with_border(quote, deco)
    
    # Add signature
    print("\n" + " " * 25 + "\033[3m\033[38;5;240m— W. Allen, probably while worrying about his mortality\033[0m")
    
    # Add some existential anxiety at the bottom
    anxiety_meter = [
        "\033[38;5;196m█\033[0m" * 10 + " \033[38;5;250m(Existential crisis: LOW)\033[0m",
        "\033[38;5;196m█\033[0m" * 20 + " \033[38;5;250m(Existential crisis: MEDIUM)\033[0m",
        "\033[38;5;196m█\033[0m" * 30 + " \033[38;5;250m(Existential crisis: HIGH)\033[0m",
        "\033[38;5;196m█\033[0m" * 40 + " \033[38;5;250m(Existential crisis: CATASTROPHIC)\033[0m"
    ]
    
    print("\n\033[1mYour Daily Dose of Neurotic Wisdom:\033[0m")
    for meter in anxiety_meter:
        print(" " * 5 + meter)
        time.sleep(0.3)
    
    # Final thought
    print("\n\033[38;5;250mP.S. Try not to think about it too much.\033[0m")
    print("\033[38;5;245m(But if you do, remember: at least you're thinking.)\033[0m")

if __name__ == "__main__":
    print_woody_quote()