"""
Campbell's Soup Can #4973
Produced: 2026-09-16 20:08:17
Worker: LiquidAI: LFM2.5-2.6B (free) (liquid/lfm-2.5-2.6b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-style philosophical quote with visual flair.
Uses ANSI colors and ASCII art for a neurotic, existential vibe.
"""

import time

# ANSI color codes
BG_BLACK = "\033[40m"
BG_RED   = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
TEXT_BLACK = "\033[90m"
TEXT_WHITE = "\033[97m"
RESET = "\033[0m"

def main():
    # The Woody Allen-esque quote - neurotic, self-deprecating, existential
    quote = (
        "I am not afraid of death; "
        "I simply refuse to exist long enough "
        "for anyone to notice. "
        "The universe has already made up its mind — "
        "and I shall wait here, eternally uncertain."
    )

    # Decorative box using Unicode box-drawing characters
    width = 68
    top = "╔" + "═" * (width - 2) + "╗"
    mid = "╠" + "─" * (width - 2) + "╣"
    bot = "╚" + "═" * (width - 2) + "╝"

    # Build lines for animated display
    lines = [
        BG_BLACK + TEXT_WHITE + "WOODY ALLEN'S PHILOSOPHICAL MOMENT" + RESET,
        "",
        top,
        "│",
        " " * 18,
        "│",
        " ".join([
            "I am not afraid of death;",
            "I simply refuse to exist long enough",
            "for anyone to notice.",
            "The universe has already made up its mind — ",
            "and I shall wait here, eternally uncertain."
        ]),
        " │",
        bot,
        "",
        quote.center(width - 2),
        "",
        BG_BLACK + TEXT_WHITE + "— END —" + RESET,
    ]

    # Animate the display: each line appears with a slight delay
    for i, line in enumerate(lines):
        print(line, end='', flush=True)
        time.sleep(0.65)

    # Final clean display
    print("\n" + "=" * 50)
    print(quote.center(50).replace(" ", " ").strip())
    print("=" * 50)

if __name__ == "__main__":
    main()