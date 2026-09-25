"""
Campbell's Soup Can #5022
Produced: 2026-09-25 13:48:43
Worker: Z.ai: GLM 5.3 Flash (z-ai/glm-5.3-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║           LATE NIGHT WITH EXISTENTIAL DREAD              ║
║       presents: one (1) quote, lightly neurotic          ║
╚══════════════════════════════════════════════════════════╝

Pure standard library. No dependencies. No refunds.
Run it. Contemplate. Blame the universe (it started it).
"""

import os
import random
import shutil
import sys
import textwrap
import time


# ---------------------------------------------------------------------------
# ANSI wardrobe (escape codes, ironed and folded)
# ---------------------------------------------------------------------------

def _wake_up_ansi():
    """On Windows, os.system('') switches on ANSI/VT escape-code processing.
    Nobody knows why it works. The universe works in mysterious ways."""
    if os.name == "nt":
        os.system("")


_wake_up_ansi()

try:  # go easy on cranky old consoles
    sys.stdout.reconfigure(errors="replace")
except Exception:
    pass

E            = "\033["
RESET        = E + "0m"
BOLD         = E + "1m"
DIM          = E + "2m"
ITALIC       = E + "3m"
AMBER        = E + "33m"
GRAY         = E + "90m"
YELLOW       = E + "93m"
CYAN         = E + "96m"
MAGENTA      = E + "95m"
WHITE        = E + "97m"
HIDE_CURSOR  = E + "?25l"
SHOW_CURSOR  = E + "?25h"
CLEAR_SCREEN = E + "2J" + E + "H"


# ---------------------------------------------------------------------------
# The goods
# ---------------------------------------------------------------------------

QUOTE = ("\"I finally asked the universe, 'Why am I here?' and after a long, "
         "uncomfortable pause it said, 'Honestly? We've all been wondering "
         "that.'\"")

GLASSES = (
    "   .-------.         .-------.   ",
    "   |       |_________|       |   ",
    "   |   o   |         |   o   |   ",
    "   |       |         |       |   ",
    "   '-------'         '-------'   ",
)


# ---------------------------------------------------------------------------
# Tiny stagehands
# ---------------------------------------------------------------------------

