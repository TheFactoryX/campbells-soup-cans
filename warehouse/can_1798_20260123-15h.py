"""
Campbell's Soup Can #1798
Produced: 2026-01-23 15:42:17
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
    corners = ['╔', '╗', '╝', '╚']
    horizontal = '═'
    vertical = '║'

    # Top border
    print(corners[0] + horizontal * (width - 2) + corners[1])

    # Middle
    for _ in range(height - 2):
        print(vertical + ' ' * (width - 2) + vertical)

    # Bottom border
    print(corners[3] + horizontal * (width - 2) + corners[2])

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Funny Woody Allen-style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "It's not that I'm afraid to die, I just don't want to be there when it happens.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I'm in the miserable category.",
        "I don't want to achieve immortality through my work... I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown."
    ]

    quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        size = os.get_terminal_size()
        width = size.columns
        height = size.lines
    except:
        width = 80
        height = 24

    # Center the box
    box_width = min(width - 4, 60)
    box_height = 7

    # Calculate padding
    padding = (width - box_width) // 2

    # Print empty lines to center vertically
    for _ in range((height - box_height) // 2 - 1):
        print()

    # Print the box with padding
    print(' ' * padding, end='')
    draw_box(box_width, box_height)

    # Print the quote inside the box with typewriter effect
    for _ in range((height - box_height) // 2 - 3):
        print()

    print(' ' * padding + '║', end='')
    print(' ' * ((box_width - 2 - len(quote)) // 2), end='')
    typewriter_effect(quote, 0.03)
    print(' ' * padding + '║')

    # Print some colorful philosophical thoughts
    print()
    time.sleep(1)

    colors = [31, 33, 32, 36, 35, 34]  # Red, Yellow, Green, Cyan, Magenta, Blue
    thoughts = [
        "The universe is expanding... and so is my waistline.",
        "Existence is a fleeting moment between two oblivions... and I'm late for dinner.",
        "We're all just cosmic dust... but I prefer to think of myself as a slight smudge.",
        "Time is an illusion... but my rent is very real.",
        "The meaning of life is 42... but my IQ is only 39.",
        "We're all going to die... but first, let me check my email."
    ]

    for i, thought in enumerate(thoughts):
        color = colors[i % len(colors)]
        print_colored(f"  {thought}", color)
        time.sleep(0.8)

    # Final thought with animation
    print()
    print_colored("  And remember:", 33)
    time.sleep(1)

    final_thought = "If you're not failing every now and again, it's a sign you're not doing anything very innovative."
    print_colored("  ", 33, end='')
    typewriter_effect(final_thought, 0.02)

    print()
    print_colored("  -- Woody Allen (probably)", 34)

if __name__ == "__main__":
    main()