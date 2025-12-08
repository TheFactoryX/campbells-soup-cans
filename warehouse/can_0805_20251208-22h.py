"""
Campbell's Soup Can #805
Produced: 2025-12-08 22:34:55
Worker: DeepSeek: DeepSeek V3.2 Speciale (deepseek/deepseek-v3.2-speciale)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random

# ANSI escape codes
RESET = "\033[0m"
BRIGHT_RED = "\033[1;31m"
BRIGHT_GREEN = "\033[1;32m"
BRIGHT_YELLOW = "\033[1;33m"
BRIGHT_BLUE = "\033[1;34m"
BRIGHT_MAGENTA = "\033[1;35m"
BRIGHT_CYAN = "\033[1;36m"
BRIGHT_WHITE = "\033[1;37m"

BRIGHT_COLORS = [
    BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW,
    BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE
]

BORDER_COLOR = "\033[2;37m"      # dim white
TITLE_COLOR = BRIGHT_CYAN
SIGNATURE_COLOR = "\033[2;36m"   # dim cyan

# Box drawing characters
TOP_LEFT = "╭"
TOP_RIGHT = "╮"
BOTTOM_LEFT = "╰"
BOTTOM_RIGHT = "╯"
HORIZONTAL = "─"
VERTICAL = "│"

def wrap_text(text, width=40):
    """Wrap text to the given width, returning a list of lines."""
    words = text.split()
    lines = []
    current = []
    current_len = 0
    for word in words:
        word_len = len(word)
        if current_len + word_len + (1 if current else 0) <= width:
            if current:
                current.append(' ')
                current_len += 1
            current.append(word)
            current_len += word_len
        else:
            lines.append(''.join(current))
            current = [word]
            current_len = word_len
    if current:
        lines.append(''.join(current))
    return lines

def type_string(text, delay=0.05, color=None):
    """Print text with a typewriter effect.
    If `color` is given, use that color; otherwise pick random bright colors per word."""
    if color is not None:
        sys.stdout.write(color)
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(RESET)
    else:
        words = text.split()
        for i, word in enumerate(words):
            c = random.choice(BRIGHT_COLORS)
            sys.stdout.write(c)
            for ch in word:
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write(RESET)
            if i != len(words) - 1:
                sys.stdout.write(' ')
                sys.stdout.flush()
                time.sleep(delay)

def main():
    # Clear screen and move cursor home
    print("\033[2J\033[H", end="")

    # Original Woody Allen style quotes (created for this program)
    quotes = [
        "I'm not saying life is meaningless, but if it were a movie, I'd ask for my money back.",
        "The only thing standing between me and immortality is this pesky habit of breathing.",
        "Existential dread is my constant companion. At least it's loyal.",
        "I've always been afraid of death. But now I'm more afraid of being the last one to die in my family—who will feed my cat?",
        "The universe is expanding, and so is my waistline. At least one of those is under my control.",
        "If God exists, I hope he has a good sense of humor. Otherwise, I'm in trouble."
    ]

    # Choose a random quote
    quote = random.choice(quotes)

    # Wrap the quote to 40 characters per line
    lines = wrap_text(quote, width=40)

    # Determine box dimensions
    max_line_len = max(len(line) for line in lines)
    interior_width = max_line_len + 2          # one space margin on each side
    total_box_width = interior_width + 2       # including the borders

    # Header
    header = "A Woody Allen-esque Philosophical Quote"
    header_padding = max(0, (total_box_width - len(header)) // 2)
    sys.stdout.write(' ' * header_padding)
    type_string(header, delay=0.03, color=TITLE_COLOR)
    print("\n")

    # Top border
    sys.stdout.write(BORDER_COLOR + TOP_LEFT + HORIZONTAL * interior_width + TOP_RIGHT + RESET)
    print()

    # Print each line inside the box
    for line in lines:
        # Left border and left margin
        sys.stdout.write(BORDER_COLOR + VERTICAL + RESET + ' ')
        sys.stdout.flush()

        # Type the line with random colors per word
        type_string(line, delay=0.05, color=None)

        # Fill the remaining space to align the right border
        filler_len = interior_width - (1 + len(line))
        if filler_len > 0:
            sys.stdout.write(' ' * filler_len)

        # Right border
        sys.stdout.write(BORDER_COLOR + VERTICAL + RESET)
        print()

    # Bottom border
    sys.stdout.write(BORDER_COLOR + BOTTOM_LEFT + HORIZONTAL * interior_width + BOTTOM_RIGHT + RESET)
    print("\n")

    # Signature
    signature = "\u2014 In the spirit of Woody Allen"
    sig_padding = max(0, (total_box_width - len(signature)) // 2)
    sys.stdout.write(' ' * sig_padding)
    type_string(signature, delay=0.07, color=SIGNATURE_COLOR)
    print("\n")

    # ASCII art of Woody Allen (simplified)
    woody = [
        "      .-~~~-.",
        "     /       \\",
        "    |  o   o  |",
        "    |    ~    |",
        "     \\  ___  /",
        "      '-----'"
    ]
    for line in woody:
        art_padding = max(0, (total_box_width - len(line)) // 2)
        sys.stdout.write(' ' * art_padding)
        type_string(line, delay=0.04, color=BORDER_COLOR)
        print()
        time.sleep(0.1)

    # Final newline
    print()

if __name__ == "__main__":
    main()