def w(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def cols():
    return shutil.get_terminal_size((80, 24)).columns


def pad_for(width):
    return " " * max(0, (cols() - width) // 2)


def paint_glasses(line):
    """Amber frames, cyan eyes. Very intellectual."""
    return AMBER + line.replace("o", RESET + CYAN + "o" + RESET + AMBER) + RESET


def paint_blink(line):
    """Lids closed. Still thinking. Mostly about the lids."""
    return AMBER + line.replace("-", RESET + CYAN + "-" + RESET + AMBER) + RESET


def nervous_type(text, color=WHITE, base=0.04, stutter=0.05):
    """Types like someone who rehearsed this in the shower for thirty years."""
    for i, ch in enumerate(text):
        w(color + ch + RESET)
        time.sleep(base + random.uniform(0.0, 0.02))
        if ch in ",;:":
            time.sleep(0.18)
        elif ch in ".!?":
            time.sleep(0.38)
        elif ch in "'\"":
            time.sleep(0.05)
        # occasionally un-say a letter, then commit anyway
        if stutter and i > 0 and ch.isalpha() and random.random() < stutter:
            time.sleep(random.uniform(0.15, 0.35))
            w("\b \b")                 # take it back
            time.sleep(random.uniform(0.10, 0.20))
            w(color + ch + RESET)      # ...say it again, coward
            time.sleep(random.uniform(0.10, 0.30))


# ---------------------------------------------------------------------------
# The show, in six small acts of dread
# ---------------------------------------------------------------------------

def act_i_marquee():
    title = "★  LATE NIGHT WITH EXISTENTIAL DREAD  ★"
    ind = pad_for(len(title))
    frames = [GRAY, DIM, MAGENTA, DIM, GRAY, MAGENTA + BOLD, DIM, MAGENTA + BOLD]
    w("\n\n")
    for style in frames:  # a neon sign with commitment issues
        w("\r" + ind + style + title + RESET)
        time.sleep(random.uniform(0.06, 0.18))
    time.sleep(0.4)
    sub = "proudly presents one (1) philosophical crisis, barely used"
    w("\n" + pad_for(len(sub)) + DIM + ITALIC + sub + RESET + "\n")
    time.sleep(1.0)


def act_ii_glasses():
    w("\n")
    for line in GLASSES:
        w(pad_for(len(line)) + paint_glasses(line) + "\n")
        time.sleep(0.12)
    time.sleep(0.35)
    blink_glasses()


def blink_glasses():
    open_line = pad_for(len(GLASSES[2])) + paint_glasses(GLASSES[2])
    shut_line = pad_for(len(GLASSES[2])) + paint_blink(GLASSES[2].replace("o", "-"))
    w("\r\033[3A" + shut_line)   # hop up to the lens line; lids close
    time.sleep(0.22)
    w("\r" + open_line)          # open again
    time.sleep(0.55)
    w("\r" + shut_line)          # one suspicious extra blink
    time.sleep(0.16)
    w("\r" + open_line + "\r\033[3B")  # settle back down


def act_iii_ahem():
    w("\n")
    w(pad_for(12) + GRAY + "( ")
    nervous_type("ahem", color=GRAY, base=0.12, stutter=0.5)
    w(" )" + RESET + "\n")
    time.sleep(0.4)


def act_iv_the_quote():
    inner = max(26, min(52, cols() - 18))
    lines = textwrap.wrap(QUOTE, width=inner)
    body = max(len(line) for line in lines)
    box_w = body + 6
    ind = pad_for(box_w)

    w("\n" + ind + CYAN + "╔")
    for _ in range(box_w - 2):        # the top border nervously extends itself
        w("═")
        time.sleep(0.006)
    w("╗" + RESET + "\n")
    w(ind + CYAN + "║" + RESET + " " * (box_w - 2) + CYAN + "║" + RESET + "\n")

    for line in lines:
        w(ind + CYAN + "║" + RESET + "   ")
        nervous_type(line, color=WHITE, base=0.04)
        w(" " * (body - len(line) + 3) + CYAN + "║" + RESET + "\n")
        time.sleep(0.12)

    w(ind + CYAN + "║" + RESET + " " * (box_w - 2) + CYAN + "║" + RESET + "\n")
    w(ind + CYAN + "╚")
    for _ in range(box_w - 2):
        w("═")
        time.sleep(0.006)
    w("╝" + RESET + "\n")


def act_v_drift():
    frames = ["·    ·    ·", " ·   ·   · ", "  ·  ·  ·  ", " ·   ·   · "]
    palette = [GRAY, CYAN, MAGENTA]
    pad = pad_for(11)
    for i in range(10):               # thoughts, wandering, off the leash
        w("\r" + pad + palette[i % 3] + frames[i % 4] + RESET)
        time.sleep(0.2)
    w("\r" + " " * (len(pad) + 11) + "\r")
    time.sleep(0.2)


def act_vi_credits():
    w("\n")
    attr = "— overheard at the corner of Existence & 81st St."
    w(pad_for(len(attr)) + DIM + ITALIC + attr + RESET + "\n")
    time.sleep(1.1)
    note = ("( The universe was reached for comment. "
            "It has not returned a call since the Big Bang. )")
    w(pad_for(len(note)) + GRAY + note + RESET + "\n")
    time.sleep(1.2)
    w("\n" + pad_for(9))
    for ch in "f  i  n  .":
        w(GRAY + ch + RESET)
        time.sleep(0.25)
    w("\n")


def main():
    w(HIDE_CURSOR + CLEAR_SCREEN)
    try:
        act_i_marquee()
        act_ii_glasses()
        act_iii_ahem()
        act_iv_the_quote()
        act_v_drift()
        act_vi_credits()
    finally:
        w(SHOW_CURSOR + RESET + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        w("\n" + GRAY + "Fled mid-crisis. Honestly? Same." + RESET + "\n")