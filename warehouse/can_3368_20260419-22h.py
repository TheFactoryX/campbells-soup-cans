"""
Campbell's Soup Can #3368
Produced: 2026-04-19 22:56:10
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import itertools

# ANSI escape codes
RESET  = "\x1b[0m"
BOLD   = "\x1b[1m"
CYAN   = "\x1b[36m"
YELLOW = "\x1b[33m"
MAGENTA = "\x1b[35m"
RED    = "\x1b[31m"

quote = (
    f"{BOLD}{CYAN}I don't think that I have a fear of death. "
    f"Instead, I think my biggest existential black hole might be "
    f"me not realizing that the theater of my life is an elaborate "
    f"set that has been rehearsed for twenty minutes by a nervous "
    f"tech crew named Anxiety.{RESET}"
)

# a simple animation: rotating box around the quote
frames = [
    f"{MAGENTA}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}",
    f"{MAGENTA}┃{RESET}",
    f"{MAGENTA}┃{RESET}  {YELLOW}{quote}{RESET}",
    f"{MAGENTA}┃{RESET}",
    f"{MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}",
]

# Build a moving dot sequence
dots = ['   ', '.  ', '.. ', '...']

def clear_line():
    sys.stdout.write("\r\x1b[2K")  # carriage return, clear line

for _ in range(30):
    for frame, dot in itertools.product(frames, dots):
        clear_line()
        sys.stdout.write(f"{frame} {dot}")
        sys.stdout.flush()
        time.sleep(0.02)
    # Move to next cycle
    sys.stdout.write("\n")