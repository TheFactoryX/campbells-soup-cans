"""
Campbell's Soup Can #4369
Produced: 2026-07-29 19:43:31
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic philosophical musing, served with a side of ASCII anxiety.
No external dependencies. Just pure, unadulterated existential dread.
"""

import sys
import time
import random

# ── ANSI Palette ──────────────────────────────────────────────────────
RST   = "\033[0m"
BLD   = "\033[1m"
DIM   = "\033[2m"
ITL   = "\033[3m"
UL    = "\033[4m"
BLK   = "\033[30m"
RED   = "\033[31m"
GRN   = "\033[32m"
YEL   = "\033[33m"
BLU   = "\033[34m"
MAG   = "\033[35m"
CYN   = "\033[36m"
WHT   = "\033[37m"
BG_BLK= "\033[40m"
BG_WHT= "\033[47m"

# ── Woody-approved quote ──────────────────────────────────────────────
QUOTE = (
    "I told my analyst I had a fear of commitment,\n"
    "so he committed me. Now we're both afraid of each other."
)

# ── ASCII frame pieces ────────────────────────────────────────────────
TL, TR = "┌", "┐"
BL, BR = "└", "┘"
H, V   = "─", "│"
L1, R1 = "├", "┤"
L2, R2 = "┤", "├"  # mirrored for inner accent

# ── Helpers ───────────────────────────────────────────────────────────
def clear_line():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def typewriter(text, delay=0.018, color=WHT):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pulse(text, cycles=3, colors=(YEL, MAG, CYN)):
    for _ in range(cycles):
        for c in colors:
            clear_line()
            sys.stdout.write(f"\r{BLD}{c}{text}{RST}")
            sys.stdout.flush()
            time.sleep(0.25)
    print()

def draw_box(lines, width=None, pad=2, border_color=CYN, title=""):
    if width is None:
        width = max(len(l) for l in lines) + pad * 2
    inner_w = width - 2
    top = f"{border_color}{TL}{H * (inner_w)}{TR}{RST}"
    bot = f"{border_color}{BL}{H * (inner_w)}{BR}{RST}"
    print(top)
    if title:
        t = f" {title} "
        print(f"{border_color}{V}{RST}{t.center(inner_w)}{border_color}{V}{RST}")
        print(f"{border_color}{L1}{H * (inner_w)}{R1}{RST}")
    for l in lines:
        print(f"{border_color}{V}{RST} {l.ljust(inner_w - 2)} {border_color}{V}{RST}")
    print(bot)

# ── Main show ─────────────────────────────────────────────────────────
def main():
    # Intro: nervous blinking cursor
    for _ in range(6):
        sys.stdout.write(f"\r{DIM}▌{RST}")
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write(f"\r{DIM}▐{RST}")
        sys.stdout.flush()
        time.sleep(0.12)
    clear_line()

    # Title card
    draw_box(
        [
            f"{BLD}{MAG}WOODY ALLEN'S DAILY DOSE OF DREAD{RST}",
            f"{DIM}Prescription: 1 quote, 0 side effects (except nausea){RST}",
        ],
        title=f"{YEL}⚕ MEDICAL RECORD{RST}",
        border_color=MAG,
    )
    print()

    # The quote – typed out with neurotic pacing
    typewriter(f"{ITL}{CYN}“{RST}", delay=0.04, color=CYN)
    for line in QUOTE.split("\n"):
        typewriter(line, delay=0.022, color=WHT)
    typewriter(f"{ITL}{CYN}”{RST}", delay=0.04, color=CYN)
    print()

    # A little existential footer animation
    pulse(f"{DIM}💊  Take with a grain of salt… or a whole shaker.{RST}", cycles=2)
    print()

    # Final decorative sign-off
    draw_box(
        [
            f"{GRN}Status:{RST} {YEL}Neurotic but stable{RST}",
            f"{GRN}Next appointment:{RST} {MAG}Whenever the universe allows{RST}",
        ],
        title=f"{BLU}📋 PROGNOSIS{RST}",
        border_color=GRN,
    )

    # Tiny easter egg
    if random.random() < 0.15:
        print(f"\n{DIM}...and remember: {ITL}the light at the end of the tunnel{RST}{DIM} might just be a freight train.{RST}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Session terminated. Patient fled the room.{RST}")