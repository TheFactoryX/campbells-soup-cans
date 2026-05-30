"""
Campbell's Soup Can #3820
Produced: 2026-05-30 14:08:07
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A whimsical, animated Woody‑Allen‑style philosophical quote.
Runs in any ANSI‑capable terminal – no external libraries required.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI color & style helpers
# ----------------------------------------------------------------------
CSI = "\033["
RESET = CSI + "0m"

def color(fg=None, bg=None, bold=False):
    parts = []
    if bold:
        parts.append('1')
    if fg is not None:
        parts.append(str(30 + fg))
    if bg is not None:
        parts.append(str(40 + bg))
    return CSI + ';'.join(parts) + 'm' if parts else ''

# Basic palette (0‑7)
FG = {
    'red':    1,
    'green':  2,
    'yellow': 3,
    'blue':   4,
    'magenta':5,
    'cyan':   6,
    'white':  7,
    'black':  0,
}
BG = FG  # reuse same indices for background

# ----------------------------------------------------------------------
# Quote data
# ----------------------------------------------------------------------
quote = (
    "I have a love/hate relationship with existence: "
    "I love it when it’s not my problem, "
    "and I hate it when it becomes my problem."
)

author = "- Woody Allen (probably)"

# ----------------------------------------------------------------------
# Fancy box drawing
# ----------------------------------------------------------------------
def draw_box(text_lines, *, padding=1, margin=2, fg='cyan', bg=None):
    """Return a list of strings that draw a colored box around `text_lines`."""
    # Determine box width
    max_len = max(len(line) for line in text_lines)
    width = max_len + padding * 2

    # Choose characters
    tl, tr, bl, br, h, v = "╔", "╗", "╚", "╝", "═", "║"

    color_start = color(FG[fg], bg and BG[bg] or None, bold=True)
    line_prefix = " " * margin

    top    = line_prefix + color_start + tl + h * width + tr + RESET
    bottom = line_prefix + color_start + bl + h * width + br + RESET

    boxed = [top]
    for line in text_lines:
        spaces = " " * (width - len(line) - padding)
        interior = " " * padding + line + spaces
        boxed.append(
            line_prefix + color_start + v + interior + v + RESET
        )
    boxed.append(bottom)
    return boxed

# ----------------------------------------------------------------------
# Typewriter animation
# ----------------------------------------------------------------------
def typewriter(text, *, speed=0.04, fg='yellow', bold=False):
    """Yield the text character‑by‑character, with a slight delay."""
    style = color(FG[fg], bold=bold)
    for ch in text:
        sys.stdout.write(style + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------
def main():
    # Split quote into lines that fit nicely (max 50 chars)
    max_width = 50
    words = quote.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > max_width:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # Add the author line, right‑aligned
    author_line = author.rjust(max_width)
    lines.append("")
    lines.append(author_line)

    # Draw static box first
    boxed = draw_box(lines, fg='magenta')
    for line in boxed:
        print(line)

    # Small pause before the animation
    time.sleep(1.2)

    # Animate the quote inside the box (replace the box with a typewriter effect)
    # We'll clear the box area (ANSI cursor up + erase line)
    clear_seq = CSI + "2K"          # erase whole line
    move_up = CSI + "1A"           # cursor up one line

    # Move cursor to the first line of the quote inside the box
    for _ in range(len(lines) + 2):   # +2 for top/bottom border
        sys.stdout.write(move_up)
    sys.stdout.flush()

    # Re‑print the top border
    print(boxed[0])

    # Animate each inner line
    for i, original in enumerate(lines):
        # Erase the line where this text will go
        sys.stdout.write(move_up + clear_seq)
        sys.stdout.flush()
        # Build padded line like draw_box does
        padded = " " * 1 + original.ljust(max_width) + " " * 1
        sys.stdout.write(
            color(FG['magenta'], bold=True) + "║" + RESET
        )
        typewriter(padded, speed=0.03, fg='yellow')
        # After printing the line we are already on the next line

    # Bottom border
    print(boxed[-1])

    # Final flourish
    print()
    for _ in range(3):
        sys.stdout.write(color(FG['green'], bold=True) + "★" + RESET + " ")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)