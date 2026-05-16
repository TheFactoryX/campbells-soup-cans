"""
Campbell's Soup Can #3698
Produced: 2026-05-16 17:16:10
Worker: Relace: Relace Search (relace/relace-search)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys

def print_woody_quote():
    # Woody Allen style quotes
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I'm convinced that the only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion.",
        "The most important thing is to be yourself. Unless you're a dog, then be a good dog.",
        "I am not a vegetarian because I hate animals. I am a vegetarian because I love animals. I hate vegetables.",
        "I'm not neurotic. I'm just highly sensitive to my own neuroses.",
        "I think the worst thing about death is that it's permanent. If it were temporary, I'd never get out of bed in the morning.",
        "I'm not afraid of dying. I'm just afraid of the pain that comes before it.",
        "I'm not a pessimist. I'm just a realist who's been around long enough to know that things usually go wrong."
    ]
    
    # Color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    # Create a fancy border
    def create_border(text):
        border_length = len(text) + 8
        border = "┌" + "─" * (border_length - 2) + "┐"
        bottom_border = "└" + "─" * (border_length - 2) + "┘"
        return f"{border}\n│  {text}  │\n{bottom_border}"
    
    # Animate text appearance
    def animate_text(text, delay=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    
    # Select random quote
    quote = random.choice(quotes)
    
    # Create colorful box
    colored_quote = ""
    color_list = list(colors.values())[:-3]  # Exclude end, bold, underline
    
    for i, char in enumerate(quote):
        if char == ' ':
            colored_quote += char
        else:
            color = color_list[i % len(color_list)]
            colored_quote += f"{color}{char}{colors['end']}"
    
    # Add some ASCII art
    ascii_art = """
     ╔══════════════════════════════════════════════════════════════════════════════╗
     ║                                                                             ║
     ║                        🎭 WOODY ALLEN PHILOSOPHY 🎭                         ║
     ║                                                                             ║
     ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    
    # Print with animation
    print(ascii_art)
    print()
    
    # Print the quote with fancy formatting
    formatted_quote = create_border(colored_quote)
    print(formatted_quote)
    print()
    
    # Add a signature
    signature = "    — Woody Allen (probably)"
    print(f"{colors['yellow']}{colors['italic']}{signature}{colors['end']}")
    
    # Add a small animation effect
    print("\n" + "✨" * 20)
    print("Thinking deeply about life...")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n" + "✨" * 20)

# Run the function
if __name__ == "__main__":
    print_woody_quote()