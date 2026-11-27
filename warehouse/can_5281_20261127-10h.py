"""
Campbell's Soup Can #5281
Produced: 2026-11-27 10:52:34
Worker: Baidu: ERNIE-5.5-Flash-Preview (free) (baidu/ernie-5.5-flash-preview:free)
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
THE WRONG SOUP
==============
A short, neurotic animation about the only philosophical conclusion that
thirty-three years of analysis can actually buy you.

Pure standard library.  No dependencies.  Just ANSI escape codes and dread.

    python3 the_wrong_soup.py
"""

import math
import os
import random
import shutil
import sys
import time

# ---------------------------------------------------------------------------
# 0.  Can we be pretty tonight?
# ---------------------------------------------------------------------------

COLOR = True
if os.environ.get("NO_COLOR") or os.environ.get("TERM", "").strip().lower() in ("", "dumb"):
    COLOR = False


def _enc():
    return getattr(sys.stdout, "encoding", None) or "ascii"


try:
    "─│╭╮╰╯✦·—▌".encode(_enc())
    FANCY = True
except Exception:
    FANCY = False

_PLAIN = {"─": "-", "│": "|", "╭": "+", "╮": "+", "╰": "+", "╯": "+",
          "✦": "*", "·": ".", "—": "-", "▌": "|"}


def g(ch):
    """Return the pretty glyph, or a shy ASCII stand-in."""
    return ch if FANCY else _PLAIN.get(ch, ch)


def T(s):
    return "".join(g(c) for c in s)


RESET = "\033[0m" if COLOR else ""


def fg(n):
    return "\033[38;5;%dm" % n if COLOR else ""


# ---------------------------------------------------------------------------
# 1.  Palette & stage dimensions
# ---------------------------------------------------------------------------

GOLD  = 221   # the warm, anxious light of a therapist's office
ROSE  = 211
AQUA  = 45
FRAME = 62
MUTED = 245
INK   = 250

W, H  = 74, 26
FPS   = 30

BOX_X, BOX_W = 4, 66
BOX_TOP, BOX_BOT = 17, 22
INNER_W = BOX_W - 2
TITLE_Y, SIG_Y = 15, 24

# ---------------------------------------------------------------------------
# 2.  The quote (one quote, as requested, in a Woody Allen-ish key)
# ---------------------------------------------------------------------------

QUOTE_RUNS = [
    ("After thirty-three years of analysis, I've reached only this: ", GOLD),
    ("the universe is ", GOLD),
    ("indifferent", ROSE),
    (", meaning is a ", GOLD),
    ("rumor", AQUA),
    (", and the one thing I truly understand is that the waiter brought the ", GOLD),
    ("wrong soup", ROSE),
    (" \u2014 and I said it was ", GOLD),
    ("fine", AQUA),
    (".", GOLD),
]


def wrap_cells(cells, width):
    """Greedy word-wrap that preserves per-character colour."""
    lines, cur = [], []
    for ch, col in cells:
        if len(cur) >= width:
            cut = -1
            for i in range(len(cur) - 1, -1, -1):
                if cur[i][0] == " ":
                    cut = i
                    break
            if cut > 0:
                lines.append(cur[:cut])
                cur = cur[cut + 1:]
            else:
                lines.append(cur)
                cur = []
        if ch == " " and not cur:
            continue
        cur.append((ch, col))
    if cur:
        lines.append(cur)
    return lines


CELLS = []
for _text, _col in QUOTE_RUNS:
    for _ch in T(_text):
        CELLS.append((_ch, _col))

QLINES = wrap_cells(CELLS, INNER_W)
TYPED_TOTAL = sum(len(l) for l in QLINES)


def cursor_pos(k):
    acc = 0
    for li, line in enumerate(QLINES):
        if k <= acc + len(line):
            return li, k - acc
        acc += len(line)
    return len(QLINES) - 1, len(QLINES[-1])


# ---------------------------------------------------------------------------
# 3.  The little man
# ---------------------------------------------------------------------------

