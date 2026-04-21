"""
Campbell's Soup Can #3394
Produced: 2026-04-21 23:51:56
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_allen_quote.py
# A playful Python script to display a funny philosophical quote in Woody Allen's style

import time
import sys

def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'gray': '\033[90m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def draw_box(text, border_color='cyan', text_color='yellow'):
    width = len(text) + 4
    print_colored('+' + '-' * width + '+', border_color)
    print_colored(f"|  {text}  |", text_color)
    print_colored('+' + '-' * width + '+', border_color)

def main():
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    attribution = "- Woody Allen"

    print("\n" * 2)
    draw_box(quote, border_color='cyan', text_color='yellow')
    print("\n" * 1)
    print_colored(attribution, 'gray')
    print("\n" * 2)

if __name__ == "__main__":
    main()