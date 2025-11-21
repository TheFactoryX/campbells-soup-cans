"""
Campbell's Soup Can #413
Produced: 2025-11-21 02:13:54
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

"""
Playful Woody Allen quote with colors, ASCII art frame, and typewriter animation.
"""

import sys
import time
import random
import re

# The quirky Woody Allen styled philosophical quote
QUOTE = "I keep hoping the universe will give me meaning like a good punchline, but so far it’s only sending me spam emails."

# ANSI color codes
COLORS = ['\033[91m',  # red
          '\033[92m',  # green
          '\033[93m',  # yellow
          '\033[94m',  # blue
          '\033[95m',  # magenta
          '\033[96m']  # cyan
RESET = '\033[0m'
CYAN = '\033[94m'
YELLOW = '\033[93m'

# Randomly color each word in the quote
words = QUOTE.split()
colored_words = [f"{random.choice(COLORS)}{w}{RESET}" for w in words]
colored_quote = ' '.join(colored_words)

# Compute visible length of the quote (without ANSI codes)
visible_len = len(re.sub(r'\x1b\[[0-9;]*m', '', colored_quote))
frame_width = visible_len + 4  # 2 stars + 2 spaces
border = '*' * frame_width

# Header
header = "💡🤔 A Woody Allen Quirky Quote 🤔💡"
print(f"{YELLOW}{header.center(frame_width)}{RESET}\n")

# Typewriter function
def typewriter(text: str, delay: float = 0.04):
    """Print `text` letter by letter with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

# Print the top border
print(f"{CYAN}{border}{RESET}")

# Print the left side star and a space, then the quote, then the right side star
print(f"{CYAN}*{RESET} ", end='')
typewriter(colored_quote, 0.05)
print(f" {CYAN}*{RESET}")

# Print the bottom border
print(f"{CYAN}{border}{RESET}")