"""
Campbell's Soup Can #3572
Produced: 2026-05-05 11:38:13
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

# ANSI escape codes for colors
COLORS = [
    '\033[31m',  # red
    '\033[33m',  # yellow
    '\033[32m',  # green
    '\033[36m',  # cyan
    '\033[34m',  # blue
    '\033[35m',  # magenta
]
RESET = '\033[0m'

# The funny Woody‑Allen‑style philosophical quote
QUOTE = (
    "I think the secret of life is that I'm terrified of becoming "
    "the very philosopher who wrote the punchline about my own doom."
)

# Simple ASCII art frame
FRAME_TOP = "┌" + "─" * (len(QUOTE) + 4) + "┐"
FRAME_BOTTOM = "└" + "─" * (len(QUOTE) + 4) + "┘"

# Make a sparkling gradient effect
def sparkle_line(line: str) -> str:
    result = ""
    for i, ch in enumerate(line):
        color = COLORS[i % len(COLORS)]
        result += f"{color}{ch}{RESET}"
    return result

def main():
    # Clear the screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print the framed quote with sparkle
    print(sparkle_line(FRAME_TOP))
    print(f"│  {QUOTE}  │")
    print(sparkle_line(FRAME_BOTTOM))

    # Animate a tiny “thinking” bubble
    bubble = ['   ', '   ', '   ', '   ']
    for _ in range(30):
        # Move bubble up and down
        for frame in ["(  )", "( y )", "(  )", "( )"]:
            sys.stdout.write("\033[s")                       # Save cursor
            sys.stdout.write("\033[10;10H")                 # Move cursor to (10,10)
            sys.stdout.write(frame)                         # Draw bubble
            sys.stdout.write("\033[u")                       # Restore cursor
            sys.stdout.flush()
            time.sleep(0.15)

    # Final chime
    sys.stdout.write("\033[10;10H")  # Move cursor to bubble position
    sys.stdout.write("~")            # Boom
    sys.stdout.flush()

if __name__ == "__main__":
    main()