FIGURE = [
    '      .-""""""-.',
    '     /  _    _  \\',
    '    |  (o)  (o) |',
    '    |     ^     |',
    '     \\  \\___/  /',
    "      '-------'",
    '       /|   |\\',
    '      / |   | \\',
    '        |   |',
    '        |   |',
    '      _|   |_',
    '     (___   ___)',
    "       '--'",
]
FIG_W = max(len(l) for l in FIGURE)
FIGURE = [l.ljust(FIG_W) for l in FIGURE]
FIG_TOP = 2
FIG_X = (W - FIG_W) // 2
FIG_CX = FIG_X + FIG_W // 2
FIG_CY = FIG_TOP + 1

# ---------------------------------------------------------------------------
# 4.  Starfield
# ---------------------------------------------------------------------------

_rng = random.Random(11)
STARS = []
for _ in range(95):
    STARS.append((
        _rng.randrange(W),
        _rng.randrange(H),
        _rng.choice([238, 239, 240, 242, 245, 250]),
        _rng.choice([0, 0, 4, 7]),
        _rng.uniform(0.05, 0.16),
        _rng.uniform(0.0, math.tau),
        _rng.randrange(0, 20),
        _rng.random() < 0.08,
    ))

# ---------------------------------------------------------------------------
# 5.  Timing (in frames, 30 fps)
# ---------------------------------------------------------------------------

T_STAR_END = 20
T_FIG0     = 22
T_FIG_STEP = 2
T_TITLE    = 52
T_BOX0     = 56
T_SWEEP    = 16
T_TYPE0    = T_BOX0 + T_SWEEP + 2
CHARS_PER_FRAME = 2.0
T_TYPE1    = T_TYPE0 + int(TYPED_TOTAL / CHARS_PER_FRAME) + 1
T_BOT0     = T_TYPE1 + 8
T_BOT1     = T_BOT0 + T_SWEEP
T_SIG      = T_BOT1 + 10
T_END      = T_SIG + 87

# ---------------------------------------------------------------------------
# 6.  Painting
# ---------------------------------------------------------------------------


def blank():
    return [[(" ", None) for _ in range(W)] for _ in range(H)]


def put(grid, x, y, text, col=None):
    if 0 <= y < H:
        row = grid[y]
        for i, ch in enumerate(text):
            xx = x + i
            if 0 <= xx < W:
                row[xx] = (ch, col)


