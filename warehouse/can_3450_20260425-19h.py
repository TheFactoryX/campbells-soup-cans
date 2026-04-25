"""
Campbell's Soup Can #3450
Produced: 2026-04-25 19:55:41
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
Run directly:  python3 woody_quote.py
"""

import sys
import time

# -------------------------------------------------------------
# ANSI escape codes for colors and styles
# -------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}

BG = {
    "black":  "\033[40m",
    "red":    "\033[41m",
    "green":  "\033[42m",
    "yellow": "\033[43m",
    "blue":   "\033[44m",
    "magenta":"\033[45m",
    "cyan":   "\033[46m",
    "white":  "\033[47m",
}

# -------------------------------------------------------------
# The quote (Woody‑Allen‑ish)
# -------------------------------------------------------------
quote = (
    "I think the universe is like a giant therapist's couch: "
    "it listens, it never judges, but if you lie down on it "
    "you might just hear yourself think…"
)

author = "— Woody Allen (probably)"

# -------------------------------------------------------------
# Helper: type‑writer animation
# -------------------------------------------------------------
def type_out(text, delay=0.03, color=FG["cyan"]):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


# -------------------------------------------------------------
# Helper: draw a fancy box around the quote
# -------------------------------------------------------------
def boxed(text_lines, title=None):
    # Determine box width
    max_len = max(len(line) for line in text_lines)
    width = max_len + 4  # padding

    top_left = "╔"
    top_mid = "═" * (width - 2)
    top_right = "╗"

    bottom_left = "╚"
    bottom_mid = "═" * (width - 2)
    bottom_right = "╝"

    side = "║"

    # Print top border
    print(FG["magenta"] + top_left + top_mid + top_right + RESET)

    # Optional title line
    if title:
        title_str = f" {title} "
        title_len = len(title_str)
        if title_len < width - 2:
            pad = (width - 2 - title_len) // 2
            title_line = side + " " * pad + title_str + " " * (width - 2 - pad - title_len) + side
        else:
            title_line = side + title_str[: width - 2] + side
        print(FG["magenta"] + title_line + RESET)

    # Print each line of the quote
    for line in text_lines:
        padded = line + " " * (width - 4 - len(line))
        print(FG["magenta"] + side + " " + padded + " " + side + RESET)

    # Print bottom border
    print(FG["magenta"] + bottom_left + bottom_mid + bottom_right + RESET)


# -------------------------------------------------------------
# Main routine
# -------------------------------------------------------------
def main():
    # Split the quote into reasonably sized lines
    words = quote.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > 58:  # wrap at ~58 chars
            lines.append(cur)
            cur = w
        else:
            cur = cur + " " + w if cur else w
    if cur:
        lines.append(cur)

    # Show the box instantly, then animate the author
    boxed(lines, title="Deep Thought")
    time.sleep(0.5)

    # Animate the author line (different colour)
    type_out(author, delay=0.05, color=FG["yellow"] + BOLD)

    # A final flash of colour for good measure
    sys.stdout.write(FG["green"] + BOLD + "\n* * * * * * * * * *\n" + RESET)
    sys.stdout.flush()
    time.sleep(0.3)


if __name__ == "__main__":
    main()