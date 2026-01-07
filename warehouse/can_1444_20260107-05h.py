"""
Campbell's Soup Can #1444
Produced: 2026-01-07 05:42:26
Worker: Google: Gemma 3 27B (free) (google/gemma-3-27b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def animated_box(text, color="32"):
    """Prints text inside an animated box with a given color."""
    box_width = len(text) + 6
    box_height = 3

    box_chars = [" ", "-", "+", "|"]
    
    for i in range(box_height):
        if i == 0:
            line = f"\033[{color}m" + "+" + "-" * (box_width - 2) + "+" + "\033[0m"
        elif i == box_height - 1:
            line = f"\033[{color}m" + "+" + "-" * (box_width - 2) + "+" + "\033[0m"
        else:
            line = f"\033[{color}m" + "+" + " " * (box_width - 2) + "+" + "\033[0m"
            
        if i == 1:
            line = f"\033[{color}m" + "| " + text + " |" + "\033[0m"

        print(line)

def wobble_text(text, color="33"):
    """
    Wobbles the text horizontally using ANSI escape codes.
    """
    width = len(text)
    for i in range(width + 1):
        padding = " " * i
        print(f"\033[{color}m{padding}{text}\033[0m", end="\r")
        time.sleep(0.05)
    
    for i in range(width, -1, -1):
        padding = " " * i
        print(f"\033[{color}m{padding}{text}\033[0m", end="\r")
        time.sleep(0.05)
    print()

def main():
    quote = "I've come to the conclusion that life is basically just a series of unfortunate events mitigated by the occasional sandwich."

    colors = ["31", "32", "33", "34", "35", "36"]
    random_color = random.choice(colors)

    print("\033[1m\033[95mThinking... (if that's even possible)\033[0m")
    time.sleep(1)

    # Choose a visual presentation at random
    presentation_type = random.randint(1, 3)
    
    if presentation_type == 1:
        animated_box(quote, random_color)

    elif presentation_type == 2:
        wobble_text(quote, random_color)
        
    else:
        print_with_delay(quote, 0.03)
        print("\033[37m(And honestly, the sandwiches aren't *that* good.)\033[0m")

if __name__ == "__main__":
    main()