def build_frame(f):
    grid = blank()

    # --- stars ------------------------------------------------------------
    for sx, sy, base, amp, spd, ph, app, big in STARS:
        if f < app:
            continue
        age = f - app
        col = base + int(amp * math.sin(f * spd + ph))
        if age < 10:
            col = int(232 + (col - 232) * (age / 10.0))
        col = max(232, min(255, col))
        put(grid, sx, sy, g("✦") if big else g("·"), col)

    # --- the man, revealed from the hat down -------------------------------
    fig_rows = max(0, min(len(FIGURE), (f - T_FIG0) // T_FIG_STEP + 1))
    if fig_rows > 0:
        x0 = FIG_X + (1 if (f % 53) in (0, 1) else 0)   # an involuntary shiver
        for i in range(fig_rows):
            put(grid, x0, FIG_TOP + i, FIGURE[i], INK)

    # --- the worry, orbiting his head --------------------------------------
    if f >= T_FIG0:
        ang = f * 0.12
        ox = int(round(FIG_CX + 11 * math.cos(ang)))
        oy = int(round(FIG_CY + 2.6 * math.sin(ang)))
        if 0 <= oy < H and 0 <= ox < W and grid[oy][ox][0] == " ":
            put(grid, ox, oy, g("✦"), GOLD if (f // 7) % 2 == 0 else ROSE)

    # --- title --------------------------------------------------------------
    if f >= T_TITLE:
        title = T("·   a rumination, unlicensed and unpaid   ·")
        put(grid, (W - len(title)) // 2, TITLE_Y, title, MUTED)

    # --- the box ------------------------------------------------------------
    if f >= T_BOX0:
        p = min(1.0, (f - T_BOX0) / float(T_SWEEP))

        if p >= 1.0:                                   # sides + empty interior
            for y in range(BOX_TOP + 1, BOX_BOT):
                for x in range(BOX_X + 1, BOX_X + BOX_W - 1):
                    grid[y][x] = (" ", None)
                put(grid, BOX_X, y, g("│"), FRAME)
                put(grid, BOX_X + BOX_W - 1, y, g("│"), FRAME)

        n = int(round(p * INNER_W))                    # top edge, left → right
        put(grid, BOX_X, BOX_TOP, g("╭"), FRAME)
        for i in range(n):
            put(grid, BOX_X + 1 + i, BOX_TOP, g("─"), FRAME)
        if p >= 1.0:
            put(grid, BOX_X + BOX_W - 1, BOX_TOP, g("╮"), FRAME)

        if f >= T_BOT0:                                # bottom edge, right → left
            q = min(1.0, (f - T_BOT0) / float(T_SWEEP))
            m = int(round(q * INNER_W))
            if q > 0:
                put(grid, BOX_X + BOX_W - 1, BOX_BOT, g("╯"), FRAME)
            for i in range(m):
                put(grid, BOX_X + BOX_W - 2 - i, BOX_BOT, g("─"), FRAME)
            if q >= 1.0:
                put(grid, BOX_X, BOX_BOT, g("╰"), FRAME)

    # --- the quote, typed out ----------------------------------------------
    if f >= T_TYPE0:
        k = min(TYPED_TOTAL, int((f - T_TYPE0) * CHARS_PER_FRAME))
        acc = 0
        for li, line in enumerate(QLINES):
            take = max(0, min(len(line), k - acc))
            for i in range(take):
                ch, col = line[i]
                put(grid, BOX_X + 1 + i, BOX_TOP + 1 + li, ch, col)
            acc += len(line)

        if f < T_SIG + 60:
            li, off = cursor_pos(k)
            if off >= INNER_W:
                li, off = li + 1, 0
            if li < len(QLINES):
                visible = (k < TYPED_TOTAL) or ((f // 8) % 2 == 0)
                if visible:
                    put(grid, BOX_X + 1 + off, BOX_TOP + 1 + li, g("▌"), GOLD)

    # --- the citation nobody asked for --------------------------------------
    if f >= T_SIG:
        sig = T("— overheard on the Upper East Side, at 3 a.m.")
        put(grid, (W - len(sig)) // 2, SIG_Y, sig, MUTED)

    return grid


# ---------------------------------------------------------------------------
# 7.  Rendering
# ---------------------------------------------------------------------------


def render(grid, home=True, clear=True):
    out = ["\x1b[H"] if home else []
    for y in range(H):
        row = grid[y]
        last = -1
        for x in range(W - 1, -1, -1):
            if row[x][0] != " ":
                last = x
                break
        if clear:
            out.append("\x1b[2K")
        cur = "\x00"
        for x in range(last + 1):
            ch, col = row[x]
            if col != cur:
                out.append(fg(col) if col is not None else RESET)
                cur = col
            out.append(ch)
        out.append(RESET)
        if y != H - 1:
            out.append("\r\n")
    return "".join(out)


# ---------------------------------------------------------------------------
# 8.  Showtime
# ---------------------------------------------------------------------------


def play():
    home = clear = COLOR
    sys.stdout.write(("\x1b[?25l" if home else "") + ("\x1b[2J" if clear else ""))
    sys.stdout.flush()
    try:
        for f in range(T_END + 1):
            sys.stdout.write(render(build_frame(f), home=home, clear=clear))
            sys.stdout.flush()
            time.sleep(1.0 / FPS)
    except KeyboardInterrupt:
        pass
    finally:
        if home:
            sys.stdout.write("\x1b[?25h")
            sys.stdout.flush()


def show_final():
    """For pipes, logs and other joyless places: one finished frame."""
    sys.stdout.write(render(build_frame(T_END), home=False, clear=False))
    sys.stdout.write("\n")


def main():
    interactive = False
    try:
        interactive = sys.stdout.isatty()
    except Exception:
        interactive = False

    if interactive:
        try:
            size = shutil.get_terminal_size((100, 30))
        except Exception:
            size = None
        if size and size.columns >= W + 1 and size.lines >= H:
            play()
            return

    show_final()


if __name__ == "__main__":
    main()