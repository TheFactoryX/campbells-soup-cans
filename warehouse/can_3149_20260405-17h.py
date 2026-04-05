"""
Campbell's Soup Can #3149
Produced: 2026-04-05 17:49:15
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
A tiny, colorful, animated Woody‑Allen‑style philosophical quote printer.
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI colour codes (foreground)
# ----------------------------------------------------------------------
FG = {
    "reset": "\033[0m",
    "red":   "\033[31m",
    "green": "\033[32m",
    "yellow":"\033[33m",
    "blue":  "\033[34m",
    "magenta":"\033[35m",
    "cyan":  "\033[36m",
    "white": "\033[37m",
    "bright_black":"\033[90m",
    "bright_red":"\033[91m",
    "bright_green":"\033[92m",
    "bright_yellow":"\033[93m",
    "bright_blue":"\033[94m",
    "bright_magenta":"\033[95m",
    "bright_cyan":"\033[96m",
    "bright_white":"\033[97m",
}

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑style, neurotic and self‑deprecating)
# ----------------------------------------------------------------------
QUOTE = (
    "I have a deep, abiding love for the universe, "
    "but I'm pretty sure it's only using me as a stand‑in for a lab rat."
)

# ----------------------------------------------------------------------
# Helper: typewriter‑style printing with colour
# ----------------------------------------------------------------------
def type_print(text: str, colour: str = "bright_cyan", delay: float = 0.03) -> None:
    """Print *text* one character at a time in *colour*."""
    for ch in text:
        sys.stdout.write(FG[colour] + ch + FG["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


# ----------------------------------------------------------------------
# Build a colourful box around the quote
# ----------------------------------------------------------------------
def boxed_quote(quote: str) -> list[str]:
    """Return a list of strings that draws the quote inside an ASCII box."""
    # Padding around the text
    pad = 2
    inner_width = len(quote) + pad * 2

    top    = "┌" + "─" * inner_width + "┐"
    middle = "│" + " " * pad + quote + " " * pad + "│"
    bottom = "└" + "─" * inner_width + "┘"
    return [top, middle, bottom]


# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    lines = boxed_quote(QUOTE)

    # Choose a colour for each line – a subtle rainbow
    colours = ["bright_magenta", "bright_cyan", "bright_yellow"]
    for line, colour in zip(lines, colours):
        type_print(line, colour, delay=0.02)

    # Small pause before exiting, so the user can enjoy the glow
    time.sleep(0.8)


if __name__ == "__main__":
    main()