"""
Campbell's Soup Can #96
Produced: 2025-11-06 14:35:59
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
RESET = '\x1b[0m'
CYAN = '\x1b[96m'
YELLOW = '\x1b[93m'
GRAY = '\x1b[90m'
RED = '\x1b[91m'
BLINK = '\x1b[5m'

# The Woody‑Allen‑style quote
QUOTE = (
    "Life is a tragic comedy, and the most tragic part? "
    "I keep laughing at the wrong punchline."
)

# Simple clear screen
def clear():
    sys.stdout.write('\x1b[2J\x1b[H')
    sys.stdout.flush()

# Function to print a scrolling marquee
def marquee(text, width=80, speed=0.05, repeats=1):
    padded = (' ' * width + text + ' ' * width)
    for _ in range(repeats):
        for i in range(len(padded) - width + 1):
            segment = padded[i:i+width]
            clear()
            sys.stdout.write(f"{YELLOW}{segment}{RESET}\n")
            sys.stdout.flush()
            time.sleep(speed)

# Function to display a stylized boxed quote with a spinner
def boxed_quote(quote):
    border_len = len(quote) + 2
    top_bottom = f"{GRAY}+{'-'*border_len}+{RESET}"
    middle = f"{GRAY}|{RESET} {CYAN}{quote}{RESET} {GRAY}|{RESET}"
    clear()
    sys.stdout.write(f"{top_bottom}\n{middle}\n{top_bottom}\n")
    sys.stdout.flush()
    # Simple spinner animation
    spinner_cycle = '|/-\\'
    for _ in range(12):
        for ch in spinner_cycle:
            sys.stdout.write(f"\r{RED}Loading {ch}{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 15 + '\r')
    sys.stdout.flush()

def main():
    # Scroll the quote across the screen once
    marquee(QUOTE, width=80, speed=0.08, repeats=1)
    # Show the quote in a colorful box with a spinner
    boxed_quote(QUOTE)
    # Final fade out effect
    for brightness in range(10, 0, -1):
        clear()
        sys.stdout.write(f"\x1b[38;2;{brightness*20};{brightness*5};{brightness*15}m{QUOTE}{RESET}\n")
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
