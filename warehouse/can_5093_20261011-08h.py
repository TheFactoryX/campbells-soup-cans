"""
Campbell's Soup Can #5093
Produced: 2026-10-11 08:52:35
Worker: inclusionAI: Ling 3.1 Flash (inclusionai/ling-3.1-flash)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
daily_neurosis.py
=================
Prints ONE funny philosophical quote in Woody Allen's style,
served with gradient dread, spectacles, a spinning void,
and a blinking cursor of existential uncertainty.

Pure Python. No dependencies. Just vibes.
"""

import os
import random
import shutil
import sys
import textwrap
import time

# ------------------------------------------------------------- the goods --
QUOTE = (
    "The universe is 13.8 billion years old, vast and utterly indifferent "
    "to my suffering \u2014 and yet, somehow, my therapist is fully booked."
)
ATTRIBUTION = "\u2014 me, probably, at 3 a.m."
TITLE = "\u2726 WOODY-ISH WISDOM \u2726"
EPILOGUE = "The universe declined to comment."
FOOTNOTE = "(parody \u2014 the real Woody is still working.)"

GLASSES = [
    "   ___  ___ ___  ",
    r"  /   \_____/   \  ",
    " |  (\u2022)   (\u2022)  | ",
    r"  \   /     \   /  ",
]

# ------------------------------------------------------------------ style --
TTY = sys.stdout.isatty()

RESET = "\033[0m" if TTY else ""
BOLD = "\033[1m" if TTY else ""
DIM = "\033[2m" if TTY else ""
ITALIC = "\033[3m" if TTY else ""
CLEAR_SCREEN = "\033[2J\033[H" if TTY else ""
HIDE_CURSOR = "\033[?25l" if TTY else ""
SHOW_CURSOR = "\033[?25h" if TTY else ""

CYAN = (56, 189, 248)
GOLD = (250, 204, 21)
MAGENTA = (232, 121, 249)
SPARKLES = [(250, 204, 21), (103, 232, 249), (240, 171, 252), (187, 247, 208)]


def _truecolor():
    if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"):
        return True
    term = os.environ.get("TERM", "")
    return "truecolor" in term or "24bit" in term


TRUECOLOR = TTY and _truecolor()


def rgb(r, g, b):
    """ANSI foreground colour, with a 256-colour fallback for ancient terminals."""
    if not TTY:
        return ""
    if TRUECOLOR:
        return f"\033[38;2;{r};{g};{b}m"

    def q(v):
        return round(v / 255 * 5)

    return f"\033[38;5;{16 + 36 * q(r) + 6 * q(g) + q(b)}m"


def mix(c1, c2, t):
    return tuple(int(round(a + (b - a) * t)) for a, b in zip(c1, c2))


def grad(t):
    """The cyan-to-magenta existential gradient."""
    return rgb(*mix(CYAN, MAGENTA, min(1.0, max(0.0, t))))


def out(s=""):
    sys.stdout.write(s)
    sys.stdout.flush()


def term_width():
    try:
        return max(40, shutil.get_terminal_size().columns)
    except Exception:
        return 80


def spin(seconds, message):
    """A little braille wheel, spinning up the courage to be alive."""
    frames = "\u280b\u2819\u2839\u2838\u283c\u2834\u2826\u2827\u2807\u280f"
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        out(f"\r{BOLD}{rgb(*GOLD)}{frames[i % len(frames)]} {DIM}{message}{RESET}")
        time.sleep(0.07)
        i += 1
    out("\r" + " " * (len(message) + 4) + "\r")


def twinkle(max_row):
    """Sprinkle a few transient sparkles around the scene."""
    w = term_width()
    last = (1, 1)
    for _ in range(16):
        if random.random() < 0.5:
            r = random.randint(1, 4)        # near the spectacles
        else:
            r = random.randint(6, max_row)  # near the box
        c = random.randint(2, max(3, w - 3))
        last = (r, c)
        out(f"\033[{r};{c}H{BOLD}{rgb(*random.choice(SPARKLES))}\u2726{RESET}")
        time.sleep(random.uniform(0.04, 0.14))
    out(f"\033[{last[0]};{last[1]}H ")  # erase the final sparkle


def main():
    w = term_width()
    try:
        out(HIDE_CURSOR)
        out(CLEAR_SCREEN)

        # -- the spectacles of wisdom ------------------------------------
        for i, line in enumerate(GLASSES):
            out(grad(i / (len(GLASSES) - 1)) + line.center(w) + RESET + "\n")
            if TTY:
                time.sleep(0.13)

        # -- consult the void -------------------------------------------
        if TTY:
            spin(1.5, "consulting the void")
        out("\n\n")

        # -- the quote, framed in gold ----------------------------------
        quote_lines = textwrap.wrap(QUOTE, max(20, w - 8))
        inner = max(w - 8, *(len(l) for l in quote_lines), len(TITLE), len(ATTRIBUTION))
        top = "╔" + "═" * (inner + 4) + "╗"
        bottom = "╚" + "═" * (inner + 4) + "╝"

        out(BOLD + rgb(*GOLD) + top.center(w) + RESET + "\n")
        if TTY:
            time.sleep(0.12)
        title_line = f"║  {TITLE}{' ' * (inner - len(TITLE))}  ║"
        out(rgb(*GOLD) + title_line.center(w) + RESET + "\n")
        blank_line = f"║  {' ' * inner}  ║"
        out(DIM + blank_line.center(w) + RESET + "\n")

        # -- typewriter revelation, one dread-filled character at a time -
        total = sum(len(l) for l in quote_lines)
        pos = 0
        for line in quote_lines:
            out(rgb(*CYAN) + "║  " + RESET)
            for i, ch in enumerate(line):
                out(grad((pos + i) / max(1, total - 1)) + ch + RESET)
                if TTY:
                    time.sleep(0.018)
            out(DIM + " " * (inner - len(line)) + "  ║" + RESET + "\n")
            pos += len(line)

        # -- attribution, with a blinking cursor of doom ----------------
        out(rgb(*CYAN) + "║  " + RESET)
        for ch in ATTRIBUTION:
            out(ITALIC + rgb(*GOLD) + ch + RESET)
            if TTY:
                time.sleep(0.035)
        pad = inner - len(ATTRIBUTION)
        clean = (
            ("\r" if TTY else "")
            + rgb(*CYAN) + "║  " + RESET
            + ITALIC + rgb(*GOLD) + ATTRIBUTION + RESET
            + DIM + " " * pad + "  ║" + RESET
        )
        if TTY:
            for _ in range(3):
                out(clean + BOLD + rgb(*GOLD) + "\u258c" + RESET)
                time.sleep(0.22)
                out(clean)
                time.sleep(0.22)
        out(clean + "\n")
        out(BOLD + rgb(*GOLD) + bottom.center(w) + RESET + "\n")

        # -- sprinkle some transient dread ------------------------------
        if TTY:
            twinkle(10 + len(quote_lines))
            out(f"\033[{12 + len(quote_lines)};1H")

        out("\n" + DIM + ITALIC + EPILOGUE.center(w) + RESET)
        out("\n" + DIM + FOOTNOTE.center(w) + RESET + "\n")
    finally:
        out(SHOW_CURSOR)


if __name__ == "__main__":
    main()