"""
Campbell's Soup Can #3641
Produced: 2026-05-10 23:09:13
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
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
A little program that displays a single Woody‑Allen‑style philosophic quip
in a colorful, animated box.  All with pure Python, no external libs.
"""

import sys
import time
import shutil

# ANSI escape codes for colours and styles
RESET = "\x1b[0m"
BOLD = "\x1b[1m"
BLINK = "\x1b[5m"

# Different colours that will be used in animation
COLORS = [
    "\x1b[31m",  # red
    "\x1b[33m",  # yellow
    "\x1b[32m",  # green
    "\x1b[36m",  # cyan
    "\x1b[34m",  # blue
    "\x1b[35m",  # magenta
]

# The Woody‑Allen‑style quote (one line, but we’ll wrap it in a box)
QUOTE = "I think, therefore I’m still afraid of anxiety, and I keep asking my doctor to collect my CPAs before I die."

# Helper to center text in the console width
def center(text, width):
    return text.center(width)

# Render a simple ASCII art box around the quote.
def render_box(lines, color):
    width = max(len(line) for line in lines)
    top_bottom = f"{color}┌{'─' * (width + 2)}┐{RESET}"
    middle = [f"{color}│ {line.ljust(width)} │{RESET}" for line in lines]
    bottom = f"{color}└{'─' * (width + 2)}┘{RESET}"
    return [top_bottom] + middle + [bottom]

# Split the quote into lines that fit the terminal width.
def wrap_quote(quote, max_width):
    words = quote.split()
    lines = []
    current = []
    for w in words:
        if len(' '.join(current + [w])) <= max_width:
            current.append(w)
        else:
            lines.append(' '.join(current))
            current = [w]
    if current:
        lines.append(' '.join(current))
    return lines

# Animate the box by changing colours over time.
def animate():
    # Get terminal size
    cols, _ = shutil.get_terminal_size(fallback=(80, 24))
    # Wrap the quote for the available width
    wrapped = wrap_quote(QUOTE, cols - 10)
    box = render_box(wrapped, COLORS[0])

    # Clean screen and print gradually
    print("\x1b[2J\x1b[H", end='')  # clear screen
    for i in range(6):
        # Pick colour for this frame
        col = COLORS[i % len(COLORS)]
        # Update border colour
        box[0] = box[0].replace(COLORS[0], col)
        box[-1] = box[-1].replace(COLORS[0], col)
        for idx in range(1, len(box)-1):
            box[idx] = box[idx].replace(COLORS[0], col)

        # Center box vertically
        blank_lines = "\n" * ((24 // 2) - len(box) // 2)
        print(f"\x1b[?25l{blank_lines}", end='')  # hide cursor
        sys.stdout.write("\n".join(box))
        sys.stdout.flush()
        time.sleep(0.5)
        # Clear previous frame
        print("\x1b[H\x1b[2J", end='')

    # Final frame without animation
    print("\x1b[?25h")  # show cursor again
    for line in box:
        print(line)
    print()  # move to next line

if __name__ == "__main__":
    animate()