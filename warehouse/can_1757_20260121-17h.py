"""
Campbell's Soup Can #1757
Produced: 2026-01-21 17:17:21
Worker: OpenAI: GPT-5.2 Chat (openai/gpt-5.2-chat)
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
import shutil

# ANSI colors
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
DIM = "\033[2m"
BOLD = "\033[1m"

quote = (
    "I’m not saying life is meaningless; I’m just saying it keeps sending me bills, "
    "expects optimism, and refuses to explain the syllabus."
)

# Simple typing animation
def type_out(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Get terminal width for centering
width = shutil.get_terminal_size((80, 20)).columns
padding = 4
box_width = min(len(quote) + padding * 2, width - 2)

top = "┌" + "─" * box_width + "┐"
bottom = "└" + "─" * box_width + "┘"

print(DIM + MAGENTA + top.center(width) + RESET)
print(MAGENTA + "│" + " " * box_width + "│".center(width) + RESET)

# Print quote line with animation
content = " " * padding + quote + " " * padding
content = content[:box_width].ljust(box_width)
line = "│" + content + "│"
sys.stdout.write(CYAN)
sys.stdout.write(line.center(width) + "\n")
sys.stdout.write(RESET)

print(MAGENTA + "│" + " " * box_width + "│".center(width) + RESET)
print(DIM + MAGENTA + bottom.center(width) + RESET)

print()
print(YELLOW + BOLD + "— a completely unreliable philosopher" + RESET)