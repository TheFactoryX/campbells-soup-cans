"""
Campbell's Soup Can #830
Produced: 2025-12-10 04:03:04
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
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
import itertools

# ANSI colour codes
RESET     = "\033[0m"
BRIGHT    = "\033[1m"
DIM       = "\033[2m"
UNDERLINE = "\033[4m"
BLINK     = "\033[5m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Background colours
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

def loading_animation(duration=1.5, steps=3, delay=0.3):
    """Show a simple loading animation while the quote is being prepared."""
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for s in spinner:
            sys.stdout.write(f"\r{YELLOW}{BRIGHT}Preparing your existential punchline... {s}{RESET}")
            sys.stdout.flush()
            time.sleep(delay)

def typewrite(text, speed=0.02, color=CYAN):
    """Print the text one character at a time, like a dramatic typewriter."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

def ascii_box(lines, border_char='*', border_color=GREEN, inner_color=WHITE):
    """Print a coloured ASCII box around a list of lines."""
    max_len = max(len(line) for line in lines)
    top = border_color + border_char * (max_len + 4) + RESET
    sys.stdout.write(top + '\n')
    for line in lines:
        sys.stdout.write(f"{border_color}{border_char} {RESET}" 
                         f"{inner_color}{line.ljust(max_len)}{RESET}" 
                         f"{border_color} {border_char}{RESET}\n")
    sys.stdout.write(top + '\n')

def main():
    quote = ("I keep rehearsing a grand existential soliloquy, "
             "but realize I’m just a neurotic actor missing the punchline.")
    # Show loading animation
    loading_animation()

    # ASCII art header
    header = [
        "  __        ___          __      __ ",
        " / /   ___ / (_) ___ ___/ /__ _ / /__",
        "/ /   / _ \\/ / / @-_-_-_ / -_ `/ / -_",
        "/_/   \\____/_/ /_/ /_/\\_/_/\\_,_/ /_/  ",
    ]
    ascii_box(header, border_char='#', border_color=BLUE, inner_color=BRIGHT+MAGENTA)

    # The quote
    lines = [quote]
    ascii_box(lines, border_char='*', border_color=YELLOW, inner_color=BRIGHT+GREEN)

    # Dramatic typewriter effect for the closing line
    closing = "And that, my friends, is how I philosophically die by accident."
    typewrite(closing, speed=0.03, color=RED)

if __name__ == "__main__":
    main()
