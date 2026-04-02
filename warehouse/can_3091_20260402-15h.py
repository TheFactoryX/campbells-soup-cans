"""
Campbell's Soup Can #3091
Produced: 2026-04-02 15:18:12
Worker: Kwaipilot: KAT-Coder-Pro V2 (kwaipilot/kat-coder-pro-v2)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-inspired philosophical quote generator with visual flair.
Prints a single, original neurotic-existential one-liner with ANSI colors
and ASCII art decorations.
"""

import sys
import time

def print_slow(text, delay=0.02):
    """Print text character by character for a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

    # The quote (original, in Woody Allen's style)
    quote = ("I’m not saying I’m a pessimist, but if I had to choose between "
             "existing and not existing, I’d probably ask for a second opinion "
             "and then still show up late to my own birth.")

    # ASCII art border
    border = "╔" + "═" * 78 + "╗"
    bottom = "╚" + "═" * 78 + "╝"

    # Clear screen (optional, but makes it pop)
    print("\033[2J\033[H", end="")

    # Top decorative line
    print(f"\n{BOLD}{CYAN}{'─' * 20} WOODY ALLEN'S NEUROTIC WISDOM {'─' * 20}{RESET}\n")

    # Print the quote inside a colored box
    print(border)
    # Center the quote roughly
    max_width = 76
    # Wrap the quote if needed (simple wrap at spaces)
    words = quote.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_width:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    lines.append(current)

    for line in lines:
        # Pad the line to fit the box
        padded = line.center(max_width)
        print(f"{BOLD}{YELLOW}║{RESET} {BOLD}{WHITE}{padded}{RESET} {BOLD}{YELLOW}║{RESET}")
    print(bottom)

    # Add a small animated "thinking" cursor
    print(f"\n{DIM}... pondering the absurdity of it all ...{RESET}")
    time.sleep(0.5)
    print(f"{DIM}... still pondering ...{RESET}")
    time.sleep(0.5)
    print(f"{DIM}... maybe it's all just a dream within a dream ...{RESET}")
    time.sleep(0.5)

    # Final punchline in a different color
    print(f"\n{BOLD}{RED}— Woody Allen (probably){RESET}\n")

if __name__ == "__main__":
    main()