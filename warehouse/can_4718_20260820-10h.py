"""
Campbell's Soup Can #4718
Produced: 2026-08-20 10:47:06
Worker: Z.ai: GLM 5.2 (free) (z-ai/glm-5.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Neurotic Philosophy Generator (Woody Allen Edition)
-----------------------------------------------------
Prints one existential quote with theatrical flair.
"""

import sys, time, random

# --- ANSI helpers -----------------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
BLINK   = "\033[5m"

FG      = lambda r,g,b: f"\033[38;2;{r};{g};{b}m"
BG      = lambda r,g,b: f"\033[48;2;{r};{g};{b}m"

INK     = FG(40, 40, 60)        # deep ink for text
CREAM   = FG(245, 235, 210)
GOLD    = FG(212, 175, 55)
RUST    = FG(180, 85, 60)
SHADOW  = FG(120, 110, 100)

def clear():  print("\033[2J\033[H", end="")

# --- The Quote (Woody-flavored, original) -----------------------------------
QUOTE = (
    "I have spent my entire life searching for the meaning of existence, "
    "and last Tuesday I think I found it on a napkin in a Chinese restaurant "
    "in Queens. It was a fortune cookie that read: 'You will soon come into "
    "a large sum of money.' I'm still waiting. In the meantime I've decided "
    "the universe is basically a hostile, indifferent void, which is, frankly, "
    "a relief — it means I don't have to be polite to it."
)

ATTRIB = "— Probably Woody Allen, at 2 a.m., in a bathrobe"

# --- Typography: word-wrap to a given width ---------------------------------
def wrap(text, width):
    out, line, ln = [], [], 0
    for word in text.split():
        if ln + len(word) + (1 if line else 0) > width:
            out.append(line); line, ln = [], 0
        line.append(word); ln += len(word) + (1 if line else 0)
    if line: out.append(line)
    return [" ".join(w) for w in out]

# --- A little ASCII bust to set the mood ------------------------------------
BUST = r"""
                .-""""""-.
              .'          '.
             /   O      O   \
            |    .        .  |
            |     .----.     |
             \   /      \   /
              '.\        /.'
                '------'
               ___||||___
              /         \
             /   [====]   \
            /_____________\
"""

# --- Animated film-strip reveal ---------------------------------------------
def filmstrip():
    rows = [l for l in BUST.splitlines() if l.strip()]
    W = max(len(r) for r in rows)
    print()
    for i, r in enumerate(rows):
        r2 = r.center(W)
        tint = FG(40+i*4, 40+i*4, 50+i*6)
        for ch in r2:
            print(f"{tint}{ch}", end="", flush=True)
            time.sleep(0.008)
        print(RESET)
    print()

# --- Typewriter the quote inside a vintage card frame -----------------------
def render():
    clear()

    # Faint film-strip header
    filmstrip()

    width = 66
    lines = wrap(QUOTE, width - 4)  # padding inside frame

    top    = "╭" + "─" * (width-2) + "╮"
    bottom = "╰" + "─" * (width-2) + "╯"
    side   = "│"

    # Title bar
    print(f"{GOLD}{top}{RESET}")
    print(f"{GOLD}{side}{RESET}{BOLD}{CREAM}"
          f"{' A NEUROTIC MEDITATION, NO. 7 ':^{width-2}}{RESET}{GOLD}{side}{RESET}")

    # Separator
    print(f"{GOLD}{side}{RESET}{SHADOW}{'·'* (width-2)}{GOLD}{side}{RESET}")

    # Body with typewriter effect
    for i, line in enumerate(lines):
        print(f"{GOLD}{side}{RESET}  ", end="", flush=True)
        for ch in line:
            color = RUST if random.random() < 0.03 else CREAM
            print(f"{color}{ch}", end="", flush=True)
            time.sleep(0.012 if ch != " " else 0.003)
        # pad to width
        print(f"{' '*(width-4-len(line))}{GOLD}  {side}{RESET}")

    # Attribution
    print(f"{GOLD}{side}{RESET}{SHADOW}{' ':^{width-2}}{GOLD}{side}{RESET}")
    print(f"{GOLD}{side}{RESET}{ITALIC}{GOLD}"
          f"{ATTRIB:^{width-2}}{RESET}{GOLD}{side}{RESET}")
    print(f"{GOLD}{bottom}{RESET}")

    # Trembling footer
    print()
    footer = "[ the void shrugs sympathetically ]"
    for _ in range(3):
        for off in (0, 1, 0, -1):
            print(f"\r{' '*off}{DIM}{SHADOW}{footer}{RESET}", end="", flush=True)
            time.sleep(0.12)
    print("\n")

# --- Run --------------------------------------------------------------------
if __name__ == "__main__":
    try:
        render()
    except KeyboardInterrupt:
        print(f"\n{RESET}\n  [ curtains ]\n")
        sys.exit(0)