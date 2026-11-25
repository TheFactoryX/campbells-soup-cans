"""
Campbell's Soup Can #5276
Produced: 2026-11-25 14:25:44
Worker: Thinking Machines: Inkling 2 Mini (thinkingmachines/inkling-2-mini)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🎬 WOODY ALLEN — EXISTENTIAL QUOTE MACHINE 🎞️
Prints ONE (1) Woody Allen-flavored philosophical quote,
typewritten inside a cinematic frame. Pure Python + ANSI.

Usage:  python3 woody_quote.py           (animated)
        python3 woody_quote.py --instant  (no animation)
"""

import argparse
import random
import sys
import time
import textwrap

# ────────────────────────── ANSI ────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
REVERSE = "\033[7m"
BLINK   = "\033[5m"

def fg(n): return f"\033[38;5;{n}m"

GOLD    = fg(220)   # deep gold
AMBER   = fg(208)
BUTTER  = fg(229)
CREAM   = fg(255)
WHITE   = fg(231)
SOFT    = fg(245)
PINK    = fg(213)
LILAC   = fg(183)
TEAL    = fg(43)
RED     = fg(196)
CURS    = fg(226)   # bright yellow cursor

ANIM = True

# ────────────────────────── Content ─────────────────────────────────
QUOTES = [
    "I don't want to be happy. I just want to spend enough time near happiness that it stops looking like a stranger.",
    "The problem with waiting is that waiting becomes a genre of your own existence.",
    "I've lived through every kind of day — and I still feel like the only one who doesn't understand any of them.",
    "If I had to choose a date to end it all, I'd pick a day with no appointments and a good glass of something.",
    "Being single is not a tragedy — it is an invitation to think about the future, but an uninvited one.",
    "I don't always know what I'm thinking. Fortunately, I'm always in the room where I'm thinking.",
    "Success feels like waiting for a phone that keeps ringing.",
    "My friends say I'm a good listener. That's kind — because I only really listen to my inner critic.",
    "If tomorrow never happens, I'd like to know that today felt like it.",
    "Some people chase fame. I chase the moment the audience stops looking at me.",
    "I have always been afraid of being left behind — until the day I find out nobody is watching me.",
    "Worried about what I spent my life doing? Everything — except the one thing I feel like I should have known how to be.",
    "A lot of people are looking for their lives. I'm not sure I'm looking for mine.",
    "I don't mind being unfinished. I just mind being looked at while I'm unfinished.",
]

# ────────────────────────── Helpers ─────────────────────────────────
def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def clear_screen():
    write("\033[2J\033[H")

def pause(t):
    if ANIM:
        time.sleep(t)

