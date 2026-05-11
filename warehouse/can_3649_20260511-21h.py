"""
Campbell's Soup Can #3649
Produced: 2026-05-11 21:41:27
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, os
import random

# ANSI escape codes
CLEAR = "\u001b[2J"
CURSOR_HOME = "\u001b[H"
RESET = "\u001b[0m"
BOLD = "\u001b[1m"
ITALIC = "\u001b[3m"
INVERSE = "\u001b[7m"

# Colors palette
COLORS = [
    "\u001b[31m",  # red
    "\u001b[32m",  # green
    "\u001b[33m",  # yellow
    "\u001b[34m",  # blue
    "\u001b[35m",  # magenta
    "\u001b[36m",  # cyan
]

QUOTE = (
    "\"I keep asking myself what the point of my existence is, "
    "but then I remember that the answer is probably the same as everyone else's: "
    "tomatoes are red, my parents argue, and I have a terrible sense of humor.\"\n\n"
    "- Woody Allen (self‑pronounced)"
)

def box_lines(text, width):
    """Return a list of lines forming a simple colorful box around the text."""
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    border_len = max_len + 4  # 2 spaces padding each side
    top = "┌" + "─" * border_len + "┐"
    bottom = "└" + "─" * border_len + "┘"
    padded = [f"│  {line.ljust(max_len)}  │" for line in lines]
    return [top] + padded + [bottom]

def animate_frame(color, frame_num):
    os.system('')  # enable ANSI on Windows
    sys.stdout.write(CLEAR + CURSOR_HOME)
    sys.stdout.write(color + BOLD)
    sys.stdout.write("\n" * 2)
    for i, line in enumerate(box_lines(QUOTE, 60)):
        # shift lines up and down for a wobbly effect
        shift = random.choice([-1, 0, 1])
        sys.stdout.write(" " * (i * 2 + shift) + line + "\n")
    sys.stdout.write(RESET)
    sys.stdout.flush()

def main():
    try:
        for frame in range(120):  # about 4 seconds @ 30fps
            color = random.choice(COLORS)
            animate_frame(color, frame)
            time.sleep(0.033)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(CLEAR + CURSOR_HOME + RESET)
        sys.stdout.flush()

if __name__ == "__main__":
    main()
