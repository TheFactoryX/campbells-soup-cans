"""
Campbell's Soup Can #3712
Produced: 2026-05-17 18:11:53
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
A tiny, colorful, animated showcase of a Woody‑Allen‑style philosophical
one‑liner.  Run it in a terminal that supports ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\x1b[0m"

# foreground colours (bright)
FG = {
    "red":    "\x1b[91m",
    "green":  "\x1b[92m",
    "yellow": "\x1b[93m",
    "blue":   "\x1b[94m",
    "magenta":"\x1b[95m",
    "cyan":   "\x1b[96m",
    "white":  "\x1b[97m",
}

# background colours (dim)
BG = {
    "black":   "\x1b[40m",
    "red":     "\x1b[41m",
    "green":   "\x1b[42m",
    "yellow":  "\x1b[43m",
    "blue":    "\x1b[44m",
    "magenta": "\x1b[45m",
    "cyan":    "\x1b[46m",
    "white":   "\x1b[47m",
}

def colour(text: str, fg: str = None, bg: str = None) -> str:
    """Wrap *text* in ANSI colour codes."""
    parts = []
    if fg:
        parts.append(FG.get(fg, ""))
    if bg:
        parts.append(BG.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)


# ----------------------------------------------------------------------
# Box drawing utilities
# ----------------------------------------------------------------------
TL, TR, BL, BR, H, V = "╭", "╮", "╰", "╯", "─", "│"


def framed(text: str, *, padding: int = 1, fg: str = "cyan") -> str:
    """Return *text* inside a coloured ASCII box."""
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    inner_width = max_len + padding * 2

    top = TL + H * inner_width + TR
    bottom = BL + H * inner_width + BR
    middle = []
    for line in lines:
        spaced = " " * padding + line.ljust(max_len) + " " * padding
        middle.append(V + spaced + V)

    box = [top] + middle + [bottom]
    return colour("\n".join(box), fg)


# ----------------------------------------------------------------------
# The quote & animation
# ----------------------------------------------------------------------
quote = (
    "\"I think the meaning of life is to keep getting "
    "confused about it, while pretending I know what I'm doing.\""
)

# Colours will cycle like a rainbow
rainbow = itertools.cycle(["red", "yellow", "green", "cyan", "blue", "magenta"])

def animate():
    """Simple type‑writer animation with colour‑shifting borders."""
    # pre‑wrap the quote inside a box (no colour yet)
    static_box = framed(quote, padding=2, fg="white")
    box_lines = static_box.splitlines()

    # erase the cursor
    sys.stdout.write("\x1b[?25l")
    try:
        for i in range(len(box_lines)):
            # choose a colour for the current line's border
            border_colour = next(rainbow)
            line = box_lines[i]
            # replace the first and last characters (the borders) with coloured ones
            coloured_line = (
                colour(line[0], fg=border_colour) +
                line[1:-1] +
                colour(line[-1], fg=border_colour)
            )
            print(coloured_line)
            time.sleep(0.2)
        # hold the final picture for a moment
        time.sleep(2)
    finally:
        # bring the cursor back
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()


if __name__ == "__main__":
    animate()