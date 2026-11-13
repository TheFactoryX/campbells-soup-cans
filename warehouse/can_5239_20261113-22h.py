"""
Campbell's Soup Can #5239
Produced: 2026-11-13 22:38:20
Worker: inclusionAI: Ling 3.2 Flash (free) (inclusionai/ling-3.2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
woody_ism.py
------------
Prints exactly ONE (1) philosophical quote in the Woody Allen tradition:
neurotic, self-deprecating, existentially evasive.

Served with: a gradient banner, two fake loading sequences, a pastel
typewriter effect, a blinking cursor of doubt, and absolutely no meaning.

Pure Python. No dependencies. No refunds. No meaning.
"""

import colorsys
import ctypes
import itertools
import sys
import textwrap
import time

# --------------------------------------------------------------- win32 ANSI
if sys.platform == "win32":
    try:  # ask Windows nicely for VT sequences (stdlib only!)
        h = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleMode(h, 0x0004)
    except Exception:
        pass

# ------------------------------------------------------------------ settings
USE_COLOR = sys.stdout.isatty()
DELAY = 0.013 if USE_COLOR else 0.0

RESET   = "\033[0m" if USE_COLOR else ""
BOLD    = "\033[1m" if USE_COLOR else ""
DIM     = "\033[2m" if USE_COLOR else ""
ITALIC  = "\033[3m" if USE_COLOR else ""
CYAN    = "\033[96m" if USE_COLOR else ""
MAGENTA = "\033[95m" if USE_COLOR else ""

WIDTH = 54  # interior width of the quote box

QUOTE = (
    "I don't want to achieve immortality through my work; I want to "
    "achieve it through not dying. So far, so good \u2014 I've never died "
    "once, and I credit my anxiety, my couch, and a strictly "
    "observational relationship with exercise."
)
ATTR   = "\u2014 Me, 3:07 AM, still not dead"
SQUEAK = "(the couch squeaked ominously)"
TITLE  = "THE MEANING OF LIFE (SO FAR)"


# ------------------------------------------------------------------ helpers
def rgb(h, s=0.62, l=0.74):
    """Truecolor escape for hue h in [0,1]."""
    r, g, b = colorsys.hls_to_rgb(h % 1.0, l, s)
    return f"\033[38;2;{round(r*255)};{round(g*255)};{round(b*255)}m"


def grad_text(text, h0, h1, s=0.62, l=0.74):
    """Paint `text` with a smooth hue gradient."""
    if not USE_COLOR:
        return text
    n = max(len(text) - 1, 1)
    out = []
    for i, ch in enumerate(text):
        out.append(rgb(h0 + (h1 - h0) * i / n, s, l))
        out.append(ch)
    out.append(RESET)
    return "".join(out)


def spinner(label, duration):
    """A busy little spinner that accomplishes nothing. Like us all."""
    if not USE_COLOR:
        return
    frames = itertools.cycle("|/-\\")
    t0 = time.time()
    while time.time() - t0 < duration:
        sys.stdout.write(f"\r  {DIM}{label} {next(frames)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.09)
    sys.stdout.write("\r" + " " * (len(label) + 8) + "\r")
    sys.stdout.flush()


def box_side():
    return CYAN + "\u2551" + RESET


def box_top():
    return grad_text("\u2554" + "\u2550" * (WIDTH + 2) + "\u2557", 0.50, 0.90)


def box_bot():
    return grad_text("\u255a" + "\u2550" * (WIDTH + 2) + "\u255d", 0.50, 0.90)


def box_blank():
    return "  " + box_side() + " " * (WIDTH + 2) + box_side()


def type_line(line, start_idx, total, delay=DELAY):
    """Typewriter one line; hue drifts continuously across the whole quote."""
    for j, ch in enumerate(line):
        if USE_COLOR:
            t = (start_idx + j) / max(total - 1, 1)
            sys.stdout.write(rgb(0.50 + 0.38 * t))
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    return start_idx + len(line)


# --------------------------------------------------------------------- main
def main():
    print("\n")

    # ~ banner ~
    spaced = " ".join(TITLE)
    pattern = ("* . " * 40)[: len(spaced)]
    spark = grad_text(pattern, 0.52, 0.92)
    print("  " + spark)
    print("  " + BOLD + grad_text(spaced, 0.50, 0.88) + RESET)
    print("  " + spark)
    print()

    # ~ pretend to work ~
    spinner("consulting the void...", 1.1)
    spinner("the void is typing", 0.9)
    print(f"  {DIM}{ITALIC}the void has left you on read.{RESET}\n")

    # ~ the quote, typed with existential deliberation ~
    quoted = "\u201c" + QUOTE + "\u201d"
    lines = textwrap.wrap(quoted, width=WIDTH)
    total = sum(len(ln) for ln in lines)

    print("  " + box_top())
    idx = 0
    for ln in lines:
        sys.stdout.write("  " + box_side() + " ")
        idx = type_line(ln, idx, total)
        sys.stdout.write(" " * (WIDTH - len(ln)) + " " + box_side() + "\n")

    print(box_blank())

    attr = ATTR.center(WIDTH)
    sys.stdout.write("  " + box_side() + " ")
    for ch in attr:
        sys.stdout.write((MAGENTA + BOLD + ch) if USE_COLOR else ch)
        sys.stdout.flush()
        time.sleep(DELAY * 0.6)
    sys.stdout.write(RESET + " " * (WIDTH - len(attr)) + " " + box_side() + "\n")

    squeak = SQUEAK.center(WIDTH)
    sys.stdout.write("  " + box_side() + " " + DIM + ITALIC + squeak + RESET)
    sys.stdout.write(" " * (WIDTH - len(squeak)) + " " + box_side() + "\n")

    print("  " + box_bot())

    # ~ a cursor, blinking, waiting for an answer that won't come ~
    if USE_COLOR:
        sys.stdout.write("\n  > ")
        sys.stdout.flush()
        for _ in range(3):
            sys.stdout.write(BOLD + MAGENTA + "\u2588" + RESET)
            sys.stdout.flush()
            time.sleep(0.22)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(0.22)
        sys.stdout.write("\r" + " " * 10 + "\r")
        sys.stdout.flush()

    # ~ fine print ~
    foot = "* meaning sold separately *"
    print("  " + DIM + ITALIC + foot.center(WIDTH + 4) + RESET + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n")