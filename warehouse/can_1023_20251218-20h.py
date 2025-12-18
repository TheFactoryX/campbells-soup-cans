"""
Campbell's Soup Can #1023
Produced: 2025-12-18 20:32:44
Worker: Mistral: Devstral 2 2512 (free) (mistralai/devstral-2512:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height):
    corners = ['╔', '╗', '╚', '╝']
    horizontal = '═'
    vertical = '║'

    # Top border
    print_colored(corners[0] + horizontal * (width - 2) + corners[1], '93')

    # Middle content
    for _ in range(height - 2):
        print_colored(vertical + ' ' * (width - 2) + vertical, '93')

    # Bottom border
    print_colored(corners[2] + horizontal * (width - 2) + corners[3], '93')

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Funny Woody Allen-style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's the exit?",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of dying, I just don't want to be there when it happens.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, blind people, cripples. I thank God for my misery.",
        "I don't want to achieve immortality through my work... I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "My one regret in life is that I am not someone else.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't know the question, but sex is definitely the answer."
    ]

    selected_quote = random.choice(quotes)

    # ASCII art of Woody Allen (simplified)
    woody_art = r"""
          .-""""""-.
         /          \
        |            |
        |  O    O    |
        |    __      |
        |   /  \     |
        |  |    |    |
         \  \__/    /
          '-....-'
    """

    # Print Woody Allen ASCII art with color
    print_colored(woody_art, '96')

    # Print a fancy box
    box_width = max(len(line) for line in woody_art.split('\n')) + 4
    draw_box(box_width, 15)

    # Print the quote with typewriter effect
    print("\n")
    print_colored("    Woody Allen's Thought of the Day:", '95')
    print("\n")
    typewriter_effect(f"    \"{selected_quote}\"", 0.03)
    print("\n")

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print_colored("    ⭐", '93')
        time.sleep(0.5)
        print_colored("    ⭐", '91')
        time.sleep(0.5)
        print_colored("    ⭐", '92')
        print("\033[F", end="")  # Move cursor up
        print("    \033[K", end="")  # Clear line

    print("\n")

if __name__ == "__main__":
    main()