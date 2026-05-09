"""
Campbell's Soup Can #3618
Produced: 2026-05-09 13:53:02
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
Run it directly:  python3 this_file.py
"""

import sys
import time
import shutil

# ----------------------------------------------------------------------
# ANSI colour / style helpers
# ----------------------------------------------------------------------
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
    "black": "\033[40m",
    "red":   "\033[41m",
    "green": "\033[42m",
    "yellow":"\033[43m",
    "blue":  "\033[44m",
    "magenta":"\033[45m",
    "cyan":  "\033[46m",
    "white": "\033[47m",
}

def colored(text: str, *, fg: str = None, bg: str = None, bold: bool = False) -> str:
    """Wrap *text* in ANSI colour / style sequences."""
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


# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑style)
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is a little like a bad movie: "
    "it's full of awkward silences, questionable decisions, "
    "and a plot that never quite resolves—"
    "and I'm pretty sure the director left the set early."
)

# ----------------------------------------------------------------------
# Fancy box drawing (Unicode heavy‑weight)
# ----------------------------------------------------------------------
def make_box(text: str, *, padding: int = 2, color: str = "magenta") -> str:
    """Return *text* inside a coloured Unicode box."""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    horiz = "─" * (max_len + padding * 2)
    top = f"┌{horiz}┐"
    bottom = f"└{horiz}┘"
    middle = []
    for line in lines:
        space = " " * (max_len - len(line))
        middle.append(f"│{' ' * padding}{line}{space}{' ' * padding}│")
    box = "\n".join([top] + middle + [bottom])
    return colored(box, fg=color, bold=True)


# ----------------------------------------------------------------------
# Typing animation
# ----------------------------------------------------------------------
def typewriter(text: str, *, speed: float = 0.03) -> None:
    """Print *text* character‑by‑character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Slightly slower on newlines for readability
        time.sleep(speed if ch != "\n" else speed * 5)
    sys.stdout.write("\n")


# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Clear screen (works on most terminals)
    sys.stdout.write("\033c")
    term_width = shutil.get_terminal_size((80, 20)).columns

    # Prepare colourful header
    header = colored(" ★ Wo o d y   A l l e n   ★ ", fg="yellow", bold=True)
    print(header.center(term_width))
    print()

    # Print the quote inside a box
    box = make_box(QUOTE, padding=3, color="cyan")
    # Animate line‑by‑line
    for line in box.split("\n"):
        typewriter(line + "\n", speed=0.015)

    # End with a wink
    wink = colored("  ;) ", fg="green", bold=True)
    print("\n" + wink.center(term_width))


if __name__ == "__main__":
    main()