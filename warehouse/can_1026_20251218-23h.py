"""
Campbell's Soup Can #1026
Produced: 2025-12-18 23:31:23
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

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
RED     = "\033[91m"

# A simple typewriter effect
def type_print(text, delay=0.04, color=YELLOW):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Draw a simple ASCII theater frame
def draw_frame(content_lines):
    width = max(len(line) for line in content_lines) + 4
    horizontal = "+" + "-" * (width - 2) + "+"
    top = RED + horizontal + RESET
    bottom = top
    framed = [top]
    for line in content_lines:
        framed.append("| " + line.ljust(width - 4) + " |")
    framed.append(bottom)
    return "\n".join(framed)

def main():
    # Header
    header = f"{BOLD}{CYAN}Woody Allen's Theatrical Stage{RESET}"
    type_print(header, delay=0.07)

    # Quote in Woody Allen style
    quote = (
        "I keep asking whether the universe is a joke\n"
        "and the only answer it gives is \"shrug\", \n"
        "followed by a punchline you just can't see."
    )
    # Split quote into lines for the frame
    quote_lines = quote.split('\n')
    frame = draw_frame(quote_lines)

    type_print(frame, delay=0.005, color=MAGENTA)

    # A little blinking cursor at the end
    cursor_animations = ["_", "‾", "~", "≠"]
    for _ in range(8):
        for cursor in cursor_animations:
            sys.stdout.write(f"\r{BOLD}{YELLOW}{cursor}{RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
    sys.stdout.write("\r   \n")  # clear cursor line

if __name__ == "__main__":
    main()