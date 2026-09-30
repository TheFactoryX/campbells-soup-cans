"""
Campbell's Soup Can #5046
Produced: 2026-09-30 13:44:28
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
A neurotic little Python script that delivers a philosophical crisis
in the style of Woody Allen — with flair, color, and dramatic flair.
"""

import sys
import time
import itertools

# ─── ANSI color codes ─────────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    BLINK   = "\033[5m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    ORANGE  = "\033[93m"

# ─── Typewriter effect ────────────────────────────────────────────
def typewriter(text, delay=0.04, color=Color.CYAN, end="\n"):
    for char in text:
        sys.stdout.write(color + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

# ─── Blinking effect ──────────────────────────────────────────────
def blink(text, times=3, speed=0.4, color=Color.YELLOW):
    for _ in range(times):
        sys.stdout.write("\r" + color + text + Color.RESET)
        sys.stdout.flush()
        time.sleep(speed)
        sys.stdout.write("\r" + " " * len(text) + "\r")
        sys.stdout.flush()
        time.sleep(speed)

# ─── Animated border ──────────────────────────────────────────────
def animated_border(width=60, height=3, colors=None):
    if colors is None:
        colors = [Color.MAGENTA, Color.CYAN, Color.YELLOW]
    bar = "═" * width
    for i in range(height):
        c = colors[i % len(colors)]
        sys.stdout.write(c + bar + Color.RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.1)

# ─── ASCII Art: existential crisis in a teacup ───────────────────
TITLE_ART = r"""
     ╔═════════════════════════════════════════════════════════╗
     ║              _   _   _   _   _                         ║
     ║             ( ) ( ) ( ) ( ) ( )                        ║
     ║              _\_\\//_//_//\\_//                         ║
     ║             |  ╭┈╮         |    WOODY MODE ACTIVATED   ║
     ║             |  ╰┈╯    ⌣    |    PHILOSOPHICAL ENGINE    ║
     ║             |  ┌┈┐        |    NEUROTIC OUTPUT         ║
     ║             |__└┴┘        |    DO NOT PANIC            ║
     ║              |  |         |    (But panic anyway)      ║
     ║              |  |         |                             ║
     ║              |__|         |                             ║
     ║             ╱____╲       |                             ║
     ║            |      |     _|                             ║
     ║            |      |____|                               ║
     ╚═════════════════════════════════════════════════════════╝
"""

# ─── The actual Woody Allen-style quote ───────────────────────────
QUOTE_LINES = [
    "I've been thinking about mortality lately.",
    "Not in a morbid way — well, actually, exactly that.",
    "I lie in bed at night counting sheep,",
    "but the sheep are insurance salesmen,",
    "and they keep calling...",
    "I don't fear death.",
    "I just don't want to be there when it happens.",
    "Which is ironic,",
    "because honestly,",
    "death is the one appointment",
    "I’ve been consistently",
    "not showing up to...",
    "And now I'm worried",
    "that even my avoidance of death",
    "is part of some cosmic joke.",
    "What do you mean, 'you're not supposed to think about it'?!",
    "That's literally ALL I do!",
    "",
    " — In the voice of someone",
    "who booked a reservation at",
    "the End of Everything,",
    "but forgot to bring a jacket.",
]

# ─── Rainbow marquee effect ──────────────────────────────────────
def rainbow_marquee(text, cycles=2, delay=0.15):
    colors = itertools.cycle([
        Color.RED, Color.YELLOW, Color.GREEN,
        Color.CYAN, Color.BLUE, Color.MAGENTA
    ])
    padded = text[:50]
    for _ in range(cycles):
        line = next(colors) + padded + Color.RESET
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + " " * len(padded) + "\r")
    sys.stdout.flush()

# ─── Main event ───────────────────────────────────────────────────
def main():
    # Clear screen for drama
    print("\033[2J\033[H", end="")

    # Title reveal
    typewriter(
        "\n  🤖  PHILOSOPHICAL NEUROSIS v3.14159... 🤖\n",
        delay=0.03,
        color=Color.MAGENTA,
    )
    time.sleep(0.3)

    # ASCII art reveal
    typewriter(TITLE_ART, delay=0.005, color=Color.CYAN)
    time.sleep(0.5)

    # Pulsing border
    animated_border()

    # Blinking emphasis
    blink(" INITIATING EXISTENTIAL QUOTE ENGINE... ", times=3)
    print()

    # Rainbow marquee
    rainbow_marquee("🌀 Woody Allen Philosophy Simulator 🌀")

    # The quote itself — slow, dramatic typewriter
    print()
    for i, line in enumerate(QUOTE_LINES):
        color = Color.YELLOW if i % 2 == 0 else Color.CYAN
        if line.strip() == "":
            print()
            continue
        if line.startswith(" — "):
            typewriter(" " + line, delay=0.06, color=Color.ORANGE)
        else:
            typewriter("   " + line, delay=0.05, color=color)
        time.sleep(0.15)

    # Dramatic pause
    time.sleep(1.2)
    blink("     (cue awkward pause for existential dread)     ", times=2)

    # Closing flair
    print()
    animated_border(height=1)
    typewriter(
        "\n  ✨ You are here. You will not be. Enjoy the paradox! ✨\n",
        delay=0.04,
        color=Color.GREEN,
    )

if __name__ == "__main__":
    main()