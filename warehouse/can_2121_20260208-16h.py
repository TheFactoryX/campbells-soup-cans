"""
Campbell's Soup Can #2121
Produced: 2026-02-08 16:50:00
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time
from random import random

# ANSI escape codes for colors and styles
PURPLE = "\033[95m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80  # Default width

def oscillate_text(text, base_delay=0.02, amplitude=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(base_delay + amplitude * random())

def main():
    clear_screen()
    width = min(get_terminal_width(), 100)
    
    # ASCII art of a neurotic philosopher
    ascii_art = rf"""
{WHITE}       ,~~~.                         {PURPLE}    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
{WHITE}      [o,o]/{YELLOW}ø{PURPLE}                       ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
{WHITE}      /)__) {PURPLE}                       ▐▓▓▓▓▓▓      PHILOSOPHY ▓▓▌
{WHITE}     ="=j_!=="{PURPLE}                      ▐▓▓▓▓▓▓    (AND ANXIETY)▓▓▌
                               ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
    {END}"""
    
    # Woody Allen style quote
    quote = "I'm not afraid of existential despair; I just wish it came with better lighting and a complimentary beverage."
    author = "- Woody Allen's Neurotic Cousin"

    # Build speech bubble
    max_text_width = width - 10
    lines = []
    current_line = []
    current_length = 0
    
    for word in quote.split():
        if current_length + len(word) + 1 <= max_text_width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))

    # Print ASCII art
    print("\n" * 2)
    for line in ascii_art.split('\n'):
        print(line.center(width))
    
    # Calculate box dimensions
    box_width = max(len(line) for line in lines) + 4
    box_width = min(box_width, width - 4)
    horizontal_border = PURPLE + "┏" + "━" * (box_width - 2) + "┓" + END
    
    # Print speech bubble with animation
    print("\n" + horizontal_border.center(width))
    for line in lines:
        padded_line = "┃ " + line.ljust(box_width - 4) + " ┃" 
        colored_line = WHITE + padded_line[0] + UNDERLINE + padded_line[1:-1] + WHITE + padded_line[-1] + END
        print(colored_line.center(width))
        time.sleep(0.3)
    
    print(PURPLE + "┗" + "━" * (box_width - 2) + "┛" + END.center(width))
    
    # Animated author attribution
    print("\n")
    colored_author = YELLOW + BOLD + author + END
    oscillate_text(colored_author.center(width))
    
    print("\n" * 2)
    time.sleep(2)

if __name__ == "__main__":
    main()