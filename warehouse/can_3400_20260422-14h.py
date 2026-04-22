"""
Campbell's Soup Can #3400
Produced: 2026-04-22 14:09:51
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

import sys
import time
import shutil

# ---------- ANSI color helpers ----------
RESET = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"

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


def colored(text: str, fg: str = None, bg: str = None, style: str = "") -> str:
    parts = [style]
    if fg:
        parts.append(FG.get(fg, ""))
    if bg:
        parts.append(BG.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)


# ---------- Typewriter animation ----------
def typewriter(text: str, delay: float = 0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != "\n":
            time.sleep(delay)
    sys.stdout.write("\n")


# ---------- Build a fancy box ----------
def make_box(message: str, width: int = 60) -> str:
    """Return a string containing a decorative box with the message centered."""
    top = colored("╔" + "═" * (width - 2) + "╗\n", fg="cyan", style=BOLD)
    bottom = colored("╚" + "═" * (width - 2) + "╝", fg="cyan", style=BOLD)

    # split message into lines, wrap if needed
    words = message.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width - 4:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # pad each line
    padded = []
    for line in lines:
        space = width - 4 - len(line)
        left = space // 2
        right = space - left
        padded.append(
            colored(
                f"║  {' ' * left}{line}{' ' * right}  ║\n",
                fg="magenta",
                style=FAINT,
            )
        )

    return top + "".join(padded) + bottom


# ---------- Main ----------
def main():
    # The quote (Woody‑Allen‑ish)
    quote = (
        "I think the meaning of life is to find meaning in the "
        "meaningless, and then realize you were just looking for the "
        "remote control the whole time."
    )

    # Get terminal width, fallback to 80
    term_width = shutil.get_terminal_size(fallback=(80, 24)).columns
    box_width = min(70, term_width - 4)

    box = make_box(quote, width=box_width)

    # Print with a gentle typewriter effect
    typewriter(colored("\n" + " " * ((term_width - box_width) // 2), fg="blue"))
    for line in box.splitlines(keepends=True):
        # Center each line horizontally in the terminal
        padding = " " * ((term_width - len(line)) // 2)
        typewriter(padding + line, delay=0.015)

    # Final flourish
    fireworks = [
        colored(" * ", fg="yellow"),
        colored(" . ", fg="red"),
        colored(" * ", fg="green"),
        colored(" . ", fg="magenta"),
    ]
    for i in range(12):
        sys.stdout.write("\r" + " " * ((term_width - 30) // 2) + "".join(fireworks[i % 4] for _ in range(10)))
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()