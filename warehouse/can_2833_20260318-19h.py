"""
Campbell's Soup Can #2833
Produced: 2026-03-18 19:17:36
Worker: Google: Nano Banana (Gemini 2.5 Flash Image) (google/gemini-2.5-flash-image)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_quote_animation():
    quote = "I'm not saying life is meaningless... but can we at least get a refund on the existential angst?"
    
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\032[32m",  # Green
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
    ]
    reset_color = "\033[0m"

    clear_screen()
    
    # Box dimensions
    box_width = len(quote) + 6
    box_height = 5

    # Top border
    print("-" * box_width)

    # Empty lines in box
    print(f"|{' ' * (box_width - 2)}|")
    print(f"|{' ' * (box_width - 2)}|")

    # Animated quote
    for i, char in enumerate(quote):
        color = colors[i % len(colors)]
        print(f"\r|  {color}{quote[:i+1]}{reset_color}{' ' * (len(quote) - i -1)}  |", end="", flush=True)
        time.sleep(0.05)
    
    print() # Newline after the animated quote
    
    # Empty line in box
    print(f"|{' ' * (box_width - 2)}|")
    
    # Bottom border
    print("-" * box_width)
    print("\n\n\033[90m - A wise man (or just incredibly stressed)\033[0m") # Gray text

if __name__ == "__main__":
    woody_quote_animation()