"""
Campbell's Soup Can #4618
Produced: 2026-08-16 03:12:47
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ── Woody Allen-style philosophical quote ──────────────────────────────
QUOTE = "I'm not afraid of death. I just don't want to be there when it happens. "
QUOTE += "Mostly because I'd have to explain to the Grim Reaper why I spent "
QUOTE += "twenty minutes debating whether 'maybe' is a valid reply to a text message."

# ── ANSI color palette (pure Python, no external deps) ───────────────────
COLORS = {
    "reset": "\033[0m",
    "bold":  "\033[1m",
    "cyan":  "\033[36m",
    "magenta": "\033[35m",
    "yellow": "\033[33m",
}

# ── Typewriter reveal (playful animation) ───────────────────────────────
def typewriter(text, speed=0.03):
    """Print text character‑by‑character for a fun reveal effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ── Main ─────────────────────────────────────────────────────────────────
def main():
    W = 200                                              # border width

    # Colored ASCII border
    top    = COLORS["magenta"] + COLORS["bold"] + "┏" + "━" * (W - 2) + "┓" + COLORS["reset"]
    bottom = COLORS["magenta"] + COLORS["bold"] + "┗" + "━" * (W - 2) + "┛" + COLORS["reset"]
    side   = COLORS["cyan"] + "┃" + " " * (W - 2) + "┃" + COLORS["reset"]

    print(top)
    print(side)
    print(side)

    # Typewriter‑reveal the quoted line in bold cyan
    quoted = COLORS["bold"] + COLORS["cyan"] + '"' + QUOTE + '"' + COLORS["reset"]
    typewriter(quoted)

    print(side)
    print(bottom)

if __name__ == "__main__":
    main()