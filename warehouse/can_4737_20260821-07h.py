"""
Campbell's Soup Can #4737
Produced: 2026-08-21 07:10:10
Worker: Ox Alpha (stealth/ox-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
THE EXISTENTIAL HOTLINE
=======================
A fully unqualified philosophical delivery system.
Dispenses exactly one (1) neurotic quote per run.
No dependencies. No answers. Please do not shake the universe.
"""

import os
import sys
import time
import random
import textwrap
import shutil

# ----------------------------------------------------------------- setup --
os.system("")  # sneaky trick: enables ANSI escape codes on Windows 10+

try:  # help fancy characters survive on any platform
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET, BOLD, DIM = "\033[0m", "\033[1m", "\033[2m"
RED, GREEN, YELLOW = "\033[91m", "\033[92m", "\033[93m"
BLUE, MAGENTA, CYAN, WHITE = "\033[94m", "\033[95m", "\033[96m", "\033[97m"
RAINBOW = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

TITLE = "✦ ˚ · THE EXISTENTIAL HOTLINE · ˚ ✦"
SUBTITLE = "est. 3 a.m., obviously"

QUOTE = ("I've spent nine years in therapy learning to accept that the "
         "universe is cold, chaotic, and completely indifferent. Then last "
         "week the universe canceled our session. Even nihilism is "
         "standing me up.")

ATTRIBUTION = "— a man who alphabetizes his anxieties"
FOOTER = "☎ your existential crisis is important to us. please hold."


# --------------------------------------------------------------- helpers --
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def width():
    try:
        return max(shutil.get_terminal_size().columns, 46)
    except Exception:
        return 80


def centered(text):
    w = width()
    return "
".join(line.center(w) for line in text.splitlines())


def say(text, color=WHITE, base=0.02, jitter=0.02, end="
"):
    """Type text out with a nervous, human stutter."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        delay = base + random.uniform(0, jitter)
        if ch in ".,!?—":
            delay += random.uniform(0.06, 0.16)  # dramatic hesitation
        time.sleep(delay)
    sys.stdout.write(RESET + end)


def think(message, seconds=1.2):
    """Spin a little braille brain while pretending to ponder."""
    w = width()
    visible = 2 + len(message)
    pad = max((w - visible) // 2, 0)
    end_at = time.time() + seconds
    i = 0
    while time.time() < end_at:
        frame = SPINNER[i % len(SPINNER)]
        sys.stdout.write("\r" + " " * pad +
                         f"{CYAN}{frame}{RESET} {DIM}{message}{RESET}")
        sys.stdout.flush()
        time.sleep(0.07)
        i += 1
    sys.stdout.write("\r" + " " * w + "\r")


def glasses():
    """Perfectly aligned round spectacles, built with math (anxiety-free)."""
    lens, bridge, indent = "| o  o |", "=" * 14, 2
    mid = " " * indent + lens + bridge + lens
    n = len(mid)
    top, bot = [" "] * n, [" "] * n
    for s in (indent, indent + len(lens) + len(bridge)):
        top[s + 1], top[s + 6] = "/", "\"
        bot[s + 1], bot[s + 6] = "\", "/"
        for k in range(s + 2, s + 6):
            bot[k] = "_"
    return "
".join(("".join(top), mid, "".join(bot)))


def nervous_dots(rounds=2):
    """Start a sentence. Abort. Repeat. Extremely on-brand."""
    lead = " " * (width() // 2 - 2)
    for _ in range(rounds):
        for k in range(1, 4):
            sys.stdout.write("\r" + lead + "." * k)
            sys.stdout.flush()
            time.sleep(0.22)
        time.sleep(0.45)
        sys.stdout.write("\r" + " " * (len(lead) + 3) + "\r")
        time.sleep(0.12)
    sys.stdout.write(lead + "..." + RESET + "
")


def rainbow(text):
    parts = []
    for i, ch in enumerate(text):
        parts.append(RAINBOW[i % len(RAINBOW)] + ch)
    return "".join(parts) + RESET


# ----------------------------------------------------------------- show ---
def main():
    clear()

    # -- marquee ----------------------------------------------------------
    say(centered(TITLE), color=YELLOW + BOLD, base=0.012, jitter=0.010)
    say(centered(SUBTITLE), color=DIM, base=0.008, jitter=0.006)
    print()

    # -- pretend this is a professional operation --------------------------
    think("consulting inner demons", 1.3)
    print()

    # -- the thinker (well, the eyewear) -----------------------------------
    for line in centered(glasses()).splitlines():
        sys.stdout.write(CYAN + BOLD + line + RESET + "
")
        time.sleep(0.18)
    print()
    nervous_dots()
    print()

    # -- the quote, framed like it matters ----------------------------------
    inner = min(width() - 8, 62)
    lines = textwrap.wrap(QUOTE, inner)
    box_w = max(len(l) for l in lines) + 4

    print(rainbow("╔" + "═" * box_w + "╗"))
    for ln in lines:
        sys.stdout.write(MAGENTA + "║" + RESET + "  ")
        say(ln, color=WHITE + BOLD, base=0.022, jitter=0.015, end="")
        sys.stdout.write(" " * (box_w - 2 - len(ln)) +
                         MAGENTA + "║" + RESET + "
")
        time.sleep(0.05)
    print(rainbow("╚" + "═" * box_w + "╝"))

    # -- credit where overdue ------------------------------------------------
    print()
    say(centered(ATTRIBUTION), color=MAGENTA, base=0.020, jitter=0.015)

    # -- hold music for the soul ----------------------------------------------
    say(centered(FOOTER), color=DIM, base=0.006, jitter=0.004)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "

(he left abruptly. classic.)
")