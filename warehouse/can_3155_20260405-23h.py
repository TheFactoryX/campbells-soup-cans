"""
Campbell's Soup Can #3155
Produced: 2026-04-05 23:49:27
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
A tiny, colorful terminal program that prints a single
Woody‑Allen‑style philosophical quip in a flashing ASCII box.
"""

import sys
import time

# ---------- ANSI colour helpers ----------
RESET = "\033[0m"
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "mag":    "\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
BG = {
    "black": "\033[40m",
    "red":   "\033[41m",
    "green": "\033[42m",
    "yellow":"\033[43m",
    "blue":  "\033[44m",
    "mag":   "\033[45m",
    "cyan":  "\033[46m",
    "white": "\033[47m",
}

# ---------- The quote ----------
quote = (
    "I’m terrified of the future, but I’m more terrified "
    "of the idea that I’ll never get a good haircut before it."
)

# ---------- Utility: type‑writer effect ----------
def type_out(text: str, delay: float = 0.03) -> None:
    """Print `text` one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ---------- Build a coloured ASCII box ----------
def make_box(lines, padding=2):
    """Return a list of strings forming a coloured box around `lines`."""
    max_len = max(len(l) for l in lines)
    width = max_len + padding * 2
    top    = f"{FG['cyan']}╔{'═' * width}╗{RESET}"
    bottom = f"{FG['cyan']}╚{'═' * width}╝{RESET}"
    boxed  = [top]
    for line in lines:
        space = width - len(line)
        left  = space // 2
        right = space - left
        boxed.append(
            f"{FG['cyan']}║{RESET}"
            f"{' ' * left}"
            f"{FG['mag']}{line}{RESET}"
            f"{' ' * right}"
            f"{FG['cyan']}║{RESET}"
        )
    boxed.append(bottom)
    return boxed

# ---------- Main animation ----------
def main():
    # Split the quote into a few readable chunks
    words = quote.split()
    chunks = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > 55:
            chunks.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        chunks.append(cur.rstrip())

    # Create the box once (static size)
    box_lines = make_box(chunks, padding=4)

    # Fade‑in effect: draw the box line by line
    for line in box_lines:
        type_out(line, delay=0.01)
        time.sleep(0.07)

    # Hold the quote a moment before exiting
    time.sleep(2)

if __name__ == "__main__":
    main()