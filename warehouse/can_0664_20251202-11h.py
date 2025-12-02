"""
Campbell's Soup Can #664
Produced: 2025-12-02 11:30:42
Worker: Bert-Nebulon Alpha (openrouter/bert-nebulon-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def slow_print(text, delay=0.05, color=None):
    if color:
        print(color, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if color:
        print('\033[0m', end='')

def animate_quote():
    colors = [
        '\033[91m',  # red
        '\033[92m',  # green
        '\033[93m',  # yellow
        '\033[94m',  # blue
        '\033[95m',  # magenta
        '\033[96m',  # cyan
    ]

    woody_quotes = [
        "My one regret in life is that I am not someone else.",
        "I don't believe in an afterlife, although I am bringing a change of underwear.",
        "I can't listen to that much Wagner. I start getting the urge to conquer Poland.",
        "I failed to make the chess team because of my height.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying. I don't want to live on in the hearts of my countrymen. I want to live on in my apartment.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
        "I am at two with nature.",
        "To love is to suffer. To avoid suffering, one must not love. But then, one suffers from not loving. Therefore, to love is to suffer; not to love is to suffer; to suffer is to suffer. To be happy is to love. To be happy, then, is to suffer, but suffering makes one unhappy. Therefore, to be happy, one must love or love to suffer or suffer from too much happiness."
    ]

    quote = random.choice(woody_quotes)
    border = "╔" + "═" * (len(quote) + 4) + "╗"
    empty_line = "║" + " " * (len(quote) + 4) + "║"
    quote_line = f"║  {quote}  ║"
    bottom_border = "╚" + "═" * (len(quote) + 4) + "╝"

    print("\n" * 2)
    slow_print(border + "\n", color=random.choice(colors))
    slow_print(empty_line + "\n", color=random.choice(colors))

    for i, char in enumerate(quote_line):
        if char != "║" and char != " ":
            slow_print(char, color=random.choice(colors))
        else:
            print(char, end='', flush=True)
        time.sleep(0.02)

    print()
    slow_print(empty_line + "\n", color=random.choice(colors))
    slow_print(bottom_border + "\n", color=random.choice(colors))

    print("\n" + " " * (len(quote) // 2 - 5) + "— Woody Allen\n")

    for _ in range(3):
        for color in colors:
            print(color + "  ★  " + '\033[0m', end='', flush=True)
            time.sleep(0.2)
        print('\r' + " " * 20 + '\r', end='', flush=True)
        time.sleep(0.2)

    print("  ★  " + '\033[0m')

if __name__ == "__main__":
    try:
        print("\033[2J\033[H", end='')  # Clear screen
        print("\033[95m" + r"""
        ____  _    _   _______ _____ _____ _   _
       / __ \| |  | | |__   __|_   _/ ____| | | |
      | |  | | |  | |    | |    | || |  __| |_| |
      | |  | | |  | |    | |    | || | |_ |  _  |
      | |__| | |__| |    | |   _| || |__| | | | |
       \____/ \____/     |_|  |_____\_____|_| |_|
        """ + '\033[0m')

        print("\033[93m" + "Loading Woody Allen's existential wisdom...\n" + '\033[0m')
        time.sleep(1)
        animate_quote()
    except KeyboardInterrupt:
        print("\n\033[91m" + "Wisdom interrupted. The universe remains a mystery." + '\033[0m')