def center_str(text, width=62):
    pad = max(0, (width - len(text)) // 2)
    return " " * pad + text

# ────────────────────────── Animation bits ──────────────────────────
def marquee_title():
    title = "W O O D Y   A L L E N"
    sub   = "★  ★  ★   THE Q U O T E   E N G I N E   ★  ★  ★"
    if not ANIM:
        write("\n\n")
        write(center_str(sub, 62) + "\n")
        write(() if False else center_str(title, 62) + "\n")
        return
    write("\n\n" + GOLD + BOLD)
    for i in range(len(sub)):
        write(f"\r\033[2K{center_str(sub[:i+1], 62)}")
        time.sleep(0.05)
    write(f"\r\033[2K{center_str(sub, 62)}\n")
    time.sleep(0.25)
    # blinking subtitle line
    for _ in range(2):
        write(f"\r\033[2K{SOFT}{center_str('a one-man cinema · directed by a nervy man who thinks too loudly', 70)}{RESET}")
        write(f"\r\033[2K{SOFT}{center_str('a one-man cinema · directed by a nervy man who thinks too loudly', 70)}{RESET}")
        time.sleep(0.02)
    time.sleep(0.1)
    write(f"\r\033[2K{GOLD}{BOLD}{center_str(title, 62)}{RESET}\n")
    time.sleep(0.3)
    # shimmer underline
    for k in range(3):
        write(f"\n{center_str('━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━', 62)}")
        write(f"\n{BOLD}{PINK}")
        write(f"\r\033[2K{center_str('✦  one thought, a few for the price of true love  ✦', 62)}{RESET}")
        time.sleep(0.18)
    write("\n")

def synopsis():
    synopsis = "Here's a single, brave, self-aware anecdote about time, fear, and mild existential dread —"
    synopsis2 = "delivered by a man who rehearsed it on his way to his own interview with God."
    if not ANIM:
        write(f"\n{SOFT}{center_str(synopsis, 76)}{RESET}\n")
        write(f"{center_str(synopsis2, 76)}{RESET}\n\n")
        return
    write("\n")
    type_line(synopsis, SOFT, width=76, speed=0.022, cursor=False)
    write("\n")
    type_line(synopsis2, SOFT, width=76, speed=0.022, cursor=False)
    write("\n")

def type_line(text, color, width=62, speed=0.022, cursor=True):
    padded = center_str(text, width)
    if not ANIM:
        write(color + padded + RESET + "\n")
        return
    body = color + padded[:0] + RESET
    for i in range(len(padded)):
        body = color + padded[:i] + RESET
        cur = CURS + BLINK + "▌" + RESET if (cursor and padded[i:i+1] == " ") else ""
        cur = CURS + BLINK + "▌" + RESET if cursor else ""
        write(f"\r\033[2K{body}{cur}")
        time.sleep(speed)
    write(f"\r\033[2K{color}{padded}{RESET}\n")

def loading_bar():
    label = "Casting the shadows of the soul"
    width = 38
    total = 26 if ANIM else 1
    write("\n")
    for i in range(1, total + 1):
        pct = int(i / total * 100)
        filled = round(i / total * width)
        bar = fg(220) + "█" * filled + fg(245) + "░" * (width - filled) + RESET
        line = f"{label}...  {bar}  {pct:>3d}%"
        write(f"\r\033[2K{center_str(line, 78)}")
        pause(0.07 if ANIM else 0)
    write(f"\r\033[2K{center_str('▮ / ▮ / / ▮ / ▮   existential weariness loading complete  ▮ / ▮', 78)}{RESET}\n\n")
    pause(0.35)

def record_on():
    # recording dot pulse
    for _ in range(3):
        write(f"\r\033[2K{center_str('●  R E C', 62)}")
        pause(0.3 if ANIM else 0)
        write(f"\r\033[2K{center_str('   …', 62)}")
        pause(0.3 if ANIM else 0)
    write(f"\r\033[2K")

def build_frame(lines, inner=56):
    border_char = "─" if True else "─"
    width = inner + 4           # interior + padding both sides
    top = "╭" + border_char * (width - 2) + "╮"
    row = lambda t: "│ " + t.ljust(inner) + " │"
    return top, row, "╰" + border_char * (width - 2) + "╯", width

def padded_line(text, width=56):
    padded = center_str(text, width)
    return padded.ljust(width)

def quote_frame(quote_text):
    inner = 56
    lines = textwrap.wrap(quote_text, width=inner)
    lines = [l for l in lines] if lines else [quote_text]
    top, row, bottom, width = build_frame(lines, inner)

    if not ANIM:
        write(f"\n{GOLD}{top}{RESET}\n")
        for line in lines:
            write(f"{GOLD}│{RESET} {CREAM}{line.ljust(inner)}{RESET} {GOLD}│{RESET}\n")
        write(f"{GOLD}{bottom}{RESET}\n\n")
        write(f"{CENTER_BOLD('— W O O D Y   A L L E N —', 62)}{RESET}\n")
        return

    # draw the frame top & bottom up front
    write("\n" + GOLD + top + RESET + "\n")
    frame_lines = []
    for line in lines:
        padded = padded_line(line, inner)
        for i in range(len(padded)):
            shown = padded[:i]
            interior = " " + shown + CURS + BLINK + "▏" + RESET
            # base the frame on cols: "│ " + shown ... + " │"
            write(f"\r\033[2K{GOLD}│{RESET} {CREAM}{shown}{RESET}{CURS}{BLINK}▏{RESET}")
            time.sleep(0.018 if receivers_ok(padded[i]) else 0.03)
        write(f"\r\033[2K{GOLD}│{RESET} {CREAM}{padded}{RESET} {GOLD}│{RESET}\n")
        frame_lines.append(padded)
    write(GOLD + bottom + RESET + "\n\n")
    # separator
    write(f"{center_str('▓  ▓  ▓', 62)}\n\n")
    # signature typewriter
    sig = "—  W O O D Y   A L L E N  —"
    write("\n")
    type_line(sig, GOLD + BOLD, width=62, speed=0.045)
    write("\n")

def receivers_ok(ch):
    # non-space char → faster; space → slightly slower to let it breathe
    return ch != " "

def center_line(): pass

def CENTER_BOLD(text, width=62):
    pad = max(0, (width - len(text)) // 2)
    pad_str = center_str(text, width)
    return GOLD + BOLD + pad_str + RESET

def cut_and_end():
    # blinking CUT — red
    cut = "●  C U T .  ●"
    if ANIM:
        for _ in range(3):
            write(f"\r\033[2K{REVERSE}{center_str(cut, 62)}{RESET}")
            time.sleep(0.45)
            write(f"\r\033[2K")
            time.sleep(0.45)
    write(f"\r\033[2K{RED}{BOLD}{center_str(cut, 62)}{RESET}\n\n")
    # THE END, shimmering
    if ANIM:
        pad_line = center_str("T H E   E N D", 62)
        seq = [GOLD + BOLD, BUTTER + BOLD, AMBER + BOLD, WHITE + BOLD]
        for k in range(3):
            for c in seq:
                write(f"\r\033[2K{c}{pad_line}{RESET}")
                time.sleep(0.28)
        write(f"\r\033[2K{GOLD}{BOLD}{pad_line}{RESET}\n")
    else:
        write(f"{GOLD}{BOLD}{center_str('T H E   E N D', 62)}{RESET}\n")
    write("\n")

def fade_out():
    # quick fade gag: a dot column that pulses out
    if ANIM:
        write(f"\r\033[2K{SOFT}{center_str('⁙  ·  ···  ⁙  ·  ···  ⁙', 62)}{RESET}")
        for i in range(3):
            write(f"\r\033[2K{DIM}{center_str('⁙  ·  ···  ⁙  ·  ···  ⁙', 62)}{RESET}")
            time.sleep(0.18)
        write(f"\r\033[2K{DIM}{center_str('( THE  S O N G  F A D E S )', 70)}{RESET}\n")
        pause(0.3)

def footer():
    if ANIM: pause(0.2)
    write(f"\n{DIM}{center_str('this program is proud of itself.', 62)}{RESET}\n")
    write(f"{DIM}{center_str('the end · thanks for watching · I hope you laughed', 62)}{RESET}\n\n")

def main():
    parser = argparse.ArgumentParser(
        description="🎬 Print ONE (1) Woody Allen-flavored philosophical quote, typewritten in cinematic glory.")
    parser.add_argument("--instant", action="store_true",
                        help="Print the whole show at once, skipping animations")
    args = parser.parse_args()

    global ANIM
    ANIM = not args.instant and sys.stdout.isatty()

    try:
        clear_screen()
        marquee_title()
        synopsis()
        loading_bar()
        record_on()
        quote_frame(random.choice(QUOTES))
        cut_and_end()
        fade_out()
        footer()
    except KeyboardInterrupt:
        write("\n" + RESET)
        write("  (cut short — the philosopher is unimpressed)\n")
    finally:
        write(RESET)

if __name__ == "__main__":
    main()