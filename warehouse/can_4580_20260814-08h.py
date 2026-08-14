"""
Campbell's Soup Can #4580
Produced: 2026-08-14 08:37:13
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen meets ANSI colors — a neurotic, philosophical one-liner
served with a side of ASCII art and a typewriter strut.
"""

import time
import sys

# ── ANSI palette ──────────────────────────────────────────────────────────
COLORS = [
    "\033[91m",  # bright red
    "\033[92m",  # bright green
    "\033[93m",  # bright yellow
    "\033[94m",  # bright blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
    "\033[97m",  # white
    "\033[0m",   # reset
]
RESET = "\033[0m"


# ── The Woody-approved quote ──────────────────────────────────────────────
QUOTE = (
    "I don't want to achieve immortality through my work. "
    "I just want to achieve it through not dying, "
    "preferably while napping and with a really good playlist."
)


# ── Simple ASCII "neurotic squirrel" ──────────────────────────────────────
SQUIRREL = r"""
     __ __
    /  --  \
   ( @    @ )
    \  ^  /
     || ||
    /'''''\ 
"""

# ── Typewriter with color shuffle ────────────────────────────────────────
def typewriter(text, delay=0.025):
    """Print text character‑by‑character, cycling through colors."""
    for i, ch in enumerate(text):
        if ch == " ":
            # space: just pause, no color burst
            sys.stdout.write(" ")
            sys.stdout.flush()
            time.sleep(delay)
            continue
        color = COLORS[(i // 3) % len(COLORS)]  # group‑3 color shifts
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)


# ── Main show ─────────────────────────────────────────────────────────────
def main():
    width = max(len(QUOTE.splitlines()[0]) if QUOTE.splitlines() else 0, 10)

    # Header box
    header = "  WOODY'S EXISTENTIAL CORNER  "
    top    = "┌" + "─" * (len(header) - 2) + "┐"
    bot    = "└" + "─" * (len(header) - 2) + "┘"

    # Welcome splash in colors
    for i, line in enumerate([top, header, bot]):
        print(COLORS[i % len(COLORS)] + line + RESET)

    # Our furry philosopher
    print()
    print(COLORS[2] + SQUIRREL + RESET)

    # The moment of reflection
    print()
    print("💭 ", end="", flush=True)
    typewriter(QUOTE)

    # Sign‑off
    print()
    sign = "☯  May your dread be low, your coffee high, "
    sign += "and your afterlife playlist legendary! ☯"
    print(COLORS[5] + sign + RESET)


if __name__ == "__main__":
    main()