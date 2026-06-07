"""
Campbell's Soup Can #3884
Produced: 2026-06-07 18:19:28
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
A tiny, colorful, animated display of a single Woody‑Allen‑style philosophical quote.
Run directly in a terminal that understands ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI escape utilities
# ----------------------------------------------------------------------
RESET = "\u001b[0m"
BOLD = "\u001b[1m"

# Some nice pastel colors (foreground)
COLORS = [
    "\u001b[38;5;220m",  # gold
    "\u001b[38;5;215m",  # orange
    "\u001b[38;5;209m",  # coral
    "\u001b[38;5;171m",  # pink
    "\u001b[38;5;105m",  # lavender
    "\u001b[38;5;81m",   # aqua
]

def color_cycle():
    """Yield colors endlessly."""
    while True:
        for c in COLORS:
            yield c

def typewriter(text, speed=0.04, color=RESET):
    """Print text character‑by‑character like a typewriter."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

def draw_box(lines, width, color):
    """Draw a simple box around the given lines."""
    horiz = "─"
    top = f"{color}┌{horiz*width}┐{RESET}"
    bottom = f"{color}└{horiz*width}┘{RESET}"
    sys.stdout.write(top + "\n")
    for line in lines:
        padded = line.ljust(width)
        sys.stdout.write(f"{color}│{RESET}{padded}{color}│{RESET}\n")
    sys.stdout.write(bottom + "\n")

def main():
    quote = (
        "I think existential dread is like a bad haircut: "
        "you can't fix it by moving your head, "
        "but you can cover it with a hat."
    )
    # Split the quote for nicer formatting
    words = quote.split()
    max_len = 50
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > max_len:
            lines.append(cur)
            cur = w
        else:
            cur = cur + (" " if cur else "") + w
    if cur:
        lines.append(cur)

    # Prepare a color animator
    col_gen = color_cycle()

    # Simple animation: flash background while building the box
    for _ in range(3):
        bg = next(col_gen)
        draw_box([""], max_len, bg)
        time.sleep(0.15)
        # clear the box (move cursor up)
        sys.stdout.write("\u001b[2A")  # up two lines
        sys.stdout.write("\u001b[2K")  # erase line
        sys.stdout.write("\u001b[1A")  # up one line
        sys.stdout.write("\u001b[2K")  # erase line

    # Final box with static color
    final_color = next(col_gen)
    draw_box(lines, max_len, final_color)

    # Type out the quote inside the box, one line at a time
    for line in lines:
        typewriter(line, speed=0.03, color=BOLD + final_color)

    # A little flourish
    for _ in range(3):
        sys.stdout.write("\u001b[2D")   # back two columns
        sys.stdout.write("\u001b[31m♥\u001b[0m")  # red heart
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    main()