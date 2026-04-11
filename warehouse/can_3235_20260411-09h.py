"""
Campbell's Soup Can #3235
Produced: 2026-04-11 09:57:37
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
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
import itertools

# ANSI escape codes for colors / styles
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}


def typewriter(text: str, delay: float = 0.04):
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def rainbow_text(text: str):
    """Yield the text with cycling foreground colors."""
    colors = itertools.cycle(FG.values())
    for ch in text:
        yield next(colors) + ch + RESET


def framed(lines):
    """Wrap a list of strings in a simple ASCII box."""
    max_len = max(len(l) for l in lines)
    top = "╔" + "═" * (max_len + 2) + "╗"
    bottom = "╚" + "═" * (max_len + 2) + "╝"
    middle = [f"║ {l.ljust(max_len)} ║" for l in lines]
    return [top] + middle + [bottom]


def main():
    # The Woody‑Allen‑style philosophical gem
    quote = (
        "\"I’m terrified of the meaning of life, "
        "but even more terrified of the day I finally understand it.\""
    )

    # Build the visual layout
    ascii_art = [
        "      .-\"\"\"-.",
        "    .'       `.",
        "   /   .-\"\"-.  \\",
        "  |   /      \\  |",
        "  |  |  () () | |",
        "   \\  \\      /  /",
        "    `. `\"--\"` .'",
        "      `-....-`"
    ]

    # Combine art and quote inside a frame
    framed_content = framed(ascii_art + ["", BOLD + ITALIC + quote + RESET])
    # Print with a gentle fade‑in using rainbow colors
    for line in framed_content:
        colored_line = "".join(rainbow_text(line))
        typewriter(colored_line, delay=0.01)

    # End with a flicker of confetti
    confetti = [FG["magenta"] + "*" + RESET,
                FG["cyan"] + "+" + RESET,
                FG["yellow"] + "." + RESET]
    for _ in range(10):
        sys.stdout.write("\r" + " " * 80)
        sys.stdout.flush()
        sys.stdout.write("\r" + " ".join(itertools.islice(itertools.cycle(confetti), 20)))
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()