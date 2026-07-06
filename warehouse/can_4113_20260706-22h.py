"""
Campbell's Soup Can #4113
Produced: 2026-07-06 22:38:12
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
A neurotic philosophical moment with Woody Allen.
Pure Python, zero dependencies, maximum existential dread.
"""

import sys
import time
import random

# ── ANSI Color Palette ──────────────────────────────────────────────
class C:
    RST = '\033[0m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL  = '\033[4m'
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ── The Quote (original, Woody-style) ───────────────────────────────
QUOTE = (
    "I told my analyst I have a fear of commitment.\n"
    "He said, 'That's very common.'\n"
    "I said, 'Great, so I'm not special \u2014 even my neuroses are generic.'\n"
    "He nodded. 'Would you like to book another session?'\n"
    "I said, 'I can't commit to that.'"
)

SIGNATURE = "\u2014 Woody Allen (probably, or just some guy in a turtleneck)"

# ── ASCII Art: A tiny neurotic stick figure ─────────────────────────
STICK_FIGURE = [
    f"       {C.CYN}@{C.RST}",
    f"      {C.CYN}/|\\{C.RST}",
    f"      {C.CYN}/ \\{C.RST}",
    f"     {C.DIM}(therapy bill){C.RST}",
]

# ── Animation helpers ───────────────────────────────────────────────
def typewriter(text: str, delay: float = 0.012, color: str = C.WHT):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.004, 0.004))
    print()

def fade_in(text: str, color: str = C.YEL, steps: int = 8):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps):
        intensity = int(232 + (i / steps) * 23)
        sys.stdout.write(f"\r\033[38;5;{intensity}m{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.06)
    print()

def blink_text(text: str, times: int = 3, color: str = C.RED):
    """Make text blink annoyingly."""
    for _ in range(times):
        sys.stdout.write(f"\r{color}{C.BLD}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.35)
        sys.stdout.write(f"\r{' ' * len(text)}")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write(f"\r{color}{text}{C.RST}\n")

# ── Box drawing ─────────────────────────────────────────────────────
def draw_box(lines: list[str], border_color: str = C.MAG, title: str = "") -> str:
    """Wrap lines in a fancy Unicode box."""
    max_len = max(len(line) for line in lines) if lines else 0
    max_len = max(max_len, len(title))
    pad = 2
    inner_w = max_len + pad * 2

    tl, tr = "┌", "┐"
    bl, br = "└", "┘"
    h, v = "─", "│"

    top = f"{border_color}{tl}{h * inner_w}{tr}{C.RST}"
    bot = f"{border_color}{bl}{h * inner_w}{br}{C.RST}"

    result = [top]
    if title:
        title_line = f"{border_color}{v}{C.RST} {C.BLD}{C.YEL}{title.center(max_len)}{C.RST} {border_color}{v}{C.RST}"
        result.append(title_line)
        result.append(f"{border_color}{v}{h * inner_w}{v}{C.RST}")

    for line in lines:
        visible_len = len(line)
        # strip ANSI for width calc
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = max_len - len(clean)
        result.append(f"{border_color}{v}{C.RST} {line}{' ' * padding} {border_color}{v}{C.RST}")

    result.append(bot)
    return "\n".join(result)

# ── Main spectacle ──────────────────────────────────────────────────
def main():
    # Clear screen & hide cursor
    sys.stdout.write("\033[2J\033[H\033[?25l")
    sys.stdout.flush()

    # 1. Tiny animated entrance
    time.sleep(0.3)
    for frame in [
        "        .",
        "       . .",
        "      .   .",
        "     .     .",
        "    .  \\o/  .",
        "   .   /|\\   .",
        "  .    / \\    .",
        " .  (existential dread)  .",
    ]:
        sys.stdout.write(f"\033[H\033[2J{C.DIM}{frame}{C.RST}\n")
        sys.stdout.flush()
        time.sleep(0.12)

    # 2. Draw the stick figure
    sys.stdout.write("\033[H\033[2J")
    for line in STICK_FIGURE:
        print(line)
    time.sleep(0.5)

    # 3. Typewriter the quote inside a box
    quote_lines = QUOTE.split("\n")
    boxed = draw_box(quote_lines, border_color=C.CYN, title=" SESSION NOTES ")
    print()
    print(boxed)
    print()

    # 4. Typewriter the signature with hesitation
    time.sleep(0.4)
    typewriter("   Analyst's note: ", delay=0.02, color=C.DIM)
    typewriter("Patient exhibits classic avoidance ", delay=0.015, color=C.YEL)
    blink_text("AND", times=2, color=C.RED)
    typewriter(" a troubling wit.", delay=0.015, color=C.YEL)
    print()

    time.sleep(0.3)
    fade_in(f"   {SIGNATURE}", color=C.MAG)
    print()

    # 5. Final neurotic flourish
    time.sleep(0.4)
    flourishes = [
        f"{C.DIM}* adjusts glasses nervously *{C.RST}",
        f"{C.DIM}* checks pulse *{C.RST}",
        f"{C.DIM}* wonders if this print statement is a metaphor for mortality *{C.RST}",
    ]
    for f in flourishes:
        typewriter(f"   {f}", delay=0.008, color=C.BLU)
        time.sleep(0.15)

    print()
    print(f"   {C.GRN}{C.ITL}Quote generated. Existence continues. Unfortunately.{C.RST}")
    print()

    # Show cursor again
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(f"\n{C.RED}\033[?25hInterrupted. Even the code has commitment issues.{C.RST}\n")