"""
Campbell's Soup Can #4609
Produced: 2026-08-15 16:41:32
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]
RESET = "\033[0m"

def rainbow_text(text):
    """Return text with each character colored in a rotating rainbow."""
    out = []
    for i, ch in enumerate(text):
        out.append(COLORS[i % len(COLORS)] + ch)
    return "".join(out) + RESET

def spinner(duration=1.5):
    """Show a simple spinner for `duration` seconds."""
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write('\r' + next(spinner_cycle) + ' Pondering...')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # clear line

def main():
    # Woody Allen‑style quote (original)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Show a brief thinking animation
    spinner(1.2)

    # Build decorative box
    border = "╔" + "═" * (len(quote) + 4) + "╗"
    bottom = "╚" + "═" * (len(quote) + 4) + "╝"
    side = "║"

    # Print with colors
    print("\033[96m" + border + RESET)  # cyan top border
    print(side + "  " + rainbow_text(quote) + "  " + side)
    print("\033[96m" + bottom + RESET)  # cyan bottom border

if __name__ == "__main__":
    main()