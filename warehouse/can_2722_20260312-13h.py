"""
Campbell's Soup Can #2722
Produced: 2026-03-12 13:36:36
Worker: DeepSeek: DeepSeek V3 (deepseek/deepseek-chat)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import shutil

# ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"
COLOR_GREEN = "\033[32m"
COLOR_MAGENTA = "\033[35m"

# Get terminal width for dynamic box sizing
TERMINAL_WIDTH = shutil.get_terminal_size().columns

def print_centered(text, color=COLOR_RESET):
    """Print text centered in the terminal."""
    padding = (TERMINAL_WIDTH - len(text)) // 2
    print(" " * padding + color + text + COLOR_RESET)

def print_boxed(text, color=COLOR_RESET):
    """Print text inside a fancy box."""
    box_width = TERMINAL_WIDTH - 4
    text_lines = text.split('\n')
    print(color + "╭" + "─" * box_width + "╮" + COLOR_RESET)
    for line in text_lines:
        centered_line = line.center(box_width)
        print(color + "│" + centered_line + "│" + COLOR_RESET)
    print(color + "╰" + "─" * box_width + "╝" + COLOR_RESET)

def animate_text(text, delay=0.1):
    """Print text with a typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Clear screen
    print("\033[H\033[J")

    # Print title
    print_centered("Woody Allen's Philosophy", COLOR_MAGENTA)
    print()

    # Animate the quote
    animate_text(COLOR_CYAN + "Thinking..." + COLOR_RESET, 0.1)
    time.sleep(0.5)
    print()
    animate_text(COLOR_GREEN + "Hmm..." + COLOR_RESET, 0.1)
    time.sleep(0.5)
    print()

    # Print the quote in a fancy box
    print_boxed(quote, COLOR_YELLOW)
    print()

    # Print a closing message
    print_centered("Stay neurotic, my friend.", COLOR_RED)

if __name__ == "__main__":
    main()