"""
Campbell's Soup Can #3536
Produced: 2026-05-02 16:01:23
Worker: Qwen: Qwen3 Coder Flash (qwen/qwen3-coder-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_boxed_quote(quote):
    # Create a decorative box around the quote
    width = len(quote) + 4
    print("╔" + "═" * width + "╗")
    print("║ " + quote + " ║")
    print("╚" + "═" * width + "╝")

def print_woody_quote():
    # Woody Allen style quotes
    woody_quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I'm always terrified of the possible consequences of doing something stupid.",
        "I'm not a pessimist. I'm a realist who has been to hell and back.",
        "I'm not worried about the future. I'm worried about the past.",
        "The worst thing about being a pessimist is that you're usually right.",
        "I've had a perfectly wonderful evening, but this wasn't it.",
        "I'm not lazy, I'm on energy-saving mode.",
        "I don't know what's worse - being laughed at or not being laughed at."
    ]
    
    return random.choice(woody_quotes)

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_ascii_art():
    art = [
        "   ╦  ╦ ╔═╗ ╔╦╗ ╔═╗ ╔╗╔ ╦╔═╗ ╔╦╗ ╦ ╦",
        "   ║  ║ ╠═╣  ║║ ║ ║ ║║║ ║╠═╝  ║  ╚═╣",
        "   ╩  ╩ ╩ ╩ ═╩╝ ╚═╝ ╝╚╝ ╩╩    ╩   ╩"
    ]
    for line in art:
        print_colored_text(line, "35")  # Purple color

def main():
    clear_screen()
    
    # Print title with animation
    print_colored_text("=== WOODY ALLEN PHILOSOPHICAL QUOTE GENERATOR ===", "36")  # Cyan
    print()
    
    # Print ASCII art
    print_ascii_art()
    print()
    
    # Get random quote
    quote = print_woody_quote()
    
    # Add some dramatic pause
    time.sleep(1)
    
    # Print animated quote
    print_colored_text("Here's your philosophical insight:", "33")  # Yellow
    print()
    animate_text(quote, 0.03)
    print()
    
    # Print boxed version
    print_colored_text("The wisdom in a box:", "32")  # Green
    print_boxed_quote(quote)
    print()
    
    # Add some existential humor
    print_colored_text("P.S. - This is probably profound, or completely meaningless.", "31")  # Red
    print()

if __name__ == "__main__":
    main()