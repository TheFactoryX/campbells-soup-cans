"""
Campbell's Soup Can #3898
Produced: 2026-06-09 18:20:37
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A single-file Python program that prints a Woody Allen style philosophical quote
with colorful ASCII-art, typing animation, and ANSI visuals — pure Python, no deps."""

import time, sys, random

# ── ANSI helpers ──────────────────────────────────────────────────────
ESC = "\033["
def rgb(r, g, b):
    return f"{ESC}38;2;{r};{g};{b}m"

def rgb_bg(r, g, b):
    return f"{ESC}48;2;{r};{g};{b}m"

BOLD  = f"{ESC}1m"
DIM   = f"{ESC}2m"
ITAL  = f"{ESC}3m"
BLINK = f"{ESC}5m"
RESET = f"{ESC}0m"

# ── the quote ────────────────────────────────────────────────────────
QUOTE = (
    '"The only time my brain stops overthinking\n'
    " is when it's contemplating the void —\n"
    ' and even then, it schedules a follow-up appointment."'
)

ATTRIBUTION = "— Woody Allen"

# ── helpers for animation ────────────────────────────────────────────
def flush_print(s, delay=0.02, **kwargs):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    kwargs.pop("end", None)
    print(**kwargs)

def clear_screen():
    sys.stdout.write(f"{ESC}2J{ESC}H")
    sys.stdout.flush()

# ── scene 1: city-skyline intro with twinkling stars ────────────────
def stars_scene():
    H, W = 19, 78
    skyline = [
        "                                                            *           ",
        "         *                        *                                           ",
        "                           *                                                  ",
        "                  *                *                                          ",
        "·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ",
        "                                          ___                                 ",
        "                          ___[_]__/\\____|_|__                                 ",
        "          _IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII                           ",
        "|  []  | [==] [==] [==] [==] [==] [==] [==] [==] |  ___    []  _  []        ",
        "|      | [==] [==] [==] [==] [==] [==] [==] [==] | | + |      | |           ",
        "|      | [==] [==] [==] [==] [==] [==] [==] [==] | |___|  []  | |  []       ",
        "|_[]___|_[==]_[==]_[==]_[==]_[==]_[==]_[==]_[==]_|_______[]__| |__[]_______  ",
        "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||",
    ]
    lamps = set()
    star_chars = list(range(H))
    random.shuffle(star_chars)
    for frame in range(6):
        rows = [[" "]*W for _ in range(H)]
        colors = []*H
        lamp_rows = [7, 8, 9, 10]
        for ci, line in enumerate(skyline):
            for cj, ch in enumerate(line.ljust(W)):
                rows[ci][cj] = ch
        # twinkle some stars
        for i, r in enumerate(star_chars):
            if frame % 2 == i % 2 and r < 5:
                c = random.randint(0, W-1)
                if rows[r][c] == " ":
                    rows[r][c] = "✦"
        if frame == 4:
            # light a streetlamp
            for lr in lamp_rows:
                rows[lr][20] = "☀"
                rows[lr][21] = ""  # keep space
        out_lines = []
        out_lines.append(f"{BOLD}{rgb(80,80,255)}")
        out_lines.append(f"{rgb(10,10,30)}┌{'─'*78}┐{RESET}")
        for r in range(H):
            segment = "".join(rows[r])
            col_ch = rgb(180, 180, 255) if r < 5 else rgb(60,60,90) if r < 6 else rgb(130,110,80)
            out_lines.append(f"{rgb(10,10,30)}│{RESET}{col_ch}{segment}{RESET}{rgb(10,10,30)}│{RESET}")
        out_lines.append(f"{rgb(10,10,30)}└{'─'*78}┘{RESET}")

        # footer in italic yellow
        out_lines.append(f"{ITAL}{rgb(200,180,60)}   [ NYC Jazz Scene — saxophone plays somewhere in the distance ]{RESET}")

        sys.stdout.write("\n".join(out_lines) + "\n")
        sys.stdout.flush()
        time.sleep(0.6)
        clear_screen()

def build_quote_box():
    lines = QUOTE.split("\n")
    max_len = max(l.rstrip().__len__() for l in lines)
    max_len = max(max_len, len(ATTRIBUTION))
    width = max_len + 6
    border = "═" * width
    rows = []
    rows.append(f"{BOLD}{rgb(255,215,0)}╔{border}╗{RESET}")
    rows.append(f"{rgb(255,215,0)}║{RESET}{DIM}···{RESET}{' '* (width-3)}{RESET}{rgb(255,215,0)}║{RESET}")
    for line in lines:
        pad = " " * (width - len(line.rstrip()))
        rows.append(f"{rgb(255,215,0)}║{RESET}  {rgb(220,220,255)}{BOLD}{line}{RESET}{pad}{rgb(255,215,0)}║{RESET}")
    # attribution
    att_pad = " " * (width - len(ATTRIBUTION) - 2)
    rows.append(f"{rgb(255,215,0)}║{RESET}{rgb(220,220,255)}  {ITAL}{ATTRIBUTION}{RESET}{att_pad}{rgb(255,215,0)} ║{RESET}")
    rows.append(f"{rgb(255,215,0)}║{RESET}{DIM}···{RESET}{' '* (width-3)}{RESET}{rgb(255,215,0)}║{RESET}")
    rows.append(f"{rgb(255,215,0)}╚{border}╝{RESET}")
    return rows

