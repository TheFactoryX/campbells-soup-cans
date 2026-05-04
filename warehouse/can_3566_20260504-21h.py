"""
Campbell's Soup Can #3566
Produced: 2026-05-04 21:19:51
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

"""
A tiny, self‑contained program that prints a single, Woody‑Allen‑style
philosophical quip with a splash of color and a little “typewriter”
animation. No external packages required.
"""

import sys
import time
import itertools

# ANSI escape codes for colors & styles
RESET = "\033[0m"
BOLD = "\033[1m"
FG_CYAN = "\033[36m"
FG_MAGENTA = "\033[35m"
FG_YELLOW = "\033[33m"
FG_GREEN = "\033[32m"

# The quote – neurotic, self‑deprecating, existential
QUOTE = (
    f"{FG_CYAN}“I{FG_MAGENTA}'{FG_CYAN}m not afraid of dying; "
    f"{FG_GREEN}I{FG_MAGENTA}'{FG_GREEN}m just terrified of the "
    f"{FG_YELLOW}waiting{FG_MAGENTA} line in the afterlife—"
    f"{FG_CYAN}and I{FG_MAGENTA}'{FG_CYAN}m pretty sure I{FG_MAGENTA}'{FG_CYAN}ll be "
    f"late again.”"
)

# A pretty border made of ASCII art
BORDER = f"{FG_MAGENTA}" + "─" * 72 + RESET
TOP = f"{FG_MAGENTA}╭{BORDER}╮{RESET}"
BOT = f"{FG_MAGENTA}╰{BORDER}╯{RESET}"

def typewriter(text: str, delay: float = 0.04) -> None:
    """Print `text` one character at a time, like a typewriter."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Slightly faster for spaces to keep the rhythm pleasant
        time.sleep(delay if ch != " " else delay * 0.5)
    sys.stdout.write("\n")

def blinking_cursor(duration: float = 0.8, interval: float = 0.2) -> None:
    """Show a brief blinking cursor after the quote."""
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write("\033[7m \033[0m")  # reverse video space as cursor
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\b \b")          # erase cursor
        sys.stdout.flush()
        time.sleep(interval)

def main() -> None:
    # Center the quote within the border width
    inner_width = 70
    lines = [QUOTE[i:i+inner_width] for i in range(0, len(QUOTE), inner_width)]

    print(TOP)
    for line in lines:
        # Pad each line to exactly inner_width characters (ignoring ANSI codes)
        visible_len = len(line.replace("\033", "").replace("[", "").replace("m", ""))
        pad = " " * (inner_width - visible_len)
        typewriter(f"{FG_MAGENTA}│{RESET} " + line + pad + f" {FG_MAGENTA}│{RESET}")
    print(BOT)

    # A little wink after the quote
    blinking_cursor()

if __name__ == "__main__":
    main()