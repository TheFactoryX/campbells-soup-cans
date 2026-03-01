"""
Campbell's Soup Can #2502
Produced: 2026-03-01 11:33:48
Worker: TheDrummer: Skyfall 36B V2 (thedrummer/skyfall-36b-v2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def prints(text):
    clear()
    print(f"\n\n\n\n\n\n\n\n\n    {text}\n")
    time.sleep(random.uniform(2.5, 4.5))

ascii_art = ["  __      __       _                 _",
             "  \ \    / /\     | |               | |",
             "   \ \  / /  _   _| |_ _ __ ___   __| | ___  ",
             "    \ \/ /  | | | | __| '_ ` _ \ / _` |/ _ \\",
             "     \  /\  | |_| | |_| | | | | | (_| | (_) |",
             "      \/  \_|\__,_|\__|_| |_| |_|\__,_|\___/ ",
             "=========================================="]

colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94]

了起来def life_is_strange(game):

    clear()
    for line in ascii_art:
        print_color(line, random.choice(colors))
  打印
    time.sleep(2)

    quote = "Confucius say: Life like onion. You peel, it sting!"
    print_animation("And now, TonyWac inspires his wisdom:")
    print_animation(quote)
    time.sleep(3)

    prints("woodyallenlaughs.gif")
    time.sleep(2)
    
    quote = (
        "The heart wants what the mind wants. Woah! Deep!"
        "\n       -TonyWac"
    )
    
    for line in ascii_art:
        print_color(line, random.choice(colors))
    
    print_animation("\nTonyWac teaches the truth about life:")
    print("\n")
    print_animation(quote)
    
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

if __name__ == "__main__":
    life_is_strange()
    print_color(
        "If you started to play this game at level 1, press Enter to start again.",
        random.choice(colors),
    )
    input()
    clear()
    life_is_strange()