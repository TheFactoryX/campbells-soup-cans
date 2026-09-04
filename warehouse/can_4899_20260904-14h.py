"""
Campbell's Soup Can #4899
Produced: 2026-09-04 14:22:16
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
Woody Allen Style Quote — Pure Python, ANSI-colored.
Prints one neurotic, philosophical quote with visual flair.
"""

import time
import sys

# ── ANSI escape sequences ─────────────────────────────────────────
RS = "\033[0m"    # reset
B  = "\033[1m"    # bold
R  = "\033[31m"   # red
G  = "\033[32m"   # green
Y  = "\033[33m"   # yellow
BL = "\033[34m"   # blue
M  = "\033[35m"   # magenta
C  = "\033[36m"   # cyan
W  = "\033[37m"   # white

# ── The one and only Woody Allen style quote ───────────────────────
QUOTE = (
    "I'm not afraid of death. "
    "I just don't want to be the one "
    "stuck explaining to the void "
    "why I spent so much time "
    "worrying about whether the toaster "
    "was unplugged."
)

# ── Color‑typewriter: prints text with per‑character color cycling ─
def type_color(text, delay=0.018, palette=None):
    if palette is None:
        palette = [R, G, Y, BL, M, C, W]
    for ch in text:
        if ch == " ":
            print(" ", end="", flush=True)
        else:
            print(palette[ord(ch) % len(palette)] + ch, end="", flush=True)
        time.sleep(delay)
    print(RS, end="")   # reset colour, keep cursor position

# ── Clear terminal (best‑effort) ──────────────────────────────────
def clear_term():
    try:
        print("\033[2J\033[H", end="")
    except Exception:
        pass

# ── Main ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    clear_term()

    # Playful header using box‑drawing characters
    header = C + B + "╔" + "═" * 60 + "╗" + RS
    print(header)
    print(C + B + "║" + " " * 60 + "║" + RS)
    print(C + B + "║" + " " * 23 + "NEUROTIC" + " " * 35 + "║" + RS)
    print(C + B + "║" + " " * 21 + "PHILOSOPHY" + " " * 37 + "║" + RS)
    print(C + B + "║" + " " * 60 + "║" + RS)
    print(C + B + "╚" + "═" * 60 + "╝" + RS)

    # Print the quote with colourful typewriter effect
    print()
    print(Y + "→" + RS + " ", end="")   # yellow arrow + space
    type_color(QUOTE, delay=0.015)

    # Final newline for tidiness
    print()