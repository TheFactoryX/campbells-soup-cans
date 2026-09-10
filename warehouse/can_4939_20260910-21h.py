"""
Campbell's Soup Can #4939
Produced: 2026-09-10 21:38:21
Worker: Nex AGI: Nex-N2.5-Mini (free) (nex-agi/nex-n2.5-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import random
import sys
import textwrap
import time
from shutil import get_terminal_size


try:
    terminal_width = min(max(get_terminal_size().columns, 64), 80)
    terminal_height = max(get_terminal_size().rows, 18)
except (AttributeError, ValueError):
    terminal_width, terminal_height = 78, 24

RESET = "\033[0m"
DIM = "\033[2m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GRAY = "\033[90m"

quote = (
    "Life is a terrifying, meaningless accident - and somehow, despite my "
    "outstanding credentials for panic, I keep showing up."
)


def color(line, code):
    return f"{code}{line}{RESET}" if code else line


def render_quote(progress):
    usable = max(52, min(72, terminal_width - 6))
    full_lines = textwrap.wrap(
        quote, width=usable - 8, break_long_words=False, break_on_hyphens=False
    )
    card_width = min(max(map(len, full_lines)) + 8, terminal_width - 2)
    content_width = card_width - 4

    lines = textwrap.wrap(
        quote[:progress],
        width=content_width,
        break_long_words=False,
        break_on_hyphens=False,
    ) or [""]

    border = "─" * card_width
    card = [
        color(f"╭{border}╮", MAGENTA),
        color(f"│{DIM}{' ' * card_width}{RESET}│", YELLOW),
    ]
    card.extend(color(f"│{' ' * 2}{line:<{content_width - 4}}{' ' * 2}│", CYAN) for line in lines)
    card.extend(
        [
            color(f"│{DIM}{' ' * card_width}{RESET}│", YELLOW),
            color(f"╰{border}╯", MAGENTA),
        ]
    )

    sys.stdout.write("\033[H\033[J")
    for _ in range(max(0, (terminal_height - len(card)) // 2)):
        sys.stdout.write("\n")
    sys.stdout.write("\n".join(card))
    sys.stdout.write("\033[0m")
    sys.stdout.flush()


def cosmic_dream():
    for tick in range(18):
        sys.stdout.write("\033[H\033[2J")
        field = [" "] * (terminal_width * terminal_height)
        for _ in range(20):
            x = random.randrange(terminal_width)
            y = random.randrange(terminal_height)
            field[y * terminal_width + x] = random.choice(".*:+-<>")
        for y in range(terminal_height):
            sys.stdout.write("".join(field[y * terminal_width : (y + 1) * terminal_width]) + "\n")
        sys.stdout.write(
            f"\n{GRAY}Consulting the cosmos... {tick + 1}/18{RESET}\n\n"
        )
        sys.stdout.flush()
        time.sleep(0.035)


if __name__ == "__main__":
    cosmic_dream()
    for character in range(len(quote) + 1):
        render_quote(character)
        time.sleep(0.025)
    render_quote(len(quote))
    time.sleep(0.25)
    print(f"{GRAY}Existential conclusion reached.{RESET}")