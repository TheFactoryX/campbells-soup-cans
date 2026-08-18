"""
Campbell's Soup Can #4679
Produced: 2026-08-18 17:43:03
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen Style Philosophical Quote
with terminal eye-candy — no external dependencies,
just pure Python and cosmic anxiety.
"""
import sys
import time
import random

# ─── ANSI Colors ─────────────────────────────────────────────
R = '\033[91m'      # Red
G = '\033[92m'      # Green
Y = '\033[93m'      # Yellow
B = '\033[94m'      # Blue
P = '\033[95m'      # Pink / Magenta
Cy = '\033[96m'     # Cyan
W = '\033[97m'      # White
BLD = '\033[1m'     # Bold
DIM = '\033[2m'     # Dim / Faint
IT = '\033[3m'      # Italic
RST = '\033[0m'     # Reset

COLORS = [R, G, Y, B, P, Cy]


# ─── Helpers ─────────────────────────────────────────────────
def w(text):
    """Write text to stdout and flush immediately."""
    sys.stdout.write(text)
    sys.stdout.flush()


def wait(t):
    time.sleep(t)


def typewriter(text, delay=0.04):
    """Print text character-by-character with slight randomness."""
    for ch in text:
        w(ch)
        wait(delay * (0.3 + 0.7 * random.random()))


def print_clear():
    """Clear the terminal screen."""
    w('\033[2J\033[H')


# ─── Main ────────────────────────────────────────────────────
def main():
    print_clear()

    # ── ASCII Art: Our Neurotic Philosopher ──
    art = f"""
{Cy}{DIM}
        ,--.   ,--.
        )\\  ) (  /(/
       / ,'/\\_ \\ ,\\
      | ( (  oo)   |
      |  \\_\\_  //) |
       \\  \\_/(_/  /
        '._  ___  .'
           | |  | |
        __| |  | |__
       /  | |  | |  \\
      |   | |  | |   |
      |   |_|  |_|   |
       \\            /
        `───────────'
         |  |  |  |
         |  |  |  |
         |__|  |__|
{RST}"""

    for ch in art:
        w(ch)
        wait(0.002)
    wait(0.3)

    # ── Thinking Animation ──
    w(f'\n{Y}{IT}  ...processing{RST}')
    for _ in range(4):
        wait(0.4)
        w(Y + IT + '.' + RST)
    wait(0.3)
    w(f' {P}(existentially exhausted){RST}\n\n')
    wait(0.6)

    # ── The Quote ──
    # A custom Woody Allen-style philosophical gem:
    # neurotic, self-deprecating, and existentially anxious.
    quote_lines = [
        "I'm not afraid of death; I just resent",
        "that it has better timing than me.",
        "It shows up uninvited and ruins everything",
        "\u2014 just like my in-laws, except death at",
        "least comes with a sense of purpose.",
    ]

    box_width = 54

    # Top border — animated, rainbow
    w('\n')
    top = '\u2554' + '\u2550' * box_width + '\u2557'
    for ch in top:
        wait(0.008)
        w(random.choice(COLORS) + ch + RST)
    w('\n')

    # Quote content — typewriter effect with color cycling
    for line in quote_lines:
        inner = '  ' + line
        padding = ' ' * (box_width - len(inner))
        w(DIM + '\u2551' + RST)
        for ch in inner:
            wait(0.03)
            w(random.choice(COLORS) + ch + RST)
        w(padding)
        wait(0.1)
        w(DIM + '\u2551' + RST + '\n')

    # Bottom border — animated, rainbow
    bottom = '\u255a' + '\u2550' * box_width + '\u255d'
    for ch in bottom:
        wait(0.008)
        w(random.choice(COLORS) + ch + RST)

    wait(0.8)

    # ── Attribution ──
    w(f'\n{DIM}{IT}  \u2014 A brief moment of lucidity in an otherwise{RST}')
    wait(0.3)
    w(f'\n{DIM}{IT}    meaningless cosmic void{RST}\n')
    wait(0.8)

    # ── Coda ──
    w(f'\n{P}{BLD}  [Clinical Note: This is why I am still single]{RST}\n')
    wait(1.5)

    # ── Floating Thoughts ──
    thoughts = [
        f"{Y}  ...should I be concerned that I'm not concerned enough?{RST}",
        f"{B}  ...did the universe expand, or did I just get smaller?{RST}",
        f"{G}  ...I came for wisdom, I'm leaving with indigestion.{RST}",
    ]

    for t in thoughts:
        wait(1.8)
        typewriter(t)
        wait(1.5)
        w('\r' + ' ' * 70 + '\r')

    wait(1)
    w(f'\n{DIM}  The universe yawns. Then it forgets about me.{RST}\n')
    wait(1.5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        w(f'\n\n{R}{BLD}  Run interrupted.{RST}\n')
        w(f'{DIM}  The existential crisis will resume shortly.{RST}\n')