"""
Campbell's Soup Can #4711
Produced: 2026-08-20 03:58:50
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""🧠💨 Woody Allen style philosophy, served with ANSI colors and ASCII flair."""
import time
import sys

# ── ANSI color palette ────────────────────────────────────────────────
R  = "\033[91m"  # red
G  = "\033[92m"  # green
Y  = "\033[93m"  # yellow
B  = "\033[94m"  # blue
M  = "\033[95m"  # magenta
C  = "\033[96m"  # cyan
W  = "\033[97m"  # white
RST = "\033[0m"
BLD = "\033[1m"

# ── typewriter printer ────────────────────────────────────────────────
def typewriter(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ── ASCII border helpers ──────────────────────────────────────────────
TOP_LEFT = f"{BLD}{B}{'┌'}{'─'*60}┐{RST}"
TOP_RIGHT = f"{BLD}{B}{'┐'}{'─'*60}┐{RST}"  # just used conceptually
MID_SEP  = f"{BLD}{B}{'├'}{'─'*60}┤{RST}"
BOTTOM   = f"{BLD}{B}{'└'}{'─'*60}┘{RST}"

# Woody's neurotic masterpiece
QUOTE = (
    '"I\'m not afraid of death. I just don\'t want to be there when it happens— '
    'I\'ll probably just stand there apologizing to the oxygen, '
    'hoping it doesn\'t mind my neurotic energy."'
)

# ── tiny "thinking" animation ─────────────────────────────────────────
def thinking_animation():
    frames = ["( ͡° ͜ʖ ͡°)", "( ͡° ʖ ͡°)", "( ʖ ͡° ͡°)", "( ͡° ͜ʖ)"]
    for _ in range(3):
        for f in frames:
            print(f"\r{Y}Thinking...{f}{RST}", end="", flush=True)
            time.sleep(0.12)
    print("\r" + " " * 20, end="\r")  # clear line

# ── main ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # border + title
    print(BLD + B + "┌" + "─"*60 + "┐" + RST)
    print(f"{C}🧠  WOODY'S THOUGHT CORNER  🧠{RST}")
    print(BLD + B + "├" + "─"*60 + "┤" + RST)

    # thinking animation
    thinking_animation()

    # the quote with style
    print(f"{Y}{BLD}➤{RST} {M}{BLD}{QUOTE}{RST}")

    # footer
    print(BLD + B + "└" + "─"*60 + "┘" + RST)

    # typewriter reveal (optional flair; comment out if instant is preferred)
    # typewriter(QUOTE, delay=0.015)