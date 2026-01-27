"""
Campbell's Soup Can #1892
Produced: 2026-01-27 23:34:51
Worker: OpenAI: GPT-4.1 Nano (openai/gpt-4.1-nano)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"
COLOR_WHITE = "\033[37m"
BOLD = "\033[1m"
CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

# Function to clear the terminal
def clear():
    print(CLEAR_SCREEN, end='')

# Function to animate typing effect
def type_text(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Function to draw a fancy box around the quote
def print_boxed_quote(quote_lines):
    width = max(len(line) for line in quote_lines) + 4
    top_bottom = f"{COLOR_CYAN}{'+' + '-'*(width-2) + '+'}{COLOR_RESET}"
    print(top_bottom)
    for line in quote_lines:
        print(f"{COLOR_CYAN}| {COLOR_WHITE}{line.ljust(width-4)} {COLOR_CYAN}|{COLOR_RESET}")
    print(top_bottom)

# Main function
def main():
    try:
        print(HIDE_CURSOR)
        clear()
        # ASCII Art Header
        header = [
            f"{COLOR_MAGENTA}{BOLD}Woody Allen's Existential Snack{COLOR_RESET}"
        ]
        for line in header:
            print(line)
        print()

        # The quote in a styled box
        quote = "I'm not afraid of death; I just don't want to be there when it happens."
        quote_lines = []

        # Wrap quote into lines if needed
        max_width = 60
        words = quote.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= max_width:
                line += " " + word if line else word
            else:
                quote_lines.append(line)
                line = word
        if line:
            quote_lines.append(line)

        # Add some poetic flourish
        print_boxed_quote(quote_lines)
        print()

        # Think bubbles animation
        thoughts = [
            "Is death the ultimate punchline?",
            "Or just the pause before the afterparty?",
            "Maybe I’ll be famous... for dying?"
        ]

        for thought in thoughts:
            # Animate each thought
            print(f"{COLOR_YELLOW}Thinking:{COLOR_RESET} ", end='')
            for ch in thought:
                print(ch, end='', flush=True)
                time.sleep(0.05)
            print()
            time.sleep(0.8)
        print()

        # Self-deprecating note with color splash
        note = f"{BOLD}{COLOR_GREEN}Note to self: I'm happier not knowing the meaning of life. Same goes for my keys.{COLOR_RESET}"
        type_text(note)
        print()

        # End with a wink
        wink = f"{COLOR_RED}{BOLD}Remember: We're all just cosmic jokes waiting for the punchline.{COLOR_RESET}"
        print(wink)
        print()

        # Show some animated stars
        stars = ['*', '+', '.', '✦', '✧']
        print(f"{COLOR_MAGENTA}", end='')
        for _ in range(20):
            print(' ', end='')
            print(stars[os.urandom(1)[0] % len(stars)], end='', flush=True)
            time.sleep(0.05)
        print(f"{COLOR_RESET}")
    finally:
        print(SHOW_CURSOR)

if __name__ == "__main__":
    main()