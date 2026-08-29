"""
Campbell's Soup Can #4864
Produced: 2026-08-29 02:12:11
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic, colorful, typewriter-delivered Woody Allen–style philosophical quote.
Pure Python — no external dependencies, run directly with `python3 woody.py`.
"""

import sys, time

# ── ANSI color codes ────────────────────────────────────────────
RS = "\033[0"   # reset  (we'll add the final 'm' at runtime for safety)
B  = "\033[1"   # bold
C  = "\033[96m" # cyan
Y  = "\033[93m" # yellow
G  = "\033[92m" # green
M  = "\033[95m" # magenta
R  = "\033[91m" # red

# Actually, let's use the proper full codes straight away:
RS = "\033[0m"
B  = "\033[1m"
C  = "\033[96m"
Y  = "\033[93m"
G  = "\033[92m"
M  = "\033[95m"
R  = "\033[91m"

# ── The Woody Allen style quote ──────────────────────────────────
# Embedded ANSI codes for segmented colors. Plain string, perfectly safe.
QUOTE = (
    C + "I don't want to achieve immortality through my work" + RS + " "
    + Y + "just to live long enough" + RS + " "
    + G + "to see if the refrigerator light turns off" + RS + " "
    + M + "when I close the door." + RS
)

# ── Typewriter effect using only built‑ins ───────────────────────
def typewriter(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ── A tiny decorative banner ─────────────────────────────────────
def banner():
    print(C + "▲" + RS + "  " + B + "Philosophical Musings" + RS + "  " + C + "▲" + RS)

# ── Entry point ──────────────────────────────────────────────────
if __name__ == "__main__":
    banner()

    # Subtle "thinking" prelude
    sys.stdout.write(R + "...thinking" + RS)
    for _ in range(3):
        sys.stdout.write(R + "." + RS)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n\n")

    # Typewriter reveal — each segment lights up in its own color
    typewriter(QUOTE)

    # Friendly footnote
    print("\n" + C + "─" + RS + "  existentialism served fresh  " + C + "─" + RS + "\n")