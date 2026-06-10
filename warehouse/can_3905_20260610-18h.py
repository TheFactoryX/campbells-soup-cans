"""
Campbell's Soup Can #3905
Produced: 2026-06-10 18:09:18
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
A tiny, self‑contained Python script that prints a single,
Woody‑Allen‑style philosophical joke with a splash of color
and a little “typewriter” animation.

Run it directly:
    $ python3 woody_woes.py
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI color & style helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some nice foreground colors
FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

# ----------------------------------------------------------------------
# The quote (feel free to edit – keep it Woody‑Allen‑ish!)
# ----------------------------------------------------------------------
QUOTE = (
    f"{FG['magenta']}I'm not afraid of death;{RESET} "
    f"{FG['cyan']}I just don't want to be there{RESET} "
    f"{FG['yellow']}when it happens.{RESET}"
)

# ----------------------------------------------------------------------
# Fancy box drawing (Unicode heavy‑box characters)
# ----------------------------------------------------------------------
def boxed(text: str) -> str:
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    top    = "┌" + "─" * (width + 2) + "┐"
    bottom = "└" + "─" * (width + 2) + "┘"
    middle = "\n".join(f"│ {line.ljust(width)} │" for line in lines)
    return f"{FG['green']}{top}{RESET}\n{middle}\n{FG['green']}{bottom}{RESET}"

# ----------------------------------------------------------------------
# Typewriter animation – prints one character at a time
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # a slightly longer pause after punctuation for effect
        if ch in ".!?,;:":
            time.sleep(delay * 6)
        else:
            time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Build the final visual: a colored box containing the quote
    art = boxed(QUOTE)

    # Print a helpful title in bold
    title = f"{BOLD}{FG['yellow']}Woody Allen’s Existential One‑Liner{RESET}"
    print("\n" + title + "\n")

    # Animate the box line‑by‑line (still using the typewriter effect)
    for line in art.split("\n"):
        typewriter(line, delay=0.03)

    # End with a wink
    wink = f"{FG['red']}¯\\_(ツ)_/¯{RESET}"
    print("\n" + wink + "\n")

if __name__ == "__main__":
    main()