"""
Campbell's Soup Can #4901
Produced: 2026-09-04 21:29:37
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def slow_print(text, color, delay=0.03):
    print(color, end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('\033[0m', end='', flush=True)

def woody_allen_philosophy():
    # The Woody Allen quote in his neurotic, self-deprecating style
    quote = "I don't want to achieve immortality through my work; I just don't want to be there when it happens."
    
    # ANSI color codes for visual flair
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGIC_PURPLE = '\033[95m'
    
    # Calculate box dimensions dynamically
    box_length = len(quote) + 4
    inner_width = box_length - 2
    padding = (inner_width - len(quote)) // 2
    left_pad = ' ' * padding
    right_pad = ' ' * (inner_width - len(quote) - padding)
    
    # Build box components with padding
    top_border = f"+{'-' * (box_length - 2)}+"
    bottom_border = top_border
    content_line = f"|{left_pad}{quote}{right_pad}|\n"
    
    # Animate the top border with cyan fade
    print(MAGIC_PURPLE + " " * 20 + "↓↓↓ Philosophizing in Progress ↓↓↓\n" + '\033[0m')
    print(CYAN + top_border)
    time.sleep(0.2)  # Dramatic pause
    
    # Type the existential dread slowly
    slow_print(content_line, YELLOW)
    
    # Close the box with a flourish
    print(CYAN + bottom_border)
    print(MAGIC_PURPLE + " " * 20 + "↑↑↑ Existential Crisis Complete ↑↑↑" + '\033[0m')

if __name__ == "__main__":
    woody_allen_philosophy()