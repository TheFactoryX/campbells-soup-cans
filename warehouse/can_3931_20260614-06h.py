"""
Campbell's Soup Can #3931
Produced: 2026-06-14 06:57:00
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen on Existential Ink - a single-file, visually jazzy demo
"""

import sys
import time
import math

# ANSI escape codes
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
RED = "\033[31m"

# The philosophical Woody-quote
QUOTE = (
    "I think the meaning of life is just to be terrified of the obvious— "
    "and then, when you laugh, realize you also invented the fear."
)

# Simple spinner for dramatic effect
spinner_chars = ['|', '/', '-', '\\']
def spinner(duration=2.0, steps=20):
    interval = duration / steps
    for _ in range(steps):
        for ch in spinner_chars:
            sys.stdout.write(f"\r{GREEN}{ch}{RESET} Loading...")
            sys.stdout.flush()
            time.sleep(interval)
    sys.stdout.write("\r")
    sys.stdout.flush()

# Build an ASCII art box around the quote
def boxed_text(text, cols=60):
    width = min(cols, 80)
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > width - 4:
            lines.append(line.rstrip())
            line = ""
        line += word + " "
    if line:
        lines.append(line.rstrip())

    top = YELLOW + "+" + "-" * (width - 2) + "+" + RESET
    middle = [f"{CYAN}|{RESET} {MAGENTA}{line.ljust(width - 4)}{CYAN} |{RESET}" for line in lines]
    bottom = YELLOW + "+" + "-" * (width - 2) + "+" + RESET
    return "\n".join([top] + middle + [bottom])

# Main routine
def main():
    # Dramatic intro
    print(f"{ITALIC}{BOLD}{YELLOW}Who needs existential dread when you have a terminal?{RESET}\n")
    spinner(duration=3)

    # Print the quote inside an ASCII art frame
    framed = boxed_text(QUOTE, cols=70)
    print(f"{CYAN}{framed}{RESET}\n")

    # Small animation at the end
    for i in range(3):
        print(f"{RED}Thinking...", end='\r', flush=True)
        time.sleep(0.5)
        print(f"{GREEN}Yes, I do think!", end='\r', flush=True)
        time.sleep(0.5)
        print(" " * 20, end='\r')
    print(f"{BOLD}{GREEN}Finished!{RESET}")

if __name__ == "__main__":
    main()