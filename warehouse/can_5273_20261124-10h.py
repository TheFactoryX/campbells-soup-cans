"""
Campbell's Soup Can #5273
Produced: 2026-11-24 10:55:52
Worker: Meta: Muse Spark Open (meta/muse-spark-open)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random
import shutil
import textwrap
import os

# ── ANSI ─────────────────────────────────────────────────────
R = "\033[0m"
B = "\033[1m"
D = "\033[2m"
I = "\033[3m"
U = "\033[4m"

# 256 color helpers
def c256(n): return f"\033[38;5;{n}m"
def bg256(n): return f"\033[48;5;{n}m"

CREAM = c256(230)
BEIGE = c256(222)
GOLD = c256(178)
MUSTARD = c256(136)
BROWN = c256(94)
GLASSES = c256(245)
SKIN = c256(216)
RED = c256(167)
TEAL = c256(30)
MUTED = c256(246)
PINK = c256(175)

HIDE = "\033[?25l"
SHOW = "\033[?25h"

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def sleep(t):
    time.sleep(t)

def typewriter(text, delay=0.025, color=""):
    for ch in text:
        sys.stdout.write(color + ch + R)
        sys.stdout.flush()
        if ch not in " \n":
            time.sleep(delay + random.uniform(0, 0.012))
        else:
            time.sleep(delay * 0.3)
    sys.stdout.write("\n")

def strip_ansi(s):
    import re
    return re.sub(r'\x1b\[[0-9;]*m', '', s)

def center_block(lines, width=None):
    if width is None:
        width = shutil.get_terminal_size().columns
    out = []
    for l in lines:
        vis = len(strip_ansi(l))
        pad = max(0, (width - vis)//2)
        out.append(" " * pad + l)
    return out

# ── Woody Allen style original quotes ──────────────────────
QUOTES = [
    "I told eternity I'd call it back later — now it won't stop leaving me existential voicemails.",
    "If the universe is expanding, why do I still feel trapped in my own head with no legroom?",
    "I don't mind the meaning of life being meaningless, I just wish it came with better punchlines.",
    "My therapist says to embrace the void. I did — and now the void wants me to meet its parents.",
    "I wanted immortality through not dying, but my hypochondria wants me to die just to prove it was right.",
    "Life is divided into the horrible and the miserable. I accidentally RSVP'd 'yes' to both.",
    "I asked God for a sign He exists. He sent me my tax audit — I'm still interpreting it.",
    "Consciousness is just stardust having a panic attack while trying to pay rent in Manhattan.",
]

quote = random.choice(QUOTES)
attribution = "— Woody Allen (ish)"

# ── Art pieces ─────────────────────────────────────────────
FACE = [
    f"{MUTED}                 . - - - - - .{R}",
    f"{MUTED}             .'{R} {CREAM}.- - - - - -.  {R}{MUTED}'{R}",
    f"{MUTED}           /{R} {BROWN}/{R}  {GLASSES}.- - - -.  {R}{BROWN}\\{R} {MUTED}\\{R}",
    f"{MUTED}          |{R} {BROWN}|{R} {GLASSES}/{R} {B}o{R}   {B}o{R} {GLASSES}\\{R} {BROWN}|{R} {MUTED}|{R}",
    f"{MUTED}          |{R} {BROWN}|{R} {GLASSES}|{R}    {MUTED}^{R}    {GLASSES}|{R} {BROWN}|{R} {MUTED}|{R}  {D}{MUTED}my glasses are{R}",
    f"{MUTED}          |{R} {BROWN}|{R} {GLASSES}|{R}    {PINK}_{D}{MUTED}—{R}    {GLASSES}|{R} {BROWN}|{R} {MUTED}|{R} {D}{MUTED}thicker than my{R}",
    f"{MUTED}           \\{R} {BROWN}\\{R}  {GLASSES}' -  - - '{R}  {BROWN}/{R} {MUTED}/{R}  {D}{MUTED}philosophy{R}",
    f"{MUTED}            '.{R}  {CREAM}' - .___. - '{R}  {MUTED}.'{R}",
    f"{MUTED}               ' - - - - - '{R}  {D}{CREAM}existential sigh™{R}",
]

SKYLINE = f"{D}{c256(240)}  ▁▂▃ {c256(242)}▅▅ {c256(240)}▃▅▇▅▆▅▃▂▁  {c256(242)}▂▅▇█▇▅▂  {c256(240)}▁▂▃▅▆▅▃▁     Manhattan (allegedly){R}"

def marquee_frame(tick, width=70):
    bulbs = ["●", "○"]
    line = ""
    for i in range(width):
        on = (i + tick) % 4 == 0
        if on:
            line += GOLD + "●" + R
        else:
            line += c256(236) + "·" + R
    return line

def show():
    clear()
    sys.stdout.write(HIDE)
    term_w = shutil.get_terminal_size().columns
    box_w = min(74, term_w - 4)
    inner_w = box_w - 6

    # Curtain open
    for tick in range(10):
        clear()
        lines = []
        lines.append("")
        lines.append(center_block([f"{GOLD}{B} ★  W O O D Y ' S   E X I S T E N T I A L   C A B A R E T  ★ {R}"])[0])
        lines.append(center_block([f"{MUTED}Live from a nervous apartment on the Upper West Side{R}"])[0])
        lines.append("")
        marq = marquee_frame(tick, box_w)
        for l in center_block([marq]):
            lines.append(l)

        # tiny stage
        stage_top = f"{MUSTARD}┌{'─' * box_w}┐{R}"
        stage_bot = f"{MUSTARD}└{'─' * box_w}┘{R}"
        lines.append(center_block([stage_top])[0])
        for fline in FACE:
            padded = f"{MUSTARD}│{R} " + fline.center(box_w) if False else f"{MUSTARD}│{R}  " + fline + " "*(box_w - len(strip_ansi(fline)) -2) + f"{MUSTARD}│{R}"
            # instead center face manually
            vis = len(strip_ansi(fline))
            pad = (box_w - vis)//2
            lines.append(center_block([f"{MUSTARD}│{R}" + " "*pad + fline + " "*(box_w - pad - vis) + f"{MUSTARD}│{R}"])[0])

        lines.append(center_block([f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[0])
        lines.append(center_block([SKYLINE.center(box_w+20), f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[-1])
        lines.append(center_block([stage_bot])[0])

        for l in lines:
            sys.stdout.write(l + "\n")
        sleep(0.07)

    # Quote box reveal
    clear()
    # Header again
    for l in center_block([
        "",
        f"{GOLD}{B} ★  W O O D Y ' S   E X I S T E N T I A L   C A B A R E T  ★ {R}",
        f"{MUTED}Live from a nervous apartment on the Upper West Side{R}",
        "",
        center_block([marquee_frame(2, box_w)])[0],
        center_block([f"{MUSTARD}┌{'─' * box_w}┐{R}"])[0],
    ]):
        sys.stdout.write(l+"\n")

    # Face again static
    for fline in FACE:
        vis = len(strip_ansi(fline))
        pad = (box_w - vis)//2
        line = f"{MUSTARD}│{R}" + " "*pad + fline + " "*(box_w - pad - vis) + f"{MUSTARD}│{R}"
        sys.stdout.write(center_block([line])[0] + "\n")

    sys.stdout.write(center_block([f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[0] + "\n")
    sys.stdout.write(center_block([f"{MUSTARD}├{'─' * box_w}┤{R}"])[0] + "\n")

    # Wrapping quote
    wrapped = textwrap.wrap(quote, width=inner_w - 4)
    # top quote decoration
    big_open = f"{GOLD}{B}“{R}"
    big_close = f"{GOLD}{B}”{R}"

    # empty line
    sys.stdout.write(center_block([f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[0] + "\n")

    # animate typing inside box
    for idx, line in enumerate(wrapped):
        vis = len(line)
        pad = (box_w - vis)//2
        # typewriter per line but inside box structure
        prefix = center_block([f"{MUSTARD}│{R}" + " "*pad])[0]
        # we will manually print with box borders
        sys.stdout.write(prefix)
        # add opening quote on first line
        if idx == 0:
            sys.stdout.write(big_open + " ")
        else:
            sys.stdout.write("  ")
        # type the line
        for ch in line:
            sys.stdout.write(f"{CREAM}{I}{ch}{R}")
            sys.stdout.flush()
            time.sleep(0.028)
        if idx == len(wrapped)-1:
            sys.stdout.write(" " + big_close)
        # fill rest + border
        remaining = box_w - pad - vis - 4  # 4 for quotes & spaces
        if idx == 0 or idx == len(wrapped)-1:
            remaining -= 1
        sys.stdout.write(" " * max(0, remaining) + f"{MUSTARD}│{R}\n")
        time.sleep(0.12)

    sys.stdout.write(center_block([f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[0] + "\n")

    # attribution - typewriter right aligned
    attr_vis = len(attribution) + 2  # for —
    pad_attr = box_w - attr_vis - 4
    attr_line_prefix = center_block([f"{MUSTARD}│{R}" + " "*pad_attr])[0]
    sys.stdout.write(attr_line_prefix)
    sys.stdout.write(f"{D}{BEIGE}")
    for ch in attribution:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write(R + "  " + f"{MUSTARD}│{R}\n")

    sys.stdout.write(center_block([f"{MUSTARD}│{R}" + " "*box_w + f"{MUSTARD}│{R}"])[0] + "\n")
    sys.stdout.write(center_block([f"{MUSTARD}└{'─' * box_w}┘{R}"])[0] + "\n")
    sys.stdout.write(center_block([marquee_frame(3, box_w)])[0] + "\n")
    sys.stdout.write("\n")
    for l in center_block([
        f"{MUTED}{D}↳ *nervous clarinet solo*   {MUTED}Anxiety™ is complimentary. Please tip your existential dread.{R}",
        f"{MUTED}{D}  [ Admission: $0  |  Therapy bill: ongoing ]{R}",
    ]):
        sys.stdout.write(l+"\n")

    sys.stdout.write(SHOW)
    sys.stdout.flush()

    # subtle blink of cursor after
    try:
        time.sleep(0.8)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        show()
    finally:
        sys.stdout.write(SHOW + R + "\n")
