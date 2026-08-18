"""
Campbell's Soup Can #4682
Produced: 2026-08-18 20:40:45
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def type_write(text, delay=0.05, color='\033[1;33m'):
    """Print text character by character with a color."""
    reset = '\033[0m'
    for ch in text:
        sys.stdout.write(color + ch + reset)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear the screen using ANSI escape codes
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    # Print a title
    title = "A Woody Allen-esque Thought"
    print('\033[1;35m' + title + '\033[0m')
    print('-' * len(title))

    # The philosophical quote
    quote = ("I'm not afraid of death; I'm afraid that when I die, "
             "my therapist will finally get to bill me for the last session.")

    # Create a box around the quote
    padding = 2
    width = len(quote) + padding * 2
    border_char = '*'
    top_bottom = border_char * (width + 2)

    # Top border
    print(top_bottom)
    # Side borders with spaces
    print(border_char + ' ' * width + border_char)
    # Quote line with typewriter effect
    sys.stdout.write(border_char + ' ' * padding)
    type_write(quote, delay=0.06)
    sys.stdout.write(' ' * padding + border_char + '\n')
    # Side borders again
    print(border_char + ' ' * width + border_char)
    # Bottom border
    print(top_bottom)

if __name__ == '__main__':
    main()