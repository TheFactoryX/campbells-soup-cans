"""
Campbell's Soup Can #317
Produced: 2025-11-16 14:30:51
Worker: OpenAI: o3 (openai/o3)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen–esque one-liner with a splash of color and animation.
import sys
import time
import itertools
import shutil

# ANSI helpers
RESET = "\033[0m"
BOLD = "\033[1m"
COLORS = ["31", "32", "33", "34", "35", "36"]  # red, green, yellow, blue, magenta, cyan


def center(text):
    """Center text based on terminal width (fallback to 80)."""
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)


def rainbow_print(lines, delay=0.05):
    """Print each line in a different color."""
    for color, line in zip(itertools.cycle(COLORS), lines):
        sys.stdout.write(f"{BOLD}\033[{color}m{center(line)}{RESET}\n")
        sys.stdout.flush()
        time.sleep(delay)


def thinking(duration=2.0):
    """Small 'thinking...' spinner."""
    spinner = itertools.cycle("∙●")
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{BOLD}\033[90mpondering {next(spinner)} {RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 40 + "\r")  # clear line


def typewriter(text, delay=0.04, color="33"):
    """Typewriter-style printing of the quote."""
    sys.stdout.write(BOLD)
    for ch in text:
        sys.stdout.write(f"\033[{color}m{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay if ch != " " else delay / 4)
    sys.stdout.write("\n")


ASCII_WOODY = [
    r"        _____   ",
    r"      .'     '. ",
    r"     /  O   O  \ ",
    r"    |     ^     |",
    r"    |  \_____/  |",
    r"     \         / ",
    r"      '._____.'  "
]

QUOTE = (
    "I tried having an existential crisis once, "
    "but my hypochondria kept interrupting with more urgent bulletins."
)

if __name__ == "__main__":
    rainbow_print(ASCII_WOODY, delay=0.1)
    thinking()
    typewriter(QUOTE)