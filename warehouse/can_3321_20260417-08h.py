"""
Campbell's Soup Can #3321
Produced: 2026-04-17 08:05:18
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
A tiny, self‑contained script that prints a single
Woody‑Allen‑style philosophical quip with a splash of color
and a typewriter‑style animation.

Run it directly:
    $ python3 this_script.py
"""

import sys
import time

# ---------- ANSI color helpers ----------
RESET = "\033[0m"
BOLD = "\033[1m"

# foreground colors
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
# background colors
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

def color_text(text: str, *, fg=None, bg=None, bold=False) -> str:
    """Wrap *text* in ANSI escape codes."""
    parts = []
    if bold:
        parts.append(BOLD)
    if fg:
        parts.append(FG.get(fg, ""))
    if bg:
        parts.append(BG.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)

# ---------- The quote ----------
quote = (
    "I told my therapist that I’m terrified of dying. "
    "He said, “Good, at least you’re finally getting something on "
    "time you can’t procrastinate.”"
)

# ---------- Fancy box drawing ----------
def build_boxed(lines, *, border_color="cyan", text_color="yellow"):
    """Return a list of strings representing a colored ASCII box."""
    max_len = max(len(line) for line in lines)
    horiz = "─" * (max_len + 2)
    top    = color_text("┌" + horiz + "┐", fg=border_color)
    bottom = color_text("└" + horiz + "┘", fg=border_color)
    middle = []
    for line in lines:
        padded = line + " " * (max_len - len(line))
        middle.append(
            color_text("│ ", fg=border_color) +
            color_text(padded, fg=text_color) +
            color_text(" │", fg=border_color)
        )
    return [top] + middle + [bottom]

# ---------- Typewriter animation ----------
def typewriter_print(lines, delay=0.04):
    """Print each line character‑by‑character."""
    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.3)  # pause between lines

def main():
    # split the quote into a few readable lines
    words = quote.split()
    max_width = 60
    cur = []
    lines = []
    for w in words:
        if len(" ".join(cur + [w])) <= max_width:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))

    # build the colored box
    boxed = build_boxed(lines, border_color="magenta", text_color="green")

    # animate!
    typewriter_print(boxed, delay=0.02)

    # final pause before exiting
    time.sleep(1)

if __name__ == "__main__":
    main()