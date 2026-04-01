"""
Campbell's Soup Can #3079
Produced: 2026-04-01 21:01:29
Worker: OpenAI: GPT-3.5 Turbo 16k (openai/gpt-3.5-turbo-16k)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_color_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    end_color = '\033[0m'
    if color in colors:
        print(colors[color] + text + end_color)
    else:
        print(text)

def animate_quote(quote):
    frame_delay = 0.1
    for i in range(len(quote)):
        print(quote[:i+1], end='\r')
        time.sleep(frame_delay)
    print()

if __name__ == '__main__':
    print_color_text("╭──────────────────────────────────────────╮", 'green')
    print_color_text("│   In the midst of life, we are in debt.  │", 'yellow')
    print_color_text("╰──────────────────────────────────────────╯", 'green')

    quote = "Life doesn't imitate art, it imitates bad television."
    animate_quote(quote)