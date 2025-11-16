"""
Campbell's Soup Can #319
Produced: 2025-11-16 16:35:41
Worker: Anthropic: Claude 3.7 Sonnet (anthropic/claude-3.7-sonnet)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys
from math import sin, cos, pi
import itertools
import threading

# Define ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Woody Allen style quote
quote = "I've figured out the meaning of life, but now I can't remember where I put the note. That's the trouble with existential breakthroughs - they're never around when you need them."

# Fancy border for the quote
def create_border(width, height):
    top = "╭" + "─" * width + "╮"
    middle = "│" + " " * width + "│"
    bottom = "╰" + "─" * width + "╯"
    return [top] + [middle] * height + [bottom]

# Function to wrap text to fit within a width
def wrap_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return lines

# Spinning cursor animation for fun
def spinning_cursor():
    cursor = itertools.cycle(['|', '/', '-', '\\'])
    while not done:
        sys.stdout.write(next(cursor))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

# Create a typing effect for text
def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Main display
def main():
    global done
    done = False
    
    # Start spinner in a separate thread
    spinner = threading.Thread(target=spinning_cursor)
    spinner.daemon = True
    spinner.start()
    
    # Clear screen and set initial position
    print("\033[2J\033[H", end="")
    time.sleep(1)
    
    # Show a Woody Allen-esque intro
    type_text(f"{YELLOW}Thoughts from a neurotic mind...{RESET}\n\n")
    time.sleep(1)
    
    # Stop the spinner
    done = True
    time.sleep(0.5)
    
    # Prepare the quote in a fancy box
    width = 50
    wrapped_quote = wrap_text(quote, width - 4)
    height = len(wrapped_quote)
    
    border = create_border(width, height)
    
    # Display the quote with animated colors
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    
    # Print top border
    print(f"{random.choice(colors)}{border[0]}{RESET}")
    
    # Print quote with padding
    for i, line in enumerate(wrapped_quote):
        padding = (width - len(line)) // 2
        print(f"{random.choice(colors)}{border[i+1][0]}{' ' * padding}{BOLD}{WHITE}{line}{RESET}{random.choice(colors)}{' ' * (width - padding - len(line))}{border[i+1][-1]}{RESET}")
    
    # Print bottom border
    print(f"{random.choice(colors)}{border[-1]}{RESET}")
    
    # Print signature
    time.sleep(0.5)
    print(f"\n{CYAN}~ Woody Allen (probably){RESET}")
    
    # Draw some glasses as a finishing touch
    time.sleep(0.7)
    glasses = [
        "    _______________         _______________",
        "   /               \\       /               \\",
        "  /                 \\     /                 \\",
        " |                   |   |                   |",
        " |                   |   |                   |",
        "  \\                 /     \\                 /",
        "   \\_______________/       \\_______________/"
    ]
    
    for line in glasses:
        print(f"{YELLOW}{line}{RESET}")
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        sys.exit(0)