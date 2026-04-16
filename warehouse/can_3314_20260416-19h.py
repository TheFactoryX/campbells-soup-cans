"""
Campbell's Soup Can #3314
Produced: 2026-04-16 19:37:31
Worker: OpenAI: GPT-5 Image Mini (openai/gpt-5-image-mini)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Playful single-file Python program that prints ONE funny philosophical quote
in the style of Woody Allen (neurotic, self-deprecating, existential),
with a brief required disclaimer and colorful animated presentation.
No external dependencies. ANSI colors used.
"""

import sys
import time
import shutil
import math
import itertools
import os

# ANSI color helpers
CSI = "\033["
RESET = CSI + "0m"
BOLD = CSI + "1m"
DIM = CSI + "2m"
ITALIC = CSI + "3m"
UNDER = CSI + "4m"

# Some nice colors (foreground)
COLORS = [
    CSI + "38;5;197m",  # pink
    CSI + "38;5;206m",
    CSI + "38;5;220m",  # yellow
    CSI + "38;5;118m",  # green
    CSI + "38;5;81m",   # teal
    CSI + "38;5;75m",   # blue
    CSI + "38;5;141m",  # purple
]

# Box drawing chars
TL = "╭"
TR = "╮"
BL = "╰"
BR = "╯"
H = "─"
V = "│"

# The required brief disclaimer for style-of-public-figure requests:
DISCLAIMER = (
    "Note: I can't write exactly in Woody Allen's voice, "
    "but here's an original line inspired by his neurotic, self-deprecating, existential style."
)

# The single original quote to display (one quote only)
QUOTE = (
    "I'm not afraid of death; I'm mostly terrified of being two hours late "
    "to my own existential crisis because I couldn't find my keys."
)

# Small ASCII "neurotic face" to add playfulness
NEUROTIC_FACE = "(•͡˘㉨•͡˘)"

# Utility: get terminal width
def term_width(default=80):
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default

# Center text wrt terminal width
def center_text(s, width=None):
    if width is None:
        width = term_width()
    lines = s.splitlines()
    return "\n".join(line.center(width) for line in lines)

# Typewriter effect printing one char at a time with color cycling
def typewriter_print(text, colors=COLORS, delay=0.02):
    color_cycle = itertools.cycle(colors)
    for ch in text:
        if ch == " ":
            sys.stdout.write(ch)
        else:
            color = next(color_cycle)
            sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Gradual box draw with quote inside, with colored border shimmering
def animated_quote_box(quote, padding=2, border_colors=COLORS, dwell=0.04):
    # Prepare single-line quote wrapped to not exceed terminal width
    tw = term_width()
    max_inner = tw - 10
    if len(quote) > max_inner:
        # naive wrap
        words = quote.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 <= max_inner:
                cur = cur + (" " if cur else "") + w
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    else:
        lines = [quote]

    box_width = max(len(line) for line in lines) + padding * 2
    box_total = box_width + 2  # borders

    # Ensure box doesn't exceed terminal width
    if box_total + 8 > tw:
        box_width = tw - 10
        # truncate middle if necessary
        lines = [ln[: box_width - padding * 2 - 3] + "..." if len(ln) > box_width - padding * 2 else ln for ln in lines]

    # Build empty box lines
    top = TL + H * box_width + TR
    bottom = BL + H * box_width + BR

    # Animate border shimmering
    for i in range(6):
        color = border_colors[i % len(border_colors)]
        sys.stdout.write("\r" + " " * ((tw - box_total) // 2))  # move to center-ish
        sys.stdout.write(color + top + RESET + "\n")
        for ln in lines:
            pad_left = " " * padding
            pad_right = " " * (box_width - len(ln) - padding)
            sys.stdout.write(" " * ((tw - box_total) // 2))
            sys.stdout.write(color + V + RESET)
            sys.stdout.write(" " * padding + ln + pad_right)
            sys.stdout.write(color + V + RESET + "\n")
        sys.stdout.write(" " * ((tw - box_total) // 2))
        sys.stdout.write(color + bottom + RESET + "\n")
        sys.stdout.flush()
        time.sleep(dwell)
        # Move cursor up to redraw (erase previous with ANSI)
        sys.stdout.write(CSI + str(len(lines) + 2) + "A")  # move up
        sys.stdout.write(CSI + "0J")  # clear from cursor down

    # Final stable box with rainbow typing of quote inside
    # Print top
    color = border_colors[0]
    sys.stdout.write(" " * ((tw - box_total) // 2) + BOLD + color + top + RESET + "\n")
    for ln in lines:
        pad_left = " " * padding
        pad_right = " " * (box_width - len(ln) - padding)
        sys.stdout.write(" " * ((tw - box_total) // 2) + BOLD + color + V + RESET + " ")
        # typewriter the line with color gradient
        # We'll paint each character cycling colors for a rainbow effect
        gradient = list(itertools.islice(itertools.cycle(border_colors), len(ln)))
        for ch, col in zip(ln, gradient):
            if ch == " ":
                sys.stdout.write(" ")
            else:
                sys.stdout.write(col + ch + RESET)
        sys.stdout.write(" " + BOLD + color + V + RESET + "\n")
    sys.stdout.write(" " * ((tw - box_total) // 2) + BOLD + color + bottom + RESET + "\n")
    sys.stdout.flush()

# Small spinner while "thinking"
def spinner(seconds=1.8):
    symbols = ["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈"]
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sym = symbols[i % len(symbols)]
        sys.stdout.write("\r" + DIM + "Thinking " + sym + RESET)
        sys.stdout.flush()
        time.sleep(0.07)
        i += 1
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write(CSI + "2J" + CSI + "H")

def main():
    try:
        clear_screen()
        tw = term_width()
        # Print neurotic face centered
        print(center_text(DIM + NEUROTIC_FACE + RESET, tw))
        print()
        # Print brief disclaimer (required by style guidelines) with dim italic
        disc_lines = []
        # Wrap disclaimer at reasonable width
        wrap_width = min(72, tw - 10)
        words = DISCLAIMER.split()
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 <= wrap_width:
                cur = cur + (" " if cur else "") + w
            else:
                disc_lines.append(cur)
                cur = w
        if cur:
            disc_lines.append(cur)
        for line in disc_lines:
            # typewriter the disclaimer but dimmer
            sys.stdout.write(" " * ((tw - len(line)) // 2))
            typewriter_print(DIM + line + RESET, colors=[CSI + "38;5;244m"], delay=0.005)
        print()
        # Small spinner to build anticipation
        spinner(1.4)
        # Animated box with the single quote
        animated_quote_box(QUOTE, padding=3, border_colors=COLORS, dwell=0.06)
        print()
        # A final playful tagline (not a quote) to close — tiny and dim
        tag = "— an anxious thought, freshly microwaved"
        print(center_text(DIM + tag + RESET, tw))
        print()
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.exit(0)

if __name__ == "__main__":
    main()