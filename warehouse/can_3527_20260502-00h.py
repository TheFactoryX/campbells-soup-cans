"""
Campbell's Soup Can #3527
Produced: 2026-05-02 00:06:05
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
A tiny, self‑contained, colorful showcase that prints a single,
Woody‑Allen‑style philosophical one‑liner with a little “typewriter”
animation and a decorative box.

Run it directly:
    python3 woody_quote.py
"""

import sys
import time

# ---- ANSI style helpers ----------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# A palette that works on most terminals
FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}
BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}


def color_text(text: str, *, fg: str = None, bg: str = None, bold: bool = False) -> str:
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


# ---- The quote -------------------------------------------------------------
quote = (
    "I told my therapist I was terrified of the meaning of life. "
    "He said, \"Don't worry – I'm terrified of yours too.\""
)

# ---- Animation helper -------------------------------------------------------
def typewriter(text: str, delay: float = 0.04):
    """Print *text* one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


# ---- Build a decorative box -----------------------------------------------
def boxed(text: str, *, padding: int = 2, border_color: str = "magenta") -> str:
    """Return *text* surrounded by a fancy box."""
    lines = text.split("\n")
    width = max(len(line) for line in lines) + padding * 2
    top = f"╔{'═' * width}╗"
    bottom = f"╚{'═' * width}╝"
    middle = []
    for line in lines:
        padded = line.ljust(width - padding)
        middle.append(f"║{' ' * padding}{padded}{' ' * padding}║")
    box = "\n".join([top] + middle + [bottom])
    return color_text(box, fg=border_color, bold=True)


# ---- Main -------------------------------------------------------------------
def main():
    # Choose a nice background for the whole thing
    sys.stdout.write(color_text("\n", bg="black"))  # ensure background reset

    # Print the box with the quote inside, but animate the quote itself
    header = color_text(" Woody Allen meets Python ", fg="cyan", bold=True)
    boxed_header = boxed(header, border_color="cyan")
    print(boxed_header)

    # Empty line before the animated quote
    print()
    # Animate the quote in a soothing cyan
    typewriter(color_text(quote, fg="cyan", bold=True))
    print()
    # A closing smiley in green
    print(color_text("  :-)  ", fg="green", bold=True))


if __name__ == "__main__":
    main()