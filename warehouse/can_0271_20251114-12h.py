"""
Campbell's Soup Can #271
Produced: 2025-11-14 12:59:46
Worker: Mistral: Mistral Small 3.2 24B (free) (mistralai/mistral-small-3.2-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# Define colors using ANSI escape codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
}

# Define quotes in Woody Allen's style
QUOTES = [
    "I'm not afraid of commitment, I'm just afraid of waking up next to someone more attractive than me.",
    "I don't believe in an afterlife, so I don't have to be nice to people I don't like.",
    "I'm not a paranoid, delusional person; I'm just highly sensitive to my surroundings.",
    "I don't want to live in a world where I'm the smartest person in the room. It's too lonely.",
    "I'm not a vegetarian because I love animals; I'm a vegetarian because I hate plants.",
]

# Function to print a colorful box around the text
def print_box(text, color):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'

    print(f"{COLORS[color]}{border}")
    for line in lines:
        print(f"| {line.ljust(max_length)} |")
    print(f"{border}{COLORS['reset']}")

# Function to print a typing animation
def typewriter(text, color):
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main function
def main():
    print(f"{COLORS['cyan']}")
    print("""
    _____ _____ _____ _____ _____ _____ _____ _____
    |     |     |   | |  |  |  _  |     |   __|   |
    |   --|  |  | | | |     |     | | | |  |  | | |
    |_____|_____|_|_|_|__|__|__|__|_|_|_|_____|_|_|
    """)
    print(f"{COLORS['reset']}")

    print(f"{COLORS['yellow']}Welcome to the Woody Allen Quote Generator!{COLORS['reset']}")
    print()

    # Randomly select a quote
    quote = random.choice(QUOTES)

    # Print the quote with a typing animation
    typewriter(f"Woody Allen says: {quote}", 'magenta')

    # Print the quote in a colorful box
    print_box(quote, 'green')

    # Print a funny ASCII art
    print(f"{COLORS['blue']}")
    print("""
    (  .  )
    (  :  )
     \  `^'
      :  :
     __\  /
    (____)
    """)
    print(f"{COLORS['reset']}")

if __name__ == "__main__":
    main()