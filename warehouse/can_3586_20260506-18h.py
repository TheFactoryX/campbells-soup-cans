"""
Campbell's Soup Can #3586
Produced: 2026-05-06 18:59:21
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
A tiny, colorful Woody‑Allen‑style philosophy printer.
Runs with only the Python standard library.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI escape codes for colors & styles
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# pastel rainbow palette (foreground)
COLORS = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;46m",   # green
    "\033[38;5;51m",   # cyan
    "\033[38;5;21m",   # blue
    "\033[38;5;201m",  # magenta
]

# ----------------------------------------------------------------------
# The quote – invented in Woody‑Allen’s neurotic voice
# ----------------------------------------------------------------------
QUOTE = (
    f"{BOLD}I’m terrified of the future, not because it’s unknown, "
    f"but because I’m sure it will finally ask me to pay "
    f"for the existential crisis I’ve been avoiding all my life.{RESET}"
)

# ----------------------------------------------------------------------
# Helper to print text with a “typewriter” effect.
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    """Print `text` one character at a time with a tiny pause."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Helper to paint each line with a cycling rainbow.
# ----------------------------------------------------------------------
def rainbow_print(lines: list[str], speed: float = 0.1) -> None:
    """Print each line using a rotating rainbow foreground."""
    color_cycle = itertools.cycle(COLORS)
    for line in lines:
        color = next(color_cycle)
        sys.stdout.write(color + line + RESET + "\n")
        sys.stdout.flush()
        time.sleep(speed)

# ----------------------------------------------------------------------
# Build a decorative “box” around the quote
# ----------------------------------------------------------------------
def build_box(text: str, width: int = 72) -> list[str]:
    """Return a list of strings forming a pretty box around `text`."""
    # split long text into nicely wrapped lines
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width - 4:  # 4 for borders & spaces
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    top = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    boxed = [top]
    for ln in lines:
        padded = ln.ljust(width - 4)
        boxed.append(f"│ {padded} │")
    boxed.append(bottom)
    return boxed

# ----------------------------------------------------------------------
# Main animation routine
# ----------------------------------------------------------------------
def main() -> None:
    box = build_box(QUOTE)
    # Fade‑in style: first show an empty box, then fill line by line
    empty_box = [line.replace("─", " ").replace("│", " ").replace("─", " ") for line in box]
    rainbow_print(empty_box, speed=0.05)

    # small pause before the words appear
    time.sleep(0.6)

    # reveal the quote line by line with typewriter effect
    for i, line in enumerate(box):
        if i == 0 or i == len(box) - 1:        # top / bottom borders
            sys.stdout.write(line + "\n")
            continue
        # strip the border characters, typewrite the inner text, then re‑add borders
        inner = line[2:-2]  # content without side borders
        sys.stdout.write("│ ")
        typewriter(inner, delay=0.02)
        sys.stdout.write(" │\n")
        time.sleep(0.1)

    # final flourish: a rainbow underline
    underline = " " * 2 + "¯" * (len(box[0]) - 4)
    rainbow_print([underline], speed=0.08)

if __name__ == "__main__":
    main()