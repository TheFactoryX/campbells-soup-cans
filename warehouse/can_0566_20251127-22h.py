"""
Campbell's Soup Can #566
Produced: 2025-11-27 22:32:58
Worker: Qwen: QwQ 32B (qwen/qwq-32b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# A Woody Allen classic quote
quote = "I'm not afraid of death; I just don't want to be there when the Time Lords decide it's overmuch too soon."

border_color = 202  # Light Cyan (ANSI) - like panic buttons
animation_colors = [1, 3, 5, 9, 11, 13, 17, 19, 21]  # Bright colors

def animate_character(char, delay=0.03):
    color = random.choice(animation_colors)
    sys.stdout.write(f'\033[38;5;{color}m{char}\033[0m')
    sys.stdout.flush()
    time.sleep(delay)

def print_box(text):
    text_length = len(text)
    border = f'\033[38;5;{border_color}m{"─" * (text_length + 4)}\033[0m'
    
    print("\n" * 5)  # Create a sudden visual surprise
    
    # Print top border with animated corners
    print(f'\033[38;5;{border_color}m╔')
    for _ in range(text_length + 2):
        animate_character('─', 0.01)
    print('╗\033[0m\n', end='')
    
    # Print the text with a joyful frame
    print(f'\033[38;5;{border_color}m║ \033[0m', end='')
    for char in text:
        animate_character(char)
    print(f'\033[38;5;{border_color}m ║\033[0m')
    
    # Print bottom border with crazy love hearts in corners (just joking - regular border)
    print(f'\033[38;5;{border_color}m╚')
    for _ in range(text_length + 2):
        animate_character('─', 0.01)
    print('╝\033[0m')
    
    # Add a nervous footer
    time.sleep(0.5)
    print('\n' + ' ' * 10 + f'\033[38;5;{border_color}m(...But maybe I overdid the existential dread?)\033[0m')

if __name__ == "__main__":
    # Clear screen and center the chaos
    sys.stdout.write('\033[2J\033[1H')
    
    # Add a distractingly random border pattern
    for line in range(5):
        print(''.join(f'\033[38;5;{random.choice(animation_colors)}m☆\033[0m' for _ in range(30)))
    
    print_box(quote)