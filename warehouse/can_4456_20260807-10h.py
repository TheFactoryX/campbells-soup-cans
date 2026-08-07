"""
Campbell's Soup Can #4456
Produced: 2026-08-07 10:13:15
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
✨ Woody Allen: The Philosophical Quote Generator ✨
A visually stunning terminal program displaying funny, existential quotes.
Pure Python, no external dependencies.
"""

import time
import sys

# ─── ANSI Color Codes ─────────────────────────────────────────────────────
class C:
    R = "\033[91m"
    G = "\033[92m"
    Y = "\033[93m"
    B = "\033[94m"
    M = "\033[95m"
    C = "\033[96m"
    W = "\033[97m"
    D = "\033[90m"
    R2 = "\033[1;91m"
    G2 = "\033[1;92m"
    Y2 = "\033[1;93m"
    B2 = "\033[1;94m"
    M2 = "\033[1;95m"
    C2 = "\033[1;96m"
    S = "\033[2m"
    N = "\033[22m"
    I = "\033[3m"
    T = "\033[9m"
    R0 = "\033[0m"
    BK = "\033[40m"
    BR = "\033[41m"
    BG = "\033[42m"
    BY = "\033[43m"
    BL = "\033[44m"
    BC = "\033[46m"
    BM = "\033[45m"
    BRI = "\033[90m"

def _c(color, text):
    return f"{color}{text}{C.R0}"

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def sleep(n=0.08):
    time.sleep(n)

# ═══════════════════════════════════════════════════════════════════════════
#  Starfield animation
# ═══════════════════════════════════════════════════════════════════════════
def stars():
    import random
    random.seed(int(time.time() * 1000))
    for _ in range(40):
        x = random.randint(0, 100)
        y = random.randint(0, 30)
        print(_c(C.M, "★"), end="", flush=True)
        sleep(0.12)

# ═══════════════════════════════════════════════════════════════════════════
#  Animated quote printer (typewriter + fade)
# ═══════════════════════════════════════════════════════════════════════════
def type_quote(quote, delay=0.015, color=None):
    """Print a quote character by character with optional color."""
    if color is None:
        color = C.D
    for line in quote.strip().split("\n"):
        if line.strip():
            print(_c(color, line), end="\n", flush=True)
            sleep(delay)

# ═══════════════════════════════════════════════════════════════════════════
#  Main program
# ═══════════════════════════════════════════════════════════════════════════
def main():
    clear()

    # ── Decorative header ──
    print(_c(C.W, "╔═══════════════════════════════════════════════════╗"))
    print(_c(C.C, "║     ★   ★   ★   ★   ★   ★   ★   ★   ★   ★   ║"))
    print(_c(C.C, "║     W O O D Y   A L L E N    P H I L O S O P H I A L     ║"))
    print(_c(C.Y, "║     " + "✦" * 34 + "         " + "✦" * 34 + "         ║"))
    print(_c(C.C, "║     ★   ★   ★   ★   ★   ★   ★   ★   ★   ★   ║"))
    print(_c(C.W, "╚═══════════════════════════════════════════════════╝"))

    # ── The quotes ──
    print()

    # Quote 1 - classic Woody Allen
    q1 = """
  ~~~  "I'm not afraid of death.  I just don't want to be there when it happens."  ~~~

  ~~~  "Life is full of misery, loneliness, and suffering — and it's all over much too soon."  ~~~

  ~~~  "I don't want to achieve immortality through my work. I want to achieve it through not dying."  ~~~

  ~~~  "I love that old saying: Life is a bag of sins. We just have to carry it carefully."  ~~~

  ~~~  "I am not afraid of the dark. I am afraid of being the only one who thinks it's dark."  ~~~

  ~~~  "The thing about people who feel too much is that they never learn anything."  ~~~

  ~~~  "We're all just a little bit crazy. That's the secret."  ~~~
    """
    type_quote(q1, delay=0.02, color=C.G)

    # ── Second decorative line ──
    print(_c(C.D, " " + "─" * 70))
    print()

    # ── Fun ASCII art ──
    print(_c(C.Y, "╔═══════════════════════════════════════════════════════╗"))
    print(_c(C.Y, "║   ┌───────────────────────────────────────────────────┐  ║"))
    print(_c(C.Y, "║   │     ╭─────●─────────────────────────────────────╮  │  ║"))
    print(_c(C.Y, "║   │    │        ·         ·       ·           ·        │  ║"))
    print(_c(C.Y, "║   │    │   ┌─────────────────────────────────┐   │  ║"))
    print(_c(C.Y, "║   │    │  │  ✦   ♫  ★  ★  ♫  ✦   ★   ★  ♫  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  ·   ✦   ★  ☆   ·   ♫  ★   ★  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  ╭─────────────────────────────╮  │  ║"))
    print(_c(C.Y, "║   │    │  │  │   🎬 Woody Allen    🎬  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  │  🧘  Philosophical  🧘  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  │   🧠  Mind & Heart     │  │  ║"))
    print(_c(C.Y, "║   │    │  │  │  🧘  Philosophical  🧘  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  │  🎬 Woody Allen    🎬  │  │  ║"))
    print(_c(C.Y, "║   │    │  │  ╰─────────────────────────────╯  │  ║"))
    print(_c(C.Y, "║   │    │  │   ╭─────────────────────────╮  │  ║"))
    print(_c(C.Y, "║   │    │  │   │    💭       💭   │   │  ║"))
    print(_c(C.Y, "║   │    │  │   ╰─────────────────────────╯  │  ║"))
    print(_c(C.Y, "║   │    │  │   🧘     ·     ·    🧘   │  │  ║"))
    print(_c(C.Y, "║   │    │  │   ╭─────────────────────────╮  │  ║"))
    print(_c(C.Y, "║   │    │  │  │   🧠   🧘     🧠     🧘   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   ╭─────────────────────────╯  │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    ♫  ♥  ★    ♫       │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │  ★  ●   ♫  ★   ●    │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │  ●  ★    ●   ★  ●    │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │  ★  ·    ·  ★  ★  │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │   ♫    ♫    ♫    │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │  ★  ★  ☆  ★    │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │  ·   ·   ·   ·   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │   ♫ ♫   ♫ ♫   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   │    │  │  │   │    │    │    │   │  ║"))
    print(_c(C.Y, "║   └───────────────────────────────────────────────────┘  ║"))
    print(_c(C.W, "╚═══════════════════════════════════════════════════════╝"))

    # ── The final words ──
    print()
    print(_c(C.B, "  ───  From the heart of a neurotic philosopher  ───  "))
    print(_c(C.W, "    Every philosophy is just a story you haven't told yet."))
    print(_c(C.G, "    Made with  ✓ Python  ✓ ANSI Colors  ✓ Pure Python  ✓✗  "))
    print(_c(C.N, "    'Life is an opportunity to practice being terrible.'"))
    print()
    print(_c(C.W, " ═══════════════════════════════════════════════════════════ "))
    print()
    print(_c(C.D, "  ★  🧘  ♫  🧠  ★  🌿  ★  ♫  ★  🦋  ★  ♫  ★  🧘  ★  ★  ★  "))
    print()

if __name__ == "__main__":
    main()