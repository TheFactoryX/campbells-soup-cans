"""
Campbell's Soup Can #3365
Produced: 2026-04-19 19:53:49
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
A tiny, colorful, animated Woody‑Allen‑style quote printer.
Run it in a terminal that supports ANSI escape codes.
"""

import sys
import time
import itertools

# ── ANSI colour helpers ──────────────────────────────────────────────────────
RESET = "\033[0m"

# A palette that looks a bit neurotic (pale yellows, anxious blues, etc.)
COLORS = {
    "title": "\033[38;5;226m",   # bright yellow
    "quote": "\033[38;5;39m",    # soft cyan
    "border": "\033[38;5;245m",  # grey
    "author": "\033[38;5;202m",  # orange
    "cursor": "\033[38;5;244m",  # dim grey
}

# ── The quote ───────────────────────────────────────────────────────────────
quote = (
    "I think the meaning of life is to keep searching for meaning, "
    "while simultaneously realizing that the universe "
    "doesn't care whether we find it or not."
)
author = "— Woody Allen (probably)"

# ── Fancy box drawing (Unicode light lines) ───────────────────────────────────
def make_box(text_lines, width):
    top = f"{COLORS['border']}┌{'─' * (width + 2)}┐{RESET}"
    bottom = f"{COLORS['border']}└{'─' * (width + 2)}┘{RESET}"
    middle = [
        f"{COLORS['border']}│{RESET} {line.ljust(width)} {COLORS['border']}│{RESET}"
        for line in text_lines
    ]
    return "\n".join([top] + middle + [bottom])

# ── Split the quote into nicely sized lines ───────────────────────────────────
def wrap(text, max_width):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 > max_width:
            lines.append(current.rstrip())
            current = w + " "
        else:
            current += w + " "
    lines.append(current.rstrip())
    return lines

# ── Typewriter animation ─────────────────────────────────────────────────────
def typewriter(text, speed=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)

def animated_print(boxed, delay=0.02):
    # Reveal the box line‑by‑line with a tiny pause
    for line in boxed.splitlines():
        print(line)
        time.sleep(delay)

# ── Main routine ─────────────────────────────────────────────────────────────
def main():
    # Prepare lines
    wrapped = wrap(quote, 60)
    all_lines = wrapped + ["", author]  # blank line before author
    box_width = max(len(l) for l in all_lines)

    # Assemble the coloured box string
    boxed = make_box(
        [f"{COLORS['quote']}{l}{RESET}" for l in wrapped] +
        [f"{COLORS['author']}{author}{RESET}"],
        box_width,
    )

    # Print a flashing title first
    title = f"{COLORS['title']}Woody Allen's Existential Musings{RESET}"
    for _ in range(3):
        sys.stdout.write("\r" + " " * len(title))
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\r" + title)
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

    # Animate the quote box
    animated_print(boxed, delay=0.03)

    # Final cursor blink to give a "thinking" vibe
    cursor = f"{COLORS['cursor']}_"
    for _ in range(6):
        sys.stdout.write("\r" + cursor)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r ")
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)