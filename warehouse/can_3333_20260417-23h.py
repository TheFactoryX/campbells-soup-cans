"""
Campbell's Soup Can #3333
Produced: 2026-04-17 23:56:04
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
A tiny, colorful, animated console demo that prints a single
Woody‑Allen‑style neurotic philosophical quote.

Run: python3 this_file.py
"""

import sys
import time
import itertools
import shutil

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
CSI = "\033["
RESET = CSI + "0m"

def color(text: str, fg: int = 37, bg: int = 40, style: int = 0) -> str:
    """Return *text* wrapped in an ANSI colour/style sequence."""
    return f"{CSI}{style};{fg};{bg}m{text}{RESET}"

def rainbow_cycle():
    """Yield an infinite cycle of foreground colour codes."""
    # 31‑36 are red, green, yellow, blue, magenta, cyan
    for fg in itertools.cycle([31, 33, 32, 36, 35, 34]):
        yield fg

# ----------------------------------------------------------------------
# Layout helpers
# ----------------------------------------------------------------------
def box_around(lines, padding=1, border="*"):
    """Return *lines* (list of strings) surrounded by a simple ASCII box."""
    width = max(len(line) for line in lines) + padding * 2
    top_bottom = border * (width + 2)
    padded = [f"{border}{' '*padding}{line.ljust(width)}{' '*padding}{border}"
              for line in lines]
    return [top_bottom] + padded + [top_bottom]

def center_text(text):
    """Center *text* in the current terminal width."""
    term_width = shutil.get_terminal_size((80, 20)).columns
    return text.center(term_width)

# ----------------------------------------------------------------------
# The quote – feel free to edit
# ----------------------------------------------------------------------
QUOTE = (
    "I’m convinced the meaning of life is just a series of awkward "
    "silences, punctuated by the sound of my own stomach growling."
)

# ----------------------------------------------------------------------
# Main animation
# ----------------------------------------------------------------------
def main():
    # Prepare a static art piece (a tiny, neurotic brain)
    brain_art = [
        "   ,/////,",
        "  /      \\",
        " |  .-.  |   *thinking*",
        " | (   ) |",
        "  \\ '--' /",
        "   `----'"
    ]

    # Build the final picture: brain + quote in a box
    boxed_quote = box_around([QUOTE])
    picture = brain_art + [""] + boxed_quote

    # Animation: slowly reveal line by line with a rainbow hue
    color_cycle = rainbow_cycle()
    for i, line in enumerate(picture):
        fg = next(color_cycle)
        sys.stdout.write(color(center_text(line), fg=fg) + "\n")
        sys.stdout.flush()
        time.sleep(0.3)

    # Final flourish: blink the whole thing a couple of times
    for _ in range(3):
        sys.stdout.write(CSI + "5m")          # blink on (may not work everywhere)
        time.sleep(0.2)
        sys.stdout.write(RESET)
        time.sleep(0.2)

    # Keep the quote on screen for a moment before exiting
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET)
        sys.exit(0)