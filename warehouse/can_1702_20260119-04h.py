"""
Campbell's Soup Can #1702
Produced: 2026-01-19 04:20:11
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

def draw_box(width, height, color_code):
    horizontal = "\033[" + str(color_code) + "m" + "─" * (width - 2) + "\033[0m"
    vertical = "\033[" + str(color_code) + "m" + "|" + "\033[0m"
    corners = ["\033[" + str(color_code) + "m" + "┌", "┐", "└", "┘" + "\033[0m"]

    print(corners[0] + horizontal + corners[1])
    for _ in range(height - 2):
        print(vertical + " " * (width - 2) + vertical)
    print(corners[2] + horizontal + corners[3])

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens."
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Get terminal width
    terminal_width = 80  # Default if we can't get it
    try:
        terminal_width = int(sys.stdout.get_terminal_size().columns)
    except:
        pass

    # Box dimensions
    box_width = min(terminal_width, 70)
    box_height = 10

    # Draw the box with a fun color
    draw_box(box_width, box_height, "93")  # Yellow

    # Position cursor inside the box
    for _ in range(box_height - 2):
        print("\033[F", end="")  # Move cursor up

    # Print the quote with typewriter effect and color
    print("\033[93m")  # Yellow
    print("\033[1m")   # Bold

    # Center the quote
    lines = quote.split('\n')
    for line in lines:
        # Split line into words and wrap if necessary
        words = line.split()
        current_line = []
        for word in words:
            if len(' '.join(current_line + [word])) < box_width - 4:
                current_line.append(word)
            else:
                # Print current line
                print("\033[33C", end="")  # Move right to center
                typewriter_effect(' '.join(current_line), 0.05)
                current_line = [word]
        if current_line:
            print("\033[33C", end="")  # Move right to center
            typewriter_effect(' '.join(current_line), 0.05)

    print("\033[0m")  # Reset

    # Add a little animation
    for _ in range(3):
        time.sleep(0.5)
        print("\033[33C\033[93m✨\033[0m")
        time.sleep(0.5)
        print("\033[33C\033[93m  \033[0m")
        print("\033[F", end="")  # Move cursor up

    # Final touch
    print("\033[33C\033[93m✨\033[0m")
    print("\033[33C\033[93m-- Woody Allen (probably)\033[0m")

if __name__ == "__main__":
    main()