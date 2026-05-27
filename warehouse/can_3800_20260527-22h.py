"""
Campbell's Soup Can #3800
Produced: 2026-05-27 22:11:12
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
A tiny animated, colored showcase for a single Woody‑Allen‑style
philosophical joke.  No external packages required – just the standard
library and ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# A palette of bright colours (foreground)
COLORS = [
    "\033[38;5;208m",  # orange
    "\033[38;5;45m",   # cyan
    "\033[38;5;82m",   # green
    "\033[38;5;129m",  # pink
    "\033[38;5;226m",  # yellow
]

def color_cycle(text):
    """Yield the text repeatedly, each time wrapped in the next colour."""
    for col in itertools.cycle(COLORS):
        yield f"{col}{text}{RESET}"

# ----------------------------------------------------------------------
# Fancy box drawing – uses Unicode box‑drawing characters
# ----------------------------------------------------------------------
def make_box(lines, padding=2):
    """Return a list of strings forming a boxed version of `lines`."""
    # Determine the longest printable line (ignore ANSI codes)
    def strip_ansi(s):
        import re
        return re.sub(r"\x1b\[[0-9;]*m", "", s)

    max_len = max(len(strip_ansi(l)) for l in lines)
    inner_width = max_len + padding * 2

    top    = "┏" + "━" * inner_width + "┓"
    bottom = "┗" + "━" * inner_width + "┛"
    boxed = [top]
    for l in lines:
        stripped = strip_ansi(l)
        space = inner_width - len(stripped)
        left_pad = padding
        right_pad = space - left_pad
        boxed.append(f"┃{' ' * left_pad}{l}{' ' * right_pad}┃")
    boxed.append(bottom)
    return boxed

# ----------------------------------------------------------------------
# The quote – feel free to edit!
# ----------------------------------------------------------------------
quote = (
    "I think the meaning of life is to find meaning "
    "in the fact that we’ll never really understand it…"
)

# Break into words for a simple “typewriter” effect
words = quote.split()

# ----------------------------------------------------------------------
# Main animation loop
# ----------------------------------------------------------------------
def main():
    # Prepare coloured words generator
    coloured_words = list(color_cycle(" ".join(words)))
    # We'll reveal the quote word‑by‑word
    displayed = []
    for i, word in enumerate(words):
        # Append the next coloured word (with a trailing space)
        displayed.append(coloured_words[i])
        # Build current line(s)
        line = BOLD + " ".join(displayed) + RESET
        # Center the line within an 80‑character width for visual appeal
        centered = line.center(80)
        # Build the box and print it
        box = make_box([centered])
        sys.stdout.write("\033[H\033[2J")   # clear screen
        sys.stdout.write("\n".join(box) + "\n")
        sys.stdout.flush()
        time.sleep(0.35)   # pause for drama

    # Hold the final picture for a moment before exiting
    time.sleep(2)

if __name__ == "__main__":
    # Enable a sane terminal size on Windows (no‑op on *nix)
    try:
        import os, msvcrt, ctypes
        if os.name == "nt":
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

    main()