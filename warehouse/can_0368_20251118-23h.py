"""
Campbell's Soup Can #368
Produced: 2025-11-18 23:29:08
Worker: Google: Gemma 3 27B (free) (google/gemma-3-27b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text, color_code='\033[37m'):  # Default to white
    for char in text:
        print(color_code + char, end='', flush=True)
        time.sleep(0.03)
    print()  # Newline after the full quote

def animate_dots(num_dots=5):
    for i in range(num_dots):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print()

def main():
    clear_screen()

    quote = "I’m having a terrible existential crisis, but at least the upholstery is comfortable. It’s a small victory, really, when you consider the vast, uncaring void… and that I probably left the oven on."

    # Color codes (ANSI escape codes)
    yellow = "\033[93m"
    cyan = "\033[96m"
    magenta = "\033[95m"
    reset = "\033[0m"

    # Draw a wobbly box around the quote
    print(yellow + "╔" + "═" * 20 + "╗")
    print(yellow + "║" + " " * 20 + " ║")
    print(yellow + "║  " + cyan + quote + reset + " ║")
    print(yellow + "║" + " " * 20 + " ║")
    print(yellow + "╚" + "═" * 20 + "╝" + reset)


    print(magenta)
    animate_dots()
    print_slowly("A thought, from somewhere…probably Brooklyn.", color_code=magenta)
    print(reset)

    # A little extra flair
    time.sleep(1)
    clear_screen()
    print(yellow + "Thinking…thinking…oh dear…" + reset)


if __name__ == "__main__":
    main()