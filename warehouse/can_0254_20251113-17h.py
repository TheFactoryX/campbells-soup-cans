"""
Campbell's Soup Can #254
Produced: 2025-11-13 17:33:53
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
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
import os

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
ORANGE = '\033[38;5;208m'   # orange-ish

# The quote – a single Woody‑Allen–style line
QUOTE = ("I think the universe is a grand joke: it was created to give me a huge existential punchline "
         "and yet I'm still trying to find the punch.")

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def spinner(duration=3.0):
    """Display a simple spinner animation for `duration` seconds."""
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    sys.stdout.write('  ')
    while time.time() < end_time:
        for ch in symbols:
            sys.stdout.write('\r' + ORANGE + ch + RESET + '  Thinking…')
            sys.stdout.flush()
            time.sleep(0.125)

def typewriter(text, delay=0.06):
    """Print `text` one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    # 1. Show a spinner while we “think”
    spinner(3.0)

    # 2. Clear screen, then show a colored box with animated quote
    clear_screen()

    # Build quote box
    inner_width = len(QUOTE) + 2          # two side spaces
    top = f"{BOLD}{ORANGE}╔{'═' * inner_width}╗{RESET}"
    bottom = f"{BOLD}{ORANGE}╚{'═' * inner_width}╝{RESET}"
    left_border = f"{BOLD}{ORANGE}║ "
    right_border = f" ║{RESET}"

    print(top)
    # Start the line with left border and a space
    sys.stdout.write(left_border)
    sys.stdout.flush()
    # Typewriter reveal of the quote
    typewriter(QUOTE, delay=0.04)
    # Print right border
    sys.stdout.write(right_border)
    sys.stdout.flush()
    print(bottom)

if __name__ == "__main__":
    main()
