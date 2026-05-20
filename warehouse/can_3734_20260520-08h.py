"""
Campbell's Soup Can #3734
Produced: 2026-05-20 08:34:59
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
A tiny, colorful, animated Woody‑Allen‑style philosophical quote.
Run it in a terminal that supports ANSI colors.
"""

import sys
import time
import itertools

# ---------- ANSI colour helpers ----------
RESET = "\x1b[0m"
BOLD = "\x1b[1m"

# some pleasant pastel colours
COLS = [
    "\x1b[38;5;221m",  # soft yellow
    "\x1b[38;5;159m",  # pastel cyan
    "\x1b[38;5;180m",  # light magenta
    "\x1b[38;5;151m",  # mint green
    "\x1b[38;5;215m",  # peach
]

def color_cycle(text):
    """Yield each character coloured by a rotating palette."""
    cycler = itertools.cycle(COLS)
    for ch in text:
        yield next(cycler) + ch + RESET

def typewriter(text, delay=0.04):
    """Print text one char at a time, with colour cycling."""
    for ch in color_cycle(text):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ---------- ASCII art frame ----------
FRAME = r"""
  ╔═════════════════════════════════════════════════════════╗
  ║                                                         ║
  ║   {quote}   ║
  ║                                                         ║
  ╚═════════════════════════════════════════════════════════╝
"""

QUOTE = (
    "I feel the universe is like a comedy club: "
    "all the jokes are on me, but I’m too neurotic to laugh."
)

def build_frame(quote, width=61):
    """Insert the quote into the frame, centered and wrapped."""
    # simple word‑wrap
    words = quote.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # pad each line to width
    padded = [line.center(width) for line in lines]

    # embed into frame template
    top = "  ╔" + "═" * (width + 2) + "╗"
    bottom = "  ╚" + "═" * (width + 2) + "╝"
    empty = "  ║" + " " * (width + 2) + "║"

    # build final block
    block = [top, empty]
    for line in padded:
        block.append(f"  ║ {line} ║")
    block.append(empty)
    block.append(bottom)
    return "\n".join(block)

def main():
    frame = build_frame(QUOTE)
    # animate the frame line by line
    for line in frame.splitlines():
        typewriter(line, delay=0.02)
        time.sleep(0.06)   # a tiny pause between lines

    # final flourish
    sys.stdout.write("\n")
    typewriter(BOLD + "\x1b[38;5;202m" + "— A neurotic philosopher, 2026" + RESET, delay=0.03)

if __name__ == "__main__":
    main()