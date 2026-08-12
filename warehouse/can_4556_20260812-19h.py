"""
Campbell's Soup Can #4556
Produced: 2026-08-12 19:25:56
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
import textwrap

# ANSI color palette (256‑color foregrounds)
COLORS = [f'\033[38;5;{i}m' for i in range(200, 230, 5)]
RESET = '\033[0m'


def color(text: str, fg: str) -> str:
    """Wrap text with ANSI foreground color and reset."""
    return fg + text + RESET


def spinner(duration: float = 1.5) -> None:
    """Show a simple thinking spinner for a few seconds."""
    spin = itertools.cycle(['|', '/', '-', '\\'])
    end = time.time() + duration
    while time.time() < end:
        sys.stdout.write('\r' + color(next(spin), COLORS[0]) + ' Thinking...')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()


def main() -> None:
    # Original Woody‑Allen‑style quote (neurotic, funny, self‑deprecating)
    quote = (
        "I'm terrified of commitment; the only relationship I can truly commit to "
        "is with my therapist."
    )
    width = 58  # inner width of the box

    # Wrap the quote to fit inside the box
    lines = textwrap.wrap(quote, width)

    # Build decorative box
    top = '╔' + '═' * (width + 2) + '╗'
    bottom = '╚' + '═' * (width + 2) + '╝'

    # Show a brief thinking animation
    spinner()

    # Print top border
    sys.stdout.write(color(top, COLORS[2]) + '\n')

    # Print each line with a type‑writer effect and per‑character color cycling
    for line in lines:
        padded = line.ljust(width)
        sys.stdout.write(color('║ ', COLORS[2]))
        for ch in padded:
            fg = COLORS[ord(ch) % len(COLORS)]
            sys.stdout.write(color(ch, fg))
            sys.stdout.flush()
            time.sleep(0.02)  # typing delay
        sys.stdout.write(color(' ║', COLORS[2]) + '\n')

    # Print bottom border
    sys.stdout.write(color(bottom, COLORS[2]) + '\n')
    sys.stdout.flush()

    # A tiny neurotic face for extra flavor
    sys.stdout.write(
        color('\n   (•̀ᴗ•́)و  – Woody Allen vibes\n', COLORS[4])
    )
    sys.stdout.flush()


if __name__ == '__main__':
    main()