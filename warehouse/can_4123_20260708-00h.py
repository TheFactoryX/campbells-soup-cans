"""
Campbell's Soup Can #4123
Produced: 2026-07-08 00:13:59
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny animated, colorful display of a Woody‑Allen‑style philosophical quote.
Runs with only the Python standard library.
"""

import sys
import time
import itertools

# ---------- ANSI colour helpers ----------
CSI = "\033["
RESET = CSI + "0m"

def color(text: str, fg: int = 37, bg: int = 40, style: int = 0) -> str:
    """Return text wrapped in ANSI escape codes.

    fg – foreground colour (30‑37)
    bg – background colour (40‑47)
    style – 0 normal, 1 bold, 2 dim, 4 underline, 5 blink, 7 reverse
    """
    return f"{CSI}{style};{fg};{bg}m{text}{RESET}"

def gradient(text: str, start: int = 31, end: int = 36) -> str:
    """Paint the characters of *text* with a smooth colour gradient."""
    colors = list(range(start, end + 1))
    if len(colors) < 2:
        colors = [start, end]
    # cycle through colours if text longer than gradient
    seq = itertools.cycle(colors)
    return "".join(color(ch, fg=next(seq)) for ch in text)

# ---------- The quote ----------
quote = (
    "I think the meaning of life is a lot like trying to read "
    "the terms of service: we keep scrolling, hoping something "
    "makes sense, and the only thing we’re really sure of is "
    "that we’ll probably click “I agree” out of sheer existential dread."
)

author = "— Woody Allen (probably)"

# ---------- Animation ----------
def type_out(message: str, delay: float = 0.03) -> None:
    """Print *message* one character at a time."""
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def bounce_box(text: str, width: int = 60, height: int = 7, cycles: int = 3) -> None:
    """Draw a box that “bounces” a few times before staying still."""
    top_bot = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    empty = "│" + " " * (width - 2) + "│"

    for _ in range(cycles):
        for offset in range(2):
            # clear screen
            sys.stdout.write(CSI + "2J" + CSI + "H")
            # top padding
            for _ in range(offset):
                print()
            # draw box
            print(color(top_bot, fg=33, style=1))
            for i in range(height - 2):
                line = empty
                # put text roughly in the middle
                if i == (height - 2) // 2:
                    txt = text[: width - 4]
                    line = "│ " + txt.ljust(width - 4) + " │"
                print(color(line, fg=36))
            print(color(bottom, fg=33, style=1))
            time.sleep(0.12)

    # final static box
    sys.stdout.write(CSI + "2J" + CSI + "H")
    for _ in range(2):
        print()
    print(color(top_bot, fg=33, style=1))
    for i in range(height - 2):
        line = empty
        if i == (height - 2) // 2:
            txt = text[: width - 4]
            line = "│ " + txt.ljust(width - 4) + " │"
        print(color(line, fg=36))
    print(color(bottom, fg=33, style=1))

# ---------- Main routine ----------
def main() -> None:
    # Prepare a colourful title
    title = gradient("  ──►  WOODY‑ALLEN PHILOSOPHY  ◄──  ", 31, 35)
    type_out(title, delay=0.005)

    # Show the quote in a bouncing box
    bounce_box(quote)

    # Print the author, slowly, in a different colour
    time.sleep(0.4)
    type_out(color(author, fg=33, style=2), delay=0.04)

if __name__ == "__main__":
    main()