"""
Campbell's Soup Can #3179
Produced: 2026-04-07 15:43:17
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
A tiny animated showcase for a Woody‑Allen‑style philosophical quip.
It uses only the standard library and ANSI escape codes for colour.
"""

import sys
import time
import itertools

# --------------------------------------------------------------------------- #
# Colour helpers (ANSI escape codes)
# --------------------------------------------------------------------------- #
RESET = "\033[0m"
BOLD = "\033[1m"

# A simple palette – feel free to tweak
FG_COLORS = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
BG_COLORS = {
    "black":   "\033[40m",
    "red":     "\033[41m",
    "green":   "\033[42m",
    "yellow":  "\033[43m",
    "blue":    "\033[44m",
    "magenta": "\033[45m",
    "cyan":    "\033[46m",
    "white":   "\033[47m",
}

def colored(text: str, fg: str = None, bg: str = None, bold: bool = False) -> str:
    """Wrap *text* in ANSI colour codes."""
    parts = []
    if bold:
        parts.append(BOLD)
    if fg:
        parts.append(FG_COLORS.get(fg, ""))
    if bg:
        parts.append(BG_COLORS.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)

# --------------------------------------------------------------------------- #
# The quote
# --------------------------------------------------------------------------- #
quote = (
    "I have a fear of death, not because I'm scared of it, "
    "but because I haven't yet figured out where the exit sign points."
)

# --------------------------------------------------------------------------- #
# Fancy box drawing
# --------------------------------------------------------------------------- #
def make_box(lines, padding=2, border_style="double"):
    """Return a list of strings forming a coloured box around *lines*."""
    # Border characters
    if border_style == "double":
        tl, tr, bl, br = "╔", "╗", "╚", "╝"
        h, v = "═", "║"
    else:  # simple
        tl, tr, bl, br = "+", "+", "+", "+"
        h, v = "-", "|"

    # Determine width
    max_len = max(len(line) for line in lines)
    inner_width = max_len + padding * 2

    top    = tl + h * inner_width + tr
    bottom = bl + h * inner_width + br
    empty  = v + " " * inner_width + v

    boxed = [top]
    boxed.append(empty)
    for line in lines:
        spaces = inner_width - len(line) - padding
        left  = " " * padding
        right = " " * spaces
        boxed.append(v + left + line + right + v)
    boxed.append(empty)
    boxed.append(bottom)
    return boxed

# --------------------------------------------------------------------------- #
# Typewriter animation
# --------------------------------------------------------------------------- #
def typewriter(text, delay=0.04, colour="cyan"):
    """Yield the text one character at a time, colourised."""
    for ch in text:
        yield colored(ch, fg=colour)
        time.sleep(delay)

def animate_box(box_lines, speed=0.02):
    """Print *box_lines* line‑by‑line with a tiny pause for drama."""
    for line in box_lines:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(speed)

# --------------------------------------------------------------------------- #
# Main routine
# --------------------------------------------------------------------------- #
def main():
    # Split the quote into reasonably sized chunks
    words = quote.split()
    max_width = 56
    lines = []
    cur = []
    cur_len = 0
    for w in words:
        if cur_len + len(w) + 1 > max_width:
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
        else:
            cur.append(w)
            cur_len += len(w) + 1
    if cur:
        lines.append(" ".join(cur))

    # Build the box (coloured border)
    boxed = make_box(lines, padding=3, border_style="double")
    coloured_box = [colored(l, fg="magenta", bold=True) for l in boxed]

    # Show a little "loading" animation before the reveal
    spinner = itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"])
    for _ in range(12):
        sys.stdout.write("\r" + colored("Thinking about existence ", fg="yellow") + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")  # clear line

    # Animate the box appearance
    animate_box(coloured_box, speed=0.07)

    # Type‑out the quote underneath the box for extra flair
    sys.stdout.write("\n")
    for ch in typewriter("— Woody Allen", delay=0.06, colour="green"):
        sys.stdout.write(ch)
        sys.stdout.flush()
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()