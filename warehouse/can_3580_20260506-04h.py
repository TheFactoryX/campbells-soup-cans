"""
Campbell's Soup Can #3580
Produced: 2026-05-06 04:05:35
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
A single‑file, no‑dependency program that prints a
Woody‑Allen‑style philosophical quote in a playful,
animated, colored box.
"""

import sys
import time
import shutil

# ANSI escape codes for styling
RESET   = "\x1b[0m"
BOLD    = "\x1b[1m"
ITAL    = "\x1b[3m"

# Colors
RED     = "\x1b[31m"
GREEN   = "\x1b[32m"
YELLOW  = "\x1b[33m"
BLUE    = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN    = "\x1b[36m"
WHITE   = "\x1b[37m"
BRIGHT  = "\x1b[0;97m"

# The quote: a little neurotic, funny, and existential
QUOTE = (
    "I keep trying to make sense of the universe, "
    "but the universe keeps saying, 'Are you kidding me?'" 
)

# Build a box around the quote
def build_box(text, padding=1, color=BLUE):
    lines = text.splitlines()
    width = max(len(line) for line in lines) + 2 * padding
    top = f"{color}+{'-' * width}+{RESET}"
    bottom = top
    boxed = [top]
    for line in lines:
        padded = ' ' * padding + line + ' ' * (width - len(line) - padding)
        boxed.append(f"{color}|{RESET}{padded}{color}|{RESET}")
    boxed.append(bottom)
    return boxed

# Animate horizontal scrolling
def scroll(boxed_lines, delay=0.08):
    max_len = max(len(line) for line in boxed_lines)
    width, _ = shutil.get_terminal_size(fallback=(80, 24))
    total = width + max_len + 2  # padding to clear line
    for offset in range(total):
        for line in boxed_lines:
            sys.stdout.write('\r' + line[max_len - offset : max_len - offset + width] + ' ' * (width - len(line[max_len - offset : max_len - offset + width])))
        sys.stdout.flush()
        time.sleep(delay)
        # Move to next line after each frame
        sys.stdout.write('\x1b[1A')
    sys.stdout.write('\n')

def main():
    boxed = build_box(QUOTE, padding=2, color=CYAN)
    # Create a banner header
    header = f"{MAGENTA}{BOLD}Woody‑Allen Monologue{RESET}"
    print(header.center(80))
    scroll(boxed, delay=0.07)

if __name__ == "__main__":
    main()