def crawl_line(results, msg, n=30):
    line = "·" * n
    out = " ".join(results) + line + msg
    print(out, end="\r")
    sys.stdout.flush()

def title_screen():
    flush_print(f"\n{BOLD}{rgb(255,255,0)}  ▐▐▐ ▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐{RESET}", delay=0.004)
    sys.stdout.write("\n")
    time.sleep(0.3)
    sys.stdout.write("        ")
    flush_print(f"{BOLD}{ITAL}{rgb(255,200,80)}☕ philosophical nibbles ☕{RESET}", delay=0.03)
    time.sleep(0.4)
    sys.stdout.write("\n")

def main():
    clear_screen()
    title_screen()
    stars_scene()
    clear_screen()
    # ── scene 2: the typewriter reveal ──────────────────────────────────────
    sys.stdout.write("\n")
    # book opening animation
    stages = (5, 13, 35, 56)
    max_idx = max(stages)
    for i in range(max_idx):
        sys.stdout.write(f"\r    {rgb(220,210,160)}📖")
        if i in stages:
            sys.stdout.write(f"  {rgb(180,150,80)}Page {stages.index(i)+1}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write(f"\n    {rgb(220,210,160)}📖  ✓  (enough reading time)\n")
    time.sleep(1)

    rows = build_quote_box()
    indent = "        "
    # opening the book lines
    for lin in rows:
        print(INDENT + lin)
        time.sleep(0.13)
    sys.stdout.write("\n")
    time.sleep(1.2)

    # crawl bar
    verbs = ("dread  ", "regret  ", "analyze    ")
    results = []
    for phrase in verbs:
        crawl_line(results, phrase)
        time.sleep(2)
        results.append(phrase)
        sys.stdout.write("\n")
        time.sleep(0.5)

    crawl_line(results, "      ", n=0)  # clean
    sys.stdout.write("\n")
    time.sleep(0.6)

    # ── scene 3: exit message ──────────────────────────────────────────
    exit_line = (
        f"\n{ITAL}{rgb(120,120,120)}"
        f"  But seriously: don't worry, nobody else is reading this — even my shrink left a VM.\n"
        f"{RESET}"
    )
    flush_print(exit_line, delay=0.025)
    sys.stdout.write("\n")
    time.sleep(0.4)
    flush_print(f"   {rgb(130,210,130)}Press Enter to face reality...{RESET}", delay=0.04)
    input()
    sys.stdout.write(f"\n   {rgb(200,60,60)}Fatal error in consciousness.sys: `reality not found`\n")
    time.sleep(1.2)

INDENT = "        "
clear_screen()
title_screen()
stars_scene()
clear_screen()
sys.stdout.write("\n")
# ── scene 2: the typewriter reveal ──────────────────────────────────────
sys.stdout.write("\n")
# book opening animation
stages = (5, 13, 35, 56)
max_idx = max(stages)
for i in range(max_idx):
    sys.stdout.write(f"\r    {rgb(220,210,160)}📖")
    if i in stages:
        sys.stdout.write(f"  {rgb(180,150,80)}Page {stages.index(i)+1}{RESET}")
    sys.stdout.flush()
    time.sleep(0.15)
sys.stdout.write(f"\n    {rgb(220,210,160)}📖  ✓  (enough reading time)\n")
time.sleep(1)

rows = build_quote_box()
indent = "        "
# opening the book lines
for lin in rows:
    print(indent + lin)
    time.sleep(0.13)
sys.stdout.write("\n")
time.sleep(1.2)

# crawl bar
verbs = ("dread  ", "regret  ", "analyze    ")
results = []
for phrase in verbs:
    crawl_line(results, phrase, n=10)
    time.sleep(0.6)
    results.append(phrase)
    sys.stdout.write("\n")
    time.sleep(0.3)
    sys.stdout.flush()
crawl_line(results, "      ", n=0)
sys.stdout.write("\n")
time.sleep(0.6)

# ── scene 3: exit message ──────────────────────────────────────────
exit_line = (
    f"\n{ITAL}{rgb(120,120,120)}"
    f"  But seriously: don't worry, nobody else is reading this — even my shrink left a VM.\n"
    f"{RESET}"
)
flush_print(exit_line, delay=0.025)
sys.stdout.write("\n")
time.sleep(0.4)
flush_print(f"   {rgb(130,210,130)}Press Enter to face reality...{RESET}", delay=0.04)
try:
    input()
except EOFError:
    pass
sys.stdout.write(f"\n   {rgb(200,60,60)}Fatal error in consciousness.sys: `reality not found`\n")
time.sleep(2)