"""
Campbell's Soup Can #1515
Produced: 2026-01-10 10:36:36
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

def typewriter_effect(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, color_code):
    horizontal = '─' * (width - 2)
    print_colored('┌' + horizontal + '┐', color_code)
    for _ in range(height - 2):
        print_colored('│' + ' ' * (width - 2) + '│', color_code)
    print_colored('└' + horizontal + '┘', color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't know the question, but sex is definitely the answer.",
        "I'm not a paranoid deranged millionaire. Goddammit, I'm a billionaire!"
    ]

    quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        rows, columns = os.popen('stty size', 'r').read().split()
        width = int(columns)
        height = int(rows)
    except:
        width = 80
        height = 24

    # Calculate box dimensions
    box_width = min(width - 4, 70)
    box_height = 7

    # Position box in the middle
    print("\n" * (height // 2 - box_height // 2))

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36, 37]
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Move cursor up to inside the box
    for _ in range(box_height - 2):
        sys.stdout.write("\033[1A")  # Move cursor up
        sys.stdout.write("\033[2D")  # Move cursor left

    # Print the quote with typewriter effect
    quote_color = random.choice(colors)
    while quote_color == box_color:
        quote_color = random.choice(colors)

    # Center the quote
    lines = []
    words = quote.split()
    current_line = ""
    for word in words:
        if len(current_line + word) < box_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    # Print each line centered
    for i, line in enumerate(lines):
        padding = (box_width - len(line) - 2) // 2
        sys.stdout.write("\033[1A")  # Move cursor up
        sys.stdout.write("\033[2D")  # Move cursor left
        sys.stdout.write("│" + " " * padding + f"\033[{quote_color}m{line}\033[0m" + " " * (box_width - len(line) - 2 - padding) + "│\n")

    # Add some blinking stars for fun
    time.sleep(1)
    for _ in range(3):
        star_pos = random.randint(0, box_width - 2)
        sys.stdout.write("\033[1A")  # Move cursor up
        sys.stdout.write("\033[2D")  # Move cursor left
        sys.stdout.write("│" + " " * star_pos + "\033[1;33m*\033[0m" + " " * (box_width - star_pos - 3) + "│\n")
        time.sleep(0.3)
        sys.stdout.write("\033[1A")  # Move cursor up
        sys.stdout.write("\033[2D")  # Move cursor left
        sys.stdout.write("│" + " " * (box_width - 2) + "│\n")

    # Final message
    time.sleep(1)
    print("\n" * (height // 2 - 2))
    print_colored("  ~ A Woody Allen-esque thought for your existential crisis ~", 33)
    print_colored("  (Press any key to exit... or don't. It's your life.)", 34)

    # Wait for key press
    try:
        import msvcrt
        msvcrt.getch()
    except ImportError:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    main()