"""
Campbell's Soup Can #4926
Produced: 2026-09-08 18:41:12
Worker: Nex AGI: Nex-N2.5-Pro (free) (nex-agi/nex-n2.5-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A BRIEF EXISTENTIAL PAUSE
~~~~~~~~~~~~~~~~~~~~~~~~~
A single nervous little quote, delivered with:
  - one flatlining heartbeat
  - one anxious spark of a soul
  - one flickering neon frame
  - far too much thought

Pure Python. No dependencies. Much like the quote, it is
self-contained and slightly worried about it.
"""

import sys
import time
import random
import shutil

# ------------------------------ ANSI ------------------------------
ESC = "\033["
RESET = ESC + "0m"

def C(*codes):
    """Build an ANSI SGR sequence, e.g. C(1, 95) = bold magenta."""
    return ESC + ";".join(map(str, codes)) + "m"

BOLD, DIM, ITALIC = C(1), C(2), C(3)
HIDE_CURSOR = ESC + "?25l"
SHOW_CURSOR = ESC + "?25h"
CLEAR_SCREEN = ESC + "2J" + ESC + "H"

def paint(text, *codes):
    return C(*codes) + text + RESET

def vlen(text):
    """Visible width of a string that may contain ANSI escape sequences."""
    width, i = 0, 0
    while i < len(text):
        if text[i] == "\033":
            end = text.find("m", i + 1)
            i = len(text) if end == -1 else end + 1
        else:
            width += 1
            i += 1
    return width

