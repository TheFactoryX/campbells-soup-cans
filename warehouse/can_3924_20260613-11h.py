"""
Campbell's Soup Can #3924
Produced: 2026-06-13 11:24:14
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
A tiny, colorful, animated showcase for a Woody‑Allen‑style philosophical quip.
Run it in a terminal that understands ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some pleasant pastel tones (foreground)
COLORS = [
    "\033[38;5;221m",  # light orange
    "\033[38;5;159m",  # light cyan
    "\033[38;5;150m",  # light green
    "\033[38;5;183m",  # light pink
    "\033[38;5;215m",  # peach
]

def rainbow_cycle():
    """Yield colours forever, cycling through the palette."""
    while True:
        for c in COLORS:
            yield c

# ----------------------------------------------------------------------
# Fancy box drawing
# ----------------------------------------------------------------------
TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = "╭", "╮", "╰", "╯"
H_LINE, V_LINE = "─", "│"

def framed(text: str, padding: int = 1) -> str:
    """Return `text` surrounded by a Unicode box."""
    lines = text.splitlines()
    width = max(len(line) for line in lines)
    inner_width = width + padding * 2
    top = TOP_LEFT + H_LINE * inner_width + TOP_RIGHT
    bottom = BOTTOM_LEFT + H_LINE * inner_width + BOTTOM_RIGHT
    padded = []
    pad = " " * padding
    for line in lines:
        padded.append(f"{V_LINE}{pad}{line.ljust(width)}{pad}{V_LINE}")
    return "\n".join([top] + padded + [bottom])

# ----------------------------------------------------------------------
# Typing animation
# ----------------------------------------------------------------------
def type_out(message: str, delay: float = 0.03):
    """Print `message` one character at a time with a colour cycle."""
    colour_gen = rainbow_cycle()
    for ch in message:
        sys.stdout.write(next(colour_gen) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Main – the quote
# ----------------------------------------------------------------------
def main():
    quote = (
        f"{BOLD}I’m terrified of the future, not because I’m afraid of it, "
        f"but because it’s the only thing I’m sure I’ll never get a good "
        f"seat reservation for.{RESET}"
    )
    boxed = framed(quote, padding=2)

    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Animate the boxed quote
    for line in boxed.splitlines():
        type_out(line, delay=0.02)

    # Fade out a little after a pause
    time.sleep(1.5)
    sys.stdout.write("\033[?25l")  # hide cursor
    for _ in range(3):
        sys.stdout.write("\033[2J\033[H")  # clear again
        time.sleep(0.2)
    sys.stdout.write("\033[?25h")  # restore cursor
    sys.stdout.flush()

if __name__ == "__main__":
    main()