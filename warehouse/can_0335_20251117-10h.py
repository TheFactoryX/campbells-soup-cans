"""
Campbell's Soup Can #335
Produced: 2025-11-17 10:40:13
Worker: Anthropic: Claude 3.7 Sonnet (anthropic/claude-3.7-sonnet)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys
import os
from math import sin, cos

# Woody Allen style quotes
quotes = [
    "The universe is merely a fleeting idea in God's mind - a rather uncomfortable thought, particularly if you've just made a down payment on a house.",
    "I'm not afraid of the void; I just don't want to be there when I fall into it.",
    "Eternity is really long, especially near the end.",
    "My brain: the only thing keeping me from true happiness and also from jumping off a bridge.",
    "Existence is a brief interruption of the eternal nothingness. Unfortunately, so are most of my relationships.",
    "I've figured out the meaning of life, but now I can't remember where I put the note.",
    "The key to being content is lowering your expectations to the point of despair, then everything is a pleasant surprise."
]

# ANSI color codes
class Color:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art of Woody Allen's glasses and hair
def print_woody():
    glasses = [
        "       ____===____      ",
        " _____|         |_____ ",
        "/     |         |     \\",
        "|  O  |         |  O  |",
        "\\_____|_________|_____/"
    ]
    
    for i, line in enumerate(glasses):
        if i < 2:
            print(f"{Color.YELLOW}{line}{Color.RESET}")
        else:
            print(f"{Color.BLACK}{Color.BOLD}{line}{Color.RESET}")

# Animated typing effect
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Draw a fancy box around text
def box_text(text, width=60):
    lines = []
    words = text.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:  # -4 for the box borders and spaces
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    
    if current_line:
        lines.append(current_line)
    
    max_length = max(len(line) for line in lines)
    
    print(f"{Color.CYAN}╭{'─' * (max_length + 2)}╮{Color.RESET}")
    
    for line in lines:
        print(f"{Color.CYAN}│{Color.RESET} {Color.YELLOW}{line.ljust(max_length)}{Color.RESET} {Color.CYAN}│{Color.RESET}")
    
    print(f"{Color.CYAN}╰{'─' * (max_length + 2)}╯{Color.RESET}")

# Main program
def main():
    clear_screen()
    
    # Choose a random quote
    quote = random.choice(quotes)
    
    # Create a pulsing effect
    for _ in range(3):
        clear_screen()
        time.sleep(0.3)
        print("\n\n")
        print_woody()
        print("\n")
        time.sleep(0.3)
    
    print(f"\n{Color.MAGENTA}Woody Allen once said...{Color.RESET}\n")
    time.sleep(1)
    
    # Print the quote with typing effect and box
    box_text(quote)
    
    print(f"\n{Color.WHITE}(or at least he would have, if he were even more neurotic){Color.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Anxiety interrupted.{Color.RESET}")
        sys.exit()