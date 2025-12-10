"""
Campbell's Soup Can #831
Produced: 2025-12-10 04:46:29
Worker: OpenAI: GPT-4 Turbo Preview (openai/gpt-4-turbo-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def print_quote():
    quote = """I'm not afraid of death; I just don't want to be there when it happens."""
    style = [
        "\033[1;33;40m",  # Yellow on black background, bold
        "\033[0m"         # Reset to default
    ]
    
    # ASCII art top border
    print(style[0] + "╔" + "═" * 76 + "╗" + style[1])
    for i in range(3): print(style[0] + "║" + " " * 76 + "║" + style[1])
    
    # Center the quote
    left_padding = (76 - len(quote)) // 2
    print(style[0] + "║" + " " * left_padding + quote + " " * left_padding + (" " if len(quote) % 2 != 0 else "") + "║" + style[1])
    
    for i in range(3): print(style[0] + "║" + " " * 76 + "║" + style[1])
    # ASCII art bottom border
    print(style[0] + "╚" + "═" * 76 + "╝" + style[1])

def typewriter_effect(message, interval=0.05):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(interval)

if __name__ == "__main__":
    clear()
    message = """
    In a world where everyone is overexposed, the coolest thing you can do is maintain your mystery.\n
    """
    typewriter_effect("\033[1;35;40m" + message + "\033[0m", 0.1)  # Purple on black background, bold
    time.sleep(1)
    print_quote()