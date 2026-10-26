"""
Campbell's Soup Can #5170
Produced: 2026-10-26 13:15:58
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

def main():
    RED = '\033[31m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Woody Allen-style philosophical quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. It's like missing an important meeting you didn't even know you had."
    max_len = len(quote)
    
    # Calculate ASCII art border width
    border_length = max_len + 4  # For the spaces and '+' signs
    
    # Load the quote with a typewriter-style animation
    def type_animation(text):
        for char in text:
            print(YELLOW + char, end='', flush=True)
            time.sleep(0.02)  # Control typing speed
        print(RESET)
    
    # Print the top red border
    print(RED + '+' + '-' * border_length + '+' + RESET)
    
    # Print the middle line in cyan with the animated quote
    print(RED + '| ', end='')
    sys.stdout.flush()
    type_animation(' ')  # For the space after |
    type_animation(CYAN + BOLD + quote)
    print(RESET + ' |')
    
    # Print the bottom red border
    print(RED + '+' + '-' * border_length + '+' + RESET)

if __name__ == "__main__":
    main()