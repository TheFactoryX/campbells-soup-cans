"""
Campbell's Soup Can #4763
Produced: 2026-08-22 09:42:51
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
============================================================================
   THE EXISTENTIAL MATINEE
   ~~~~~~~~~~~~~~~~~~~~~~~
   A one-quote, fully neurotic theatrical experience in pure Python.
   No dependencies. Best enjoyed in a color terminal, ideally anxiously.
   (Ctrl+C works too -- avoidance is a valid coping strategy.)
============================================================================
"""

import os
import re
import sys
import time
import random
import shutil
import textwrap

# ------------------------------------------------------------- ANSI toolkit --
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
ITAL  = "\033[3m"

def fg(c): return "\033[38;5;%dm" % c
def bg(c): return "\033[48;5;%dm" % c

CREAM = fg(231)
GOLD  = fg(220)
AMBER = fg(178)
TEAL  = fg(80)
LILAC = fg(183)
GREY  = fg(245)
SMOKE = fg(240)

ANSI_RE = re.compile(r"\033\[[0-9;]*m")

def plain(s):
    return ANSI_RE.sub("", s)

def term_width():
    return max(shutil.get_terminal_size().columns, 46)

def center(s, width=None):
    w = width or term_width()
    pad = max(0, (w - len(plain(s))) // 2)
    return " " * pad + s

def clear():
    sys.stdout.write("\033[2J\033[H")

def hide_cursor():
    sys.stdout.write("\033[?25l"); sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h"); sys.stdout.flush()

def nap(t):
    time.sleep(t)

def enable_ansi():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

def type_out(text, color=CREAM, delay=0.045, newline=True):
    """Nervous little typewriter."""
    sys.stdout.write(" " * max(0, (term_width() - len(text)) // 2))
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        stretch = 2.2 if ch in ",;—" else (1.6 if ch in ".!?…" else 1.0)
        nap(delay * stretch * random.uniform(0.75, 1.25))
    sys.stdout.write(RESET)
    if newline:
        sys.stdout.write("
")
    sys.stdout.flush()

# ------------------------------------------------------------ the production --
TITLE    = "✦  THE EXISTENTIAL MATINEE  ✦"
SUBTITLE = "a nervous production in one act"

QUOTE  = ("I'm not afraid of eternity. "
          "I'm just worried it'll be exactly like this, only longer.")
BYLINE = "— overheard outside a therapist's office, probably"

def title_sequence():
    shades = [fg(53), fg(97), fg(134), fg(176), fg(134), fg(97)]
    for shade in shades:
        clear()
        print("
" * 5)
        print(center(BOLD + shade + TITLE + RESET))
        print("")
        print(center(DIM + GREY + SUBTITLE + RESET))
        nap(0.22)
    for shown in (True, False, True, False, True):
        clear()
        print("
" * 5)
        print(center(BOLD + LILAC + TITLE + RESET))
        print("")
        print(center(DIM + GREY + SUBTITLE + RESET))
        print("")
        if shown:
            print(center(GOLD + "presents" + RESET))
        nap(0.16)
    nap(0.5)

# ------------------------------------------------------------------ curtain --
CURTAIN_ROWS = 10

def velvet(width, row, fringe=False):
    cells = []
    for i in range(width):
        if fringe:
            cells.append(bg(52) + GOLD + "▄")
        else:
            shade = 52 if ((i // 3) + row) % 2 == 0 else 88
            cells.append(bg(shade) + " ")
    return "".join(cells) + RESET

def curtain_open():
    cols = term_width()
    steps = 18
    for s in range(steps + 1):
        t = s / steps
        eased = 1 - (1 - t) ** 2
        gap = int((cols - 4) * eased)
        half = max(0, (cols - gap) // 2)
        right = max(0, cols - gap - half)
        clear()
        print("
" * 2)
        for r in range(CURTAIN_ROWS):
            fringe = (r == CURTAIN_ROWS - 1)
            print(velvet(half, s, fringe) + " " * gap +
                  velvet(right, s + 1, fringe))
        nap(0.045)
    nap(0.25)

# -------------------------------------------------------------------- stage --
CONE = [
    "╲     │     ╱",
    " ╲    │    ╱",
    "  ╲   │   ╱",
    "   ╲  │  ╱",
    "    ╲ │ ╱",
    "     ╲▼╱",
]

GLASSES_TOP   = "    .─────────." + " " * 13 + ".─────────."
GLASSES_UPPER = "   ╱           ╲" + " " * 11 + "╱           ╲"
GLASSES_MID   = ("  " + GOLD + "│" + RESET + " " * 6 + TEAL + "◉" + RESET +
                 " " * 6 + GOLD + "│" + RESET + GOLD + "─" * 9 + RESET +
                 GOLD + "│" + RESET + " " * 6 + TEAL + "◉" + RESET +
                 " " * 6 + GOLD + "│" + RESET)
GLASSES_LOWER = "   ╲           ╱" + " " * 11 + "╲           ╱"
GLASSES_BOT   = "    '─────────'" + " " * 13 + "'─────────'"

def glasses_lines():
    plain_lines = [GLASSES_TOP, GLASSES_UPPER, None, GLASSES_LOWER, GLASSES_BOT]
    out = []
    for ln in plain_lines:
        if ln is None:
            out.append(center(GLASSES_MID))
        else:
            out.append(center(BOLD + GOLD + ln + RESET))
    return out

STAR_CHARS = ["·", "+", "*", "✦"]

def make_stars(count=26):
    cols = term_width()
    return [(random.randint(1, 7), random.randint(2, cols - 3))
            for _ in range(count)]

def star_field(stars, phase):
    grid = {}
    for (r, c) in stars:
        ch = STAR_CHARS[(c + phase) % len(STAR_CHARS)]
        col = GOLD if ch == "✦" else (AMBER if ch == "*" else SMOKE)
        grid.setdefault(r, {})[c] = col + ch + RESET
    lines = []
    for r in range(1, max(rr for rr, _ in stars) + 1):
        line = grid.get(r, {})
        if not line:
            lines.append("")
            continue
        buf = [" "] * (max(line) + 1)
        for c, s in line.items():
            buf[c] = s
        lines.append("".join(buf))
    return lines

def cone_lines():
    out = []
    for ln in CONE:
        if "▼" in ln:
            left, right = ln.split("▼")
            body = (DIM + AMBER + left + RESET + BOLD + GOLD + "▼" + RESET +
                    DIM + AMBER + right + RESET)
        else:
            body = DIM + AMBER + ln + RESET
        out.append(center(body))
    return out

def stage_frame(stars, phase, glasses_count):
    parts = [""]
    parts += star_field(stars, phase)
    parts += cone_lines()
    parts += glasses_lines()[:glasses_count]
    return "
".join(parts)

def stage_scene():
    stars = make_stars()
    total = 5
    for phase in range(14):
        clear()
        print(stage_frame(stars, phase, min(total, 1 + phase // 3)))
        nap(0.12)
    clear()
    print(stage_frame(stars, 14, total))
    nap(0.4)

def nervous_aside():
    nap(0.6)
    type_out("( he adjusts his glasses, twice )",
             color=DIM + ITAL + GREY, delay=0.03)
    nap(0.4)
    type_out("( clears throat )",
             color=DIM + ITAL + GREY, delay=0.05)
    nap(0.5)
    print()

# --------------------------------------------------------------- quote card --
def quote_card():
    lines = textwrap.wrap(QUOTE, 36)
    inner = max(len(l) for l in lines) + 4
    pad = max(0, (term_width() - (inner + 2)) // 2)
    top = GOLD + "╭" + "─" * inner + "╮" + RESET
    bot = GOLD + "╰" + "─" * inner + "╯" + RESET
    side_l = GOLD + "│" + RESET
    side_r = GOLD + "│" + RESET

    def row_text(txt):
        return CREAM + ITAL + txt + " " * (inner - 2 - len(txt)) + RESET

    print()
    print(" " * pad + top)
    for _ in lines:
        print(" " * pad + side_l + " " * inner + side_r)
    print(" " * pad + bot)
    nap(0.35)

    sys.stdout.write("\033[%dA" % len(lines))  # hop up to first interior row
    for line in lines:
        for k in range(1, len(line) + 1):
            sys.stdout.write("\r" + " " * pad + side_l + " " +
                             row_text(line[:k]) + " " + side_r + "\033[K")
            sys.stdout.flush()
            ch = line[k - 1]
            stretch = 2.4 if ch in ",;—" else (1.7 if ch in ".!?…" else 1.0)
            nap(0.05 * stretch * random.uniform(0.8, 1.2))
        sys.stdout.write("
")
        sys.stdout.flush()
    sys.stdout.write("\033[1B")                # hop back below the card
    sys.stdout.flush()

def byline():
    nap(0.3)
    for col in (SMOKE, GREY, fg(250), GREY, SMOKE):
        sys.stdout.write("\r\033[K" +
                         center(ITAL + col + BYLINE + RESET))
        sys.stdout.flush()
        nap(0.28)
    print()

def finale():
    print()
    for i in range(7):
        style = BOLD + GOLD if i % 2 == 0 else DIM + SMOKE
        sys.stdout.write("\r\033[K" +
                         center(style + "fin.  ( probably )" + RESET))
        sys.stdout.flush()
        nap(0.4)
    print()
    nap(0.3)
    print(center(DIM + SMOKE +
                 "( please exit through the gift shop of existential dread )"
                 + RESET))
    print()

# --------------------------------------------------------------------- main --
def main():
    enable_ansi()
    hide_cursor()
    try:
        title_sequence()
        curtain_open()
        stage_scene()
        nervous_aside()
        quote_card()
        byline()
        finale()
    except KeyboardInterrupt:
        print("
" + center(DIM + SMOKE +
                            "( interrupted — how very fitting )" + RESET))
    finally:
        show_cursor()
        sys.stdout.write(RESET + "
")

if __name__ == "__main__":
    main()