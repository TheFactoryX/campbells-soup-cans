"""
Campbell's Soup Can #4281
Produced: 2026-07-21 18:40:17
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ── ANSI color palette ──────────────────────────────────────────────
RST  = "\033[0m"
BLD  = "\033[1m"
DIM  = "\033[2m"
ITL  = "\033[3m"
UL   = "\033[4m"
BLK  = "\033[30m"
RED  = "\033[31m"
GRN  = "\033[32m"
YEL  = "\033[33m"
BLU  = "\033[34m"
MAG  = "\033[35m"
CYN  = "\033[36m"
WHT  = "\033[37m"
BG_BLK = "\033[40m"
BG_RED = "\033[41m"
BG_GRN = "\033[42m"
BG_YEL = "\033[43m"
BG_BLU = "\033[44m"
BG_MAG = "\033[45m"
BG_CYN = "\033[46m"
BG_WHT = "\033[47m"

# ── Woody Allen quote (original, neurotic, existential) ─────────────
QUOTE = (
    "I told my therapist I have a fear of commitment. "
    "She said, 'That'll be $200.' I said, 'Can I pay you next week?' "
    "She said, 'That's exactly the problem.'"
)

# ── ASCII art: Woody-ish glasses + neurotic swirl ───────────────────
GLASSES = [
    "       ▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄      ",
    "      ██████████     ██████████     ",
    "      ██████████     ██████████     ",
    "       ▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀      ",
    "            ▀▀▀▀▀▀▀▀▀▀▀▀             ",
]

SWIRL_FRAMES = [
    "   @   ",
    "  @ @  ",
    " @   @ ",
    "@     @",
    " @   @ ",
    "  @ @  ",
]

# ── Helper: typewriter print ────────────────────────────────────────
def typewriter(text, color=WHT, delay=0.012, end="\n"):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RST}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

# ── Helper: center text in width ────────────────────────────────────
def center_text(text, width=70):
    return text.center(width)

# ── Main animation ──────────────────────────────────────────────────
def main():
    # Clear screen + hide cursor
    sys.stdout.write("\033[2J\033[H\033[?25l")
    sys.stdout.flush()

    width = 70

    # 1. Title card with pulsing colors
    title = "WOODY ALLEN'S DAILY EXISTENTIAL CRISIS™"
    for pulse in range(6):
        c = [RED, YEL, GRN, CYN, BLU, MAG][pulse % 6]
        sys.stdout.write(f"\033[H{c}{BLD}{center_text(title, width)}{RST}\n")
        sys.stdout.flush()
        time.sleep(0.15)

    # 2. Draw glasses with color sweep
    for i, line in enumerate(GLASSES):
        color = [RED, YEL, GRN, CYN, BLU, MAG][i % 6]
        sys.stdout.write(f"{color}{center_text(line, width)}{RST}\n")
        sys.stdout.flush()
        time.sleep(0.08)

    # 3. Swirling anxiety animation (3 cycles)
    for _ in range(3):
        for frame in SWIRL_FRAMES:
            sys.stdout.write(f"\033[{5 + len(GLASSES)};0H{MAG}{center_text(frame, width)}{RST}")
            sys.stdout.flush()
            time.sleep(0.12)

    # 4. Blank line then typewriter quote
    sys.stdout.write(f"\033[{7 + len(GLASSES)};0H")
    sys.stdout.flush()
    time.sleep(0.3)

    # Quote in chunks for dramatic pauses
    chunks = QUOTE.split(". ")
    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if not chunk.endswith("."):
            chunk += "."
        typewriter(center_text(chunk, width), color=CYN, delay=0.018)
        time.sleep(0.45)

    # 5. Final neurotic footer
    time.sleep(0.5)
    footers = [
        "- Woody Allen, probably",
        "(as dictated to his analyst, 1977)",
        "Disclaimer: Not actually Woody Allen. Please don't sue.",
        "My mother liked this quote. She said it's 'nice.'",
    ]
    footer = random.choice(footers)
    typewriter(center_text(footer, width), color=DIM + YEL, delay=0.02)

    # 6. Fade out glasses
    for fade in range(5, -1, -1):
        alpha = fade / 5.0
        # Simulate fade by dimming
        sys.stdout.write(f"\033[H{DIM}")
        for line in GLASSES:
            sys.stdout.write(f"{center_text(line, width)}\n")
        sys.stdout.write(RST)
        sys.stdout.flush()
        time.sleep(0.08)

    # Show cursor again
    sys.stdout.write("\033[?25h\033[0m\n")
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\033[0m\n")
        sys.stdout.flush()