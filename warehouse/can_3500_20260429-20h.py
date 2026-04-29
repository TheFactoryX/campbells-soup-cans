"""
Campbell's Soup Can #3500
Produced: 2026-04-29 20:34:54
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ── ANSI Palette ───────────────────────────────────────────────
B = "\033[1;90m"    # bright black
R = "\033[1;91m"    # bright red
G = "\033[1;92m"    # bright green
Y = "\033[1;93m"    # bright yellow
Blu = "\033[1;94m"  # bright blue
M = "\033[1;95m"    # bright magenta
C = "\033[1;96m"    # bright cyan
W = "\033[1;97m"    # bright white
D = "\033[22;39m"   # dim reset-ish
Z = "\033[0m"       # reset all

# ── Frame ───────────────────────────────────────────────────────
def frame(text, color=C, border_color=M):
    w = 62
    lines = []
    for line in text.split("\n"):
        while len(line) < w - 4:
            line += " "
        lines.append(line[:w - 4])
    top    = border_color + "  " + "═" * w + Z
    mid    = border_color + "  ║" + Z + color + "".join(lines) + Z + border_color + "║" + Z
    bot    = border_color + "  " + "═" * w + Z
    return top + "\n" + mid + "\n" + bot

# ── Typing ──────────────────────────────────────────────────────
def typer(s, speed=0.006, color=W, glitch=False):
    for ch in s:
        if glitch and random.random() < 0.03:
            sys.stdout.write(random.choice("!@#$%^&*()_+-="))
            sys.stdout.flush()
            time.sleep(0.04)
            sys.stdout.write("\b" + color)
        sys.stdout.write(color + ch + Z)
        sys.stdout.flush()
        time.sleep(speed * random.uniform(0.5, 2.5) if glitch else speed)
    print()

# ── Sparkle ─────────────────────────────────────────────────────
def sparkle(n=30):
    chars = "✧*•♪♫✦✩✨"
    for _ in range(n):
        x = random.randint(0, 60)
        y = random.randint(0, 12)
        print(f"\033[{y};{x}H{random.choice(chars)}", end="")
    print(f"\033[{14};1H", end="")

# ── Nervous Pulse ───────────────────────────────────────────────
def pulse(text, cycles=3):
    shades = [R, Y, M, C, G]
    for i in range(cycles):
        for s in shades:
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.write(s + text + Z)
            sys.stdout.flush()
            time.sleep(0.08)
    print()

# ── Background Scroll ───────────────────────────────────────────
def scroll_bars(color=B, delay=0.02):
    for i in range(8):
        print(color + "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  " + Z)
        time.sleep(delay)

# ── The Quote ──────────────────────────────────────────────────
def the_quote():
    return (
        "I’ve been to the edge of the void, but the void was\n"
        "closed for existential maintenance, so I went to a\n"
        "deli instead and ordered a sandwich that reminded me\n"
        "of my childhood—which is to say, slightly damp and\n"
        "uncertain of its own reality. Death doesn’t frighten\n"
        "me; it’s just that the silence afterward sounds\n"
        "suspiciously like my mother-in-law’s voicemail, and\n"
        "I’m not emotionally equipped for that much quiet.\n"
        "Besides, if immortality is achieved by not dying, then\n"
        "I’ve already failed spectacularly at living, which\n"
        "feels suspiciously like a win."
    )

# ── Main ───────────────────────────────────────────────────────
def main():
    print(f"\033[?25l")  # hide cursor
    try:
        # ── Intro ───────────────────────────────────────────
        print(f"\033[2J\033[H")  # clear
        sparkle(40)
        time.sleep(0.5)
        pulse("  W O O D Y   A L L E N ' S   E X I S T E N T I A L   D E L I  ", 5)
        time.sleep(0.6)

        # ── Animated bars ─────────────────────────────────────
        print()
        scroll_bars(B, 0.03)
        print()

        # ── Quote reveal with typewriter ───────────────────────
        q = the_quote()
        framed = frame(q, color=W, border_color=Blu)
        # split framed into lines for typer
        f_lines = framed.split("\n")
        for line in f_lines:
            typer(line + "\n", speed=0.003, color=W, glitch=(random.random()<0.15))
            time.sleep(0.08)

        # ── Signature ─────────────────────────────────────────
        time.sleep(0.6)
        print()
        pulse("           — neurotic but essentially harmless           ", 2)
        print()

        # ── Confetti shower ────────────────────────────────────
        for _ in range(5):
            sparkle(25)
            time.sleep(0.15)

        # ── Fade out ───────────────────────────────────────────
        print(f"\n{Y}  (system panic in 3.. 2.. 1.. none, just anxiety lingering){Z}")
        time.sleep(1.2)

    finally:
        print(f"\033[?25h")  # show cursor
        print(f"\033[0m", end="")

if __name__ == "__main__":
    main()