def center(text, width):
    return " " * max(0, (width - vlen(text)) // 2) + text

def put(text=""):
    sys.stdout.write(text)
    sys.stdout.flush()

def goto(row, col):
    put(ESC + f"{row};{col}H")

# ----------------------------- The Quote -----------------------------
# Exactly one. Neurotic, self-deprecating, existential.
QUOTE_LINES = [
    '"I\'ve made peace with my mortality —',
    " we nod in the hallway now. It's the",
    " healthiest relationship I\'ve ever had.\"",
]

NEON = [92, 93, 94, 95, 96, 91]   # green, yellow, blue, magenta, cyan, red
LINE_COLORS = [96, 95, 93]        # cyan, magenta, gold (the settled glow)

TITLE = "E X I S T E N T I A L   M A I N T E N A N C E"
FOOTER = "·:· ( this has been your scheduled existential pause ) ·:·"

def box_drawing_available():
    try:
        "╔═╗║╚╝".encode(sys.stdout.encoding or "utf-8")
        return True
    except Exception:
        return False

def main():
    term = shutil.get_terminal_size(fallback=(90, 26))
    W = max(44, min(term.columns, 110))
    H = term.rows

    base = max(1, (H - 15) // 2)

    TITLE_ROW  = base + 0
    FRAME_TOP  = base + 3
    EKG_ROW    = base + 11
    FOOTER_ROW = base + 13

    put(CLEAR_SCREEN + HIDE_CURSOR)
    time.sleep(0.35)

    if box_drawing_available():
        TL, HBAR, TR = "╔", "═", "╗"
        VBAR, BL, BR = "║", "╚", "╝"
    else:
        TL, HBAR, TR = "+", "-", "+"
        VBAR, BL, BR = "|", "+", "+"

    # ---- frame geometry ----
    inner_width = max(vlen(line) for line in QUOTE_LINES)
    box_width = inner_width + 4
    frame_left = max(1, (W - box_width) // 2 + 1)

    top = TL + HBAR * (box_width - 2) + TR
    mid = VBAR + " " * (box_width - 2) + VBAR
    bot = BL + HBAR * (box_width - 2) + BR

    frame_rows = [
        (FRAME_TOP,     top),
        (FRAME_TOP + 1, mid),
        (FRAME_TOP + 2, mid),
        (FRAME_TOP + 3, mid),
        (FRAME_TOP + 4, mid),
        (FRAME_TOP + 5, mid),
        (FRAME_TOP + 6, bot),
    ]

    frame_cells = []
    for r, line in frame_rows:
        for idx, ch in enumerate(line):
            frame_cells.append((r, frame_left + idx, ch, 95 if ch == VBAR else 96))

    def draw_frame(extra=()):
        for r, col, ch, code in frame_cells:
            goto(r, col)
            put(paint(ch, code, *extra))

    # ---- background stars (kept far away from all text, like us) ----
    protected_rows = (
        {TITLE_ROW, EKG_ROW, EKG_ROW - 1, FOOTER_ROW}
        | set(range(FRAME_TOP, FRAME_TOP + 7))
    )
    star_rows = [r for r in range(1, H + 1) if r not in protected_rows]
    stars = []
    if star_rows:
        used = set()
        for _ in range(min(16, max(4, len(star_rows) * 5))):
            for _ in range(60):
                r = random.choice(star_rows)
                c = random.randint(1, max(1, W))
                if (r, c) not in used:
                    used.add((r, c))
                    stars.append({
                        "r": r, "c": c,
                        "sym": random.choice(["·", "·", "*", "✦"]),
                        "code": random.choice([37, 90, 94, 95, 96]),
                        "on": False,
                    })
                    break

    def draw_star(s):
        goto(s["r"], s["c"])
        put(paint(s["sym"], 2, s["code"]))

    def erase_star(s):
        goto(s["r"], s["c"])
        put(" ")

    def twinkle(n=2):
        for _ in range(n):
            if not stars:
                return
            s = random.choice(stars)
            if s["on"]:
                erase_star(s)
                s["on"] = False
            else:
                draw_star(s)
                s["on"] = True

    for s in stars:
        if random.random() < 0.7:
            draw_star(s)
            s["on"] = True

    # ---- title ----
    goto(TITLE_ROW, 1)
    put(center(paint(TITLE, 2, 33, 3), W))
    time.sleep(0.5)
    twinkle(3)

    # ---- heartbeat ----
    def build_ekg(width):
        chars = ["_"] * width
        p = 3
        while p + 4 < width:
            chars[p:p + 4] = list("/\\/\\")
            p += random.randint(8, 12)
        return "".join(chars)

    ekg_width = min(44, max(24, W - 10))
    ekg = build_ekg(ekg_width)
    ekg_col = max(1, (W - ekg_width) // 2 + 1)

    def draw_ekg(line, dot=None, codes=(2, 92)):
        if dot is None:
            out = line
        else:
            out = line[:dot] + "●" + line[dot + 1:]
        goto(EKG_ROW, ekg_col)
        put(paint(out, *codes))

    draw_ekg(ekg)
    time.sleep(0.4)

    for _sweep in range(2):
        for i in range(ekg_width):
            draw_ekg(ekg, i)
            if random.random() < 0.25:
                twinkle(1)
            time.sleep(0.038 + random.random() * 0.02)
        time.sleep(0.18)

    # ...and then, inevitably, the flatline
    flat = "_" * ekg_width
    draw_ekg(flat, ekg_width - 1, (1, 92))
    time.sleep(0.12)
    draw_ekg(flat, ekg_width - 4, (1, 37))
    time.sleep(0.12)
    draw_ekg(flat, ekg_width - 1, (2, 37))
    time.sleep(0.12)
    draw_ekg(flat, codes=(2, 37))
    time.sleep(0.9)
    twinkle(3)

    # ---- one small spark, pacing anxiously beneath the frame ----
    spark_r, spark_c = EKG_ROW, ekg_col + ekg_width - 1
    steps = 12
    drift = 0
    path = []
    for i in range(steps + 1):
        drift += random.choice([-2, -1, -1, 0, 0])   # a leftward, worried drift
        drift = max(-14, min(2, drift))
        r = spark_r - round(1 * i / steps)
        path.append((r, spark_c + drift))

    prev = None
    for r, c in path:
        if prev:
            goto(prev[0], prev[1])
            put("_" if prev[0] == EKG_ROW else " ")
        goto(r, c)
        put(paint("•", 1, 96))
        prev = (r, c)
        if random.random() < 0.4:
            twinkle(1)
        time.sleep(0.085)

    for on in range(4):
        goto(prev[0], prev[1])
        put(paint("•", 1, 96) if on % 2 == 0 else " ")
        time.sleep(0.09)
    goto(prev[0], prev[1])
    put(" ")
    time.sleep(0.15)

    # ---- the neon frame ignites ----
    draw_frame((1, 97))          # white-hot flash
    time.sleep(0.12)
    draw_frame()
    for _ in range(46):          # the inevitable buzzing
        r, col, ch, code = random.choice(frame_cells)
        goto(r, col)
        put(" ")
        time.sleep(random.uniform(0.015, 0.055))
        goto(r, col)
        put(paint(ch, code))
        if random.random() < 0.06:
            draw_frame((1,))
            time.sleep(0.05)
            draw_frame()

    # ---- the quote, typed by a nervous intern ----
    text_col = frame_left + 2
    quote_rows = [FRAME_TOP + 2, FRAME_TOP + 3, FRAME_TOP + 4]
    color_idx = 0

    for line, row in zip(QUOTE_LINES, quote_rows):
        goto(row, text_col)
        for i, ch in enumerate(line):
            code = NEON[color_idx % len(NEON)]
            color_idx += 1
            pos = text_col + i
            put(paint(ch, code))
            # sometimes a letter briefly questions its own existence
            if random.random() < 0.045:
                time.sleep(0.03)
                goto(row, pos)
                put(" ")
                time.sleep(0.04 + random.random() * 0.05)
                goto(row, pos)
                put(paint(ch, code))
            if ch == " ":
                delay = 0.012
            elif ch in ".,—;:":
                delay = 0.15
            else:
                delay = 0.034
            time.sleep(delay * random.uniform(0.6, 1.5))
        time.sleep(0.3)

    # ---- blinking block cursor, having second thoughts ----
    last_row = quote_rows[-1]
    end_col = text_col + vlen(QUOTE_LINES[-1])
    last_code = NEON[(color_idx - 1) % len(NEON)]
    for i in range(6):
        goto(last_row, end_col)
        put(paint("█", 1, last_code) if i % 2 == 0 else " ")
        time.sleep(0.14)
    goto(last_row, end_col)
    put(" ")

    # ---- settle into a steady glow ----
    for line, row, code in zip(QUOTE_LINES, quote_rows, LINE_COLORS):
        goto(row, text_col)
        put(paint(line, code))
    time.sleep(0.3)

    for pulse in range(3):
        for line, row, code in zip(QUOTE_LINES, quote_rows, LINE_COLORS):
            goto(row, text_col)
            put(paint(line, 1, code) if pulse % 2 == 0 else paint(line, code))
        twinkle(2)
        time.sleep(0.22)

    # ---- footer ----
    goto(FOOTER_ROW, 1)
    put(center(paint(FOOTER, 2, 37, 3), W))
    for _ in range(4):
        twinkle(3)
        time.sleep(0.3)
    time.sleep(0.8)

    put("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        put("\n")
    finally:
        put(SHOW_CURSOR + RESET)