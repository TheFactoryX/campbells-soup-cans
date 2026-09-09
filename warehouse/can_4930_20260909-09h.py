"""
Campbell's Soup Can #4930
Produced: 2026-09-09 09:47:07
Worker: Nex AGI: Nex-N2.5-Pro (free) (nex-agi/nex-n2.5-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One funny philosophical quote, typeset with love and dread.
Pure Python. No dependencies. Mild anxiety included.
"""

import re
import sys
import time
import random
import shutil

# ---------------- ANSI escape palette ----------------
ESC = "\033["
RESET   = ESC + "0m"
BOLD    = ESC + "1m"
DIM     = ESC + "2m"
ITALIC  = ESC + "3m"
BLINK   = ESC + "5m"

def tc(r, g, b):
    return ESC + "38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

RAINBOW = [
    tc(255,  85,  85),   # red
    tc(255, 165,  60),   # orange
    tc(255, 235,  60),   # yellow
    tc( 85, 255, 120),   # green
    tc( 60, 190, 255),   # sky blue
    tc(170, 110, 255),   # violet
    tc(255,  90, 200),   # pink
]
GOLD  = tc(255, 205, 110)
CYAN  = tc(120, 240, 240)
WHITE = tc(240, 240, 245)
GRAY  = tc(140, 140, 150)
RED   = tc(255, 110, 110)

ANSI_RE = re.compile(r"\033\[[0-9;]*m")

def vlen(s):
    """Visible length of a string (ANSI codes count as zero)."""
    return len(ANSI_RE.sub("", s))

TERM_W = shutil.get_terminal_size((80, 20)).columns

def center(text, width=None):
    width = width or TERM_W
    pad = max(0, (width - vlen(text)) // 2)
    return " " * pad + text

def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

_rainbow_i = 0

def typewrite_line(text, speed=0.022):
    """Type one line in a continuous cycling rainbow, with neurotic pauses."""
    global _rainbow_i
    for ch in text:
        sys.stdout.write(RAINBOW[_rainbow_i % len(RAINBOW)] + ch)
        _rainbow_i += 1
        sys.stdout.flush()
        pause = speed * (0.6 + random.random() * 0.9)
        if ch in ".,:;—-":
            pause += 0.10
        elif ch in "!?":
            pause += 0.25
        time.sleep(pause)
    sys.stdout.write(RESET)
    sys.stdout.flush()

def typewrite_plain(text, color, speed=0.03):
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        if not ch.isspace():
            time.sleep(speed)
    sys.stdout.write(RESET)
    sys.stdout.flush()

def print_title():
    inner = "✦  ONE THOUGHT · ONE CRISIS  ✦"
    w = len(inner) + 6
    lines = [
        GOLD + "╔" + "═" * w + "╗" + RESET,
        GOLD + "║" + RESET + "  " + BOLD + WHITE + inner + RESET + "  " + GOLD + "║" + RESET,
        GOLD + "╚" + "═" * w + "╝" + RESET,
    ]
    print()
    for ln in lines:
        print(center(ln))
    print()

def loading():
    stages = [
        "questioning childhood",
        "blaming parents",
        "reconsidering brunch",
        "fearing tuesdays",
        "achieving dread",
    ]
    bar_w = 28
    label_w = 24
    for i in range(bar_w + 1):
        frac = i / bar_w
        stage = stages[min(int(frac * len(stages)), len(stages) - 1)]
        filled = int(frac * bar_w)
        bar = GOLD + "█" * filled + DIM + "░" * (bar_w - filled) + RESET
        pct = str(int(frac * 100))
        label = CYAN + (stage.capitalize() + "...").ljust(label_w) + RESET
        line = "  " + label + "  [" + bar + "] " + pct + "%"
        sys.stdout.write("\r" + center(line))
        sys.stdout.flush()
        time.sleep(0.05 + random.random() * 0.06)
    sys.stdout.write("\n")

def face_block(eyes):
    return [
        GOLD + '       .-""""""""-.' + RESET,
        GOLD + '      /            \\' + RESET,
        GOLD + '      | ' + RESET + RED + eyes + RESET + GOLD + ' |' + RESET,
        GOLD + '      |     __     |' + RESET,
        GOLD + '       \\    (__)    /' + RESET,
        GOLD + "       '-........-'" + RESET,
    ]

def animate_face():
    """A small mind, darting nervously."""
    frames = [
        "(o)    (o)",
        "(•)    (•)",
        "(⊙)    (⊙)",
        "(o)    (•)",
        "(•)    (o)",
        "(⊙)    (o)",
        "(o)    (o)",
    ]
    for idx, eyes in enumerate(frames):
        block = face_block(eyes)
        if idx == 0:
            for ln in block:
                print(center(ln))
        else:
            sys.stdout.write("\033[6F")   # cursor up: redraw in place
            for ln in block:
                print(center(ln))
        sys.stdout.flush()
        time.sleep(0.28 + random.random() * 0.12)

QUOTE = ("I'm not afraid of death. I just find the whole concept poorly "
         "organized: no clear dress code, mysterious catering, and I'd "
         "really rather not be the main event.")

ATTR  = "— a thought, overthought, and gently regretted"
FOOT1 = "no action required. nothing ever is."
FOOT2 = "· the end? there is no end ·"

def print_quote_box():
    W = max(34, min(66, TERM_W - 8))
    lines = wrap(QUOTE, W)
    top = GOLD + "╔" + "═" * W + "╗" + RESET
    bot = GOLD + "╚" + "═" * W + "╝" + RESET
    pad = " " * max(0, (TERM_W - vlen(top)) // 2)
    print(pad + top)
    for ln in lines:
        sys.stdout.write(pad + GOLD + "║" + RESET)
        typewrite_line(ln)
        sys.stdout.write(GOLD + " " * (W - len(ln)) + "║" + RESET + "\n")
        sys.stdout.flush()
    time.sleep(0.5)   # dramatic beat before the lid closes
    print(pad + bot)

def main():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    print_title()
    loading()

    print()
    animate_face()
    print(center(DIM + "the mind, mid-crisis" + RESET))

    print()
    typewrite_plain(center("the thought arrives, uninvited:"), GRAY + ITALIC, 0.035)
    print()

    print_quote_box()

    print()
    print(center(DIM + ITALIC + ATTR + RESET))
    print()
    print(center(DIM + FOOT1 + RESET))
    print(center(BLINK + GRAY + FOOT2 + RESET))
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\n" + center(DIM + "aborted. existence resumes anyway." + RESET) + "\n")