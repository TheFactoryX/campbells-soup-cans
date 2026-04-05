"""
Campbell's Soup Can #3154
Produced: 2026-04-05 22:51:33
Worker: Amazon: Nova Lite 1.0 (amazon/nova-lite-v1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, os, random
from termcolor import colored

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def color_shift(text):
    """
    Output text with shifting colors.
    """
    colors = ['red', 'green', 'yellow', 'blue','magenta', 'cyan']
    for color in colors:
        print(colored(text, color))
        time.sleep(0.5)

def draw_border():
    """
    Draw a colorful border around the output.
    """
    border_color = random.choice(['red', 'green', 'yellow', 'blue','magenta', 'cyan'])
    print(colored("╔" + "═" * 60 + "╗", border_color))
    print(colored("║" + " " * 60 + "║", border_color))
    print(colored("║" + " " * 25 + " ".join([colored("●", border_color), colored("●", border_color), colored("●", border_color)]) + " " * 23 + "║", border_color))
    print(colored("║" + " " * 60 + "║", border_color))
    print(colored("╚" + "═" * 60 + "╝", border_color))

def main():
    clear_screen()
    draw_border()

    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    ]
    
    quote = random.choice(quotes)
    color_shift(quote)
    
    print()
    time.sleep(1)
    print(colored("\n\n      — Woody Allen\n", 'grey'))
    time.sleep(1)
    clear_screen()

if __name__ == "__main__":
    main()