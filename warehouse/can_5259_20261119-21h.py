"""
Campbell's Soup Can #5259
Produced: 2026-11-19 21:35:15
Worker: Particle AI: Particle-1 (free) (particle-ai/particle-1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A THOUGHT, OVER COFFEE
One Woody-Allen-ish philosophical gem, served with color,
animation, and a small amount of existential dread.
Pure standard library. No dependencies. No dignity.
"""

import sys
import time
import shutil

# ------------------------------------------------------------------ palette --
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"


def _c(n):
    return "\033[" + n + "m"


MAGENTA = _c("95")
CYAN    = _c("96")
YELLOW  = _c("93")
BLUE    = _c("94")
GREEN   = _c("92")
WHITE   = _c("97")
GRAY    = _c("90")
RED     = _c("91")


# --------------------------------------------------------------- box glyphs --
def _unicode_ok():
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        "╔═╗╚╝║".encode(enc)
        return True
    except (UnicodeEncodeError, LookupError):
        return False


if _unicode_ok():
    TL, TR, BL, BR, HZ, VT = "╔", "╗", "╚", "╝", "═", "║"
else:
    TL, TR, BL, BR, HZ, VT = "+", "+", "+", "+", "-", "|"


# ------------------------------------------------------------------ helpers --
def term_width():
    try:
        return shutil.get_terminal_size((72, 24)).columns
    except Exception:
        return 72


def pad_for(text, w=None):
    if w is None:
        w = term_width()
    return max(0, (w - len(text)) // 2)


def type_line(text, color="", delay=0.03, pad=None, bold=True, rule=False):
    """Type a single line, centered, character by character."""
    if pad is None:
        pad = pad_for(text)
    sys.stdout.write(" " * pad)
    sys.stdout.write(color + (BOLD if bold else DIM))
    sys.stdout.flush()
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay * (0.35 if ch == " " else 1.0))
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def thinking(label="Consulting the void", seconds=1.5):
    """A tiny spinner of dots, because indecision needs a soundtrack."""
    frames = ["   ", ".  ", ".. ", "..."]
    sys.stdout.write(GRAY + "   " + label + RESET + " ")
    sys.stdout.flush()
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sys.stdout.write("\b\b\b" + frames[i % len(frames)])
        sys.stdout.flush()
        i += 1
        time.sleep(0.18)
    sys.stdout.write("\b\b\b" + DIM + "(sorry)" + RESET + "\n")
    sys.stdout.flush()


def boxed_typewrite(lines, color=YELLOW, delay=0.032):
    """Draw a box and type the quote inside it, line by line."""
    width = max(len(l) for l in lines)
    inner = width + 6                       # 3 spaces of padding each side
    left_pad = max(0, (term_width() - (inner + 2)) // 2)
    pre = " " * left_pad

    bar = HZ * inner
    sys.stdout.write(pre + MAGENTA + TL + bar + TR + RESET + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

    for line in lines:
        sys.stdout.write(pre + MAGENTA + VT + RESET + "   ")
        sys.stdout.flush()
        for ch in line:
            sys.stdout.write(color + ch + RESET)
            sys.stdout.flush()
            time.sleep(delay * (0.25 if ch == " " else 1.0))
        remaining = (width - len(line)) + 3
        sys.stdout.write(" " * remaining + MAGENTA + VT + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.22)

    sys.stdout.write(pre + MAGENTA + BL + bar + BR + RESET + "\n")
    sys.stdout.flush()


# -------------------------------------------------------------- the content --
COFFEE = [
    "      ( (   ",
    "       ) )  ",
    "    ........ ",
    "    |      |]",
    "    \\      / ",
    "     `----'  ",
]

BANNER = "W O O D Y   A L L E N   S A Y S"

QUOTE = [
    "I'm not afraid of dying --",
    "I just don't want to be there when it happens.",
    "And knowing my luck it'll come on a Tuesday,",
    "right in the middle of a very good nap.",
]


def main():
    # --- gentle wake-up -----------------------------------------------------
    if not sys.stdout.isatty():
        # No terminal? Still print everything, just faster and quieter.
        pass

    print()
    time.sleep(0.15)

    # --- the coffee cup -----------------------------------------------------
    art_pad = pad_for(max(len(l) for l in COFFEE))
    for line in COFFEE:
        sys.stdout.write(" " * art_pad + CYAN + line + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.06)
    print()

    # --- the banner ---------------------------------------------------------
    type_line(BANNER, color=WHITE, delay=0.035, bold=True)
    time.sleep(0.15)

    rule = "- " * 22
    type_line(rule, color=GRAY, delay=0.008, bold=False)
    time.sleep(0.25)

    # --- a beat of neurotic hesitation -------------------------------------
    thinking("Consulting the void", 1.4)
    print()

    # --- the thought itself -------------------------------------------------
    boxed_typewrite(QUOTE, color=YELLOW, delay=0.028)
    time.sleep(0.35)

    # --- attribution --------------------------------------------------------
    type_line("-- overheard at 3 a.m., over a very small espresso",
              color=DIM + GREEN, delay=0.011, bold=False)
    print()

    # --- closing flourish ---------------------------------------------------
    shrug = "¯\\_(ツ)_/¯" if _unicode_ok() else "...whatever."
    type_line(shrug, color=RED, delay=0.05, bold=False)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET + "\n" + DIM + "  (fled the void)" + RESET + "\n")
        sys.stdout.flush()