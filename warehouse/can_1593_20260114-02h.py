"""
Campbell's Soup Can #1593
Produced: 2026-01-14 02:33:47
Worker: OpenAI: GPT-3.5 Turbo (older v0613) (openai/gpt-3.5-turbo-0613)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"

FG_RED = "\033[31m"
FG_YELLOW = "\033[33m"
FG_CYAN = "\033[36m"
FG_MAGENTA = "\033[35m"
FG_GREEN = "\033[32m"
FG_WHITE = "\033[37m"

BG_BLUE = "\033[44m"
BG_BLACK = "\033[40m"

CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

# A goofy Woody Allen style quote, original:
quote = (
    "“I'm not saying I'm afraid of the future — I mean, jeez,\n"
    "I can't even decide what to have for lunch,\n"
    "and I'm supposed to plan an existence?\n"
    "This existential anxiety tastes oddly like overcooked chicken.”"
)

# ASCII box drawing characters
TOP_LEFT = '╔'
TOP_RIGHT = '╗'
BOTTOM_LEFT = '╚'
BOTTOM_RIGHT = '╝'
HORIZONTAL = '═'
VERTICAL = '║'

def center_text(text, width):
    lines = text.split('\n')
    res = []
    for line in lines:
        line = line.strip()
        length = len(line)
        if length < width:
            left_padding = (width - length) // 2
            right_padding = width - length - left_padding
            res.append(' ' * left_padding + line + ' ' * right_padding)
        else:
            res.append(line)
    return res


def print_animated_boxed_quote(quote, width=60, delay=0.08):
    lines = center_text(quote, width)

    # Clear screen and move cursor home
    sys.stdout.write(CLEAR_SCREEN + CURSOR_HOME)
    sys.stdout.flush()

    # Draw top border
    top_border = TOP_LEFT + (HORIZONTAL * width) + TOP_RIGHT
    print(BOLD + FG_CYAN + top_border + RESET)

    # Draw empty line with vertical bars
    print(BOLD + FG_CYAN + VERTICAL + RESET + ' ' * width + BOLD + FG_CYAN + VERTICAL + RESET)

    # Animate line printing with rainbow-ish colors
    colors = [FG_RED, FG_YELLOW, FG_GREEN, FG_CYAN, FG_MAGENTA, FG_WHITE]
    color_index = 0

    for line in lines:
        sys.stdout.write(BOLD + FG_CYAN + VERTICAL + RESET + ' ')
        for char in line:
            if char == ' ':
                sys.stdout.write(' ')
            else:
                sys.stdout.write(colors[color_index % len(colors)] + char + RESET)
                color_index += 1
            sys.stdout.flush()
            time.sleep(delay / 8)
        sys.stdout.write(' ' + BOLD + FG_CYAN + VERTICAL + RESET + '\n')
        time.sleep(delay * 3)

    # Draw empty line with vertical bars
    print(BOLD + FG_CYAN + VERTICAL + RESET + ' ' * width + BOLD + FG_CYAN + VERTICAL + RESET)
    # Draw bottom border
    bottom_border = BOLD + FG_CYAN + BOTTOM_LEFT + (HORIZONTAL * width) + BOTTOM_RIGHT + RESET
    print(bottom_border)


def wait_then_fadeout(seconds=5):
    # Cursor hide
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    try:
        time.sleep(seconds)
        # Fade out by clearing line by line "down"
        for i in range(10):
            sys.stdout.write("\033[1A")  # Move cursor up
            sys.stdout.write("\033[K")   # Clear line
            time.sleep(0.2)
    finally:
        # Cursor show
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


def main():
    os.system("")  # Enable ANSI on some Windows terminals
    print_animated_boxed_quote(quote, width=64, delay=0.07)
    wait_then_fadeout(7)
    sys.stdout.write(CLEAR_SCREEN + CURSOR_HOME)
    print(BOLD + FG_YELLOW + "Thanks for contemplating madness with me." + RESET)


if __name__ == "__main__":
    main()