"""
Campbell's Soup Can #3187
Produced: 2026-04-08 03:32:24
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained program that prints a single
Woody‑Allen‑style philosophical quote with a splash of color
and a tiny “typewriter” animation.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time
import shutil

# ----------------------------------------------------------------------
# ANSI color utilities
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some pleasant pastel tones
FG = {
    "violet": "\033[38;5;135m",
    "cyan":   "\033[38;5;87m",
    "yellow": "\033[38;5;221m",
    "white":  "\033[38;5;255m",
}

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑style, neurotic, self‑deprecating)
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is to find a reason to "
    "stay in bed while the universe continues "
    "to pretend it has everything under control."
)

# ----------------------------------------------------------------------
# Helper: print with a typing‑like animation
# ----------------------------------------------------------------------
def type_print(text: str, delay: float = 0.02, **kw):
    """Print `text` one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print(**kw)


# ----------------------------------------------------------------------
# Helper: draw a colorful box around the quote
# ----------------------------------------------------------------------
def boxed_quote(text: str) -> str:
    """Return the quote centred inside a coloured ASCII box."""
    term_width = shutil.get_terminal_size((80, 20)).columns
    pad = 4                           # spaces each side inside the box
    lines = []
    # Split the quote into rough‑size chunks to avoid overflow
    max_len = term_width - (pad + 2) * 2
    words = text.split()
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > max_len:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # Determine box width
    inner_width = max(len(l) for l in lines) + pad * 2
    total_width = inner_width + 2          # side borders

    top = f"{FG['violet']}╔{'═' * inner_width}╗{RESET}"
    bottom = f"{FG['violet']}╚{'═' * inner_width}╝{RESET}"

    lines_formatted = []
    for line in lines:
        space = inner_width - len(line) - pad * 2
        left = " " * pad
        right = " " * (pad + space)
        lines_formatted.append(
            f"{FG['violet']}║{RESET}"
            f"{FG['cyan']}{left}{line}{right}{RESET}"
            f"{FG['violet']}║{RESET}"
        )
    return "\n".join([top] + lines_formatted + [bottom])


# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main():
    # Clear screen (optional, makes the effect nicer)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print a title
    title = f"{BOLD}{FG['yellow']}★  Woody‑Allen‑ish Philosophy  ★{RESET}"
    type_print(title, delay=0.03)
    print()  # blank line

    # Print the boxed quote with a typewriter effect
    boxed = boxed_quote(QUOTE)
    for line in boxed.split("\n"):
        type_print(line, delay=0.015)

    # Finishing flourish
    print()
    type_print(f"{FG['cyan']}— you’ve just wasted a few seconds of existential dread.{RESET}", 0.02)


if __name__ == "__main__":
    main()