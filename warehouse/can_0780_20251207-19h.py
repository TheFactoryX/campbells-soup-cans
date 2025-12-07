"""
Campbell's Soup Can #780
Produced: 2025-12-07 19:25:58
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ANSI color codes
RESET  = '\033[0m'
YELLOW = '\033[93m'
CYAN   = '\033[96m'
BLUE   = '\033[94m'
MAGENTA = '\033[95m'

# The Woody‑Allen‑style quote
QUOTE = (
    "I thought I was searching for meaning; "
    "I was just looking for a coffee shop that charges "
    "for existential dread on the side."
)

# ──────────────────────────────────────────────────────
def typewriter(text, delay=0.04, color=YELLOW):
    """Prints text with a typewriter effect."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != '\n':
            time.sleep(delay)
    sys.stdout.write(RESET + '\n')

# ──────────────────────────────────────────────────────
def print_bordered_quote(quote):
    margin = 4
    width  = len(quote) + margin * 2
    border_top_bottom = BLUE + '+' + '-' * width + '+' + RESET
    empty_line = BLUE + '|' + ' ' * width + '|' + RESET

    print(border_top_bottom)
    print(empty_line)
    # Print quote centered
    left = (width - len(quote)) // 2
    line = BLUE + '|' + ' ' * left + QUOTE + ' ' * (width - left - len(quote)) + '|' + RESET
    print(line)
    print(empty_line)
    print(border_top_bottom)

# ──────────────────────────────────────────────────────
def coffee_cup():
    cup = (
        f"{CYAN}      (  )\n"
        f"      (   )\n"
        f"      (   )\n"
        f"     {'\\\\/' if True else ''}\n"
        f"      /\\\n"
        f"     /__\\\n"
        f"{MAGENTA}   (\"\"\"\")\n"
        f"{MAGENTA}    \"\"\"\"\n"
    )
    typewriter(cup, delay=0.02, color=CYAN)

# ──────────────────────────────────────────────────────
def spinner(msg="Thinking", duration=3.0):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{msg} {chars[i % len(chars)]}')
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(msg) + 2) + '\r')  # clear line

# ──────────────────────────────────────────────────────
def main():
    print_bordered_quote(QUOTE)
    coffee_cup()
    spinner(duration=2.5)
    typewriter("Enjoy your existential coffee!", color=YELLOW)

if __name__ == "__main__":
    main()