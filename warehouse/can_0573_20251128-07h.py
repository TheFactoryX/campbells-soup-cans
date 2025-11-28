"""
Campbell's Soup Can #573
Produced: 2025-11-28 07:31:41
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful Woody‑Allen‑style philosophical quote, wrapped in a colorful box,
with a little spinner animation to build up the existential dread.
"""

import os
import sys
import time

# ANSI color codes
COLORS = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan

def colorize(word: str, idx: int) -> str:
    """Wrap a word in an ANSI color escape based on its position."""
    return f"\033[{COLORS[idx % len(COLORS)]}m{word}\033[0m"

# The Woody‑Allen‑style quote
PHILOSOPHY = (
    "I find the universe like a bad TV network: endless drama, no scripts, "
    "and I never know where the commercial break ends."
)

# Build a colorized version of the quote
COLORIZED = ' '.join(colorize(w, i) for i, w in enumerate(PHILOSOPHY.split()))

# Utility functions ---------------------------------------------------------

def clear_screen() -> None:
    """Clear the terminal screen in a cross‑platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner(duration: float = 2.0) -> None:
    """A little spinner animation while 'thinking'."""
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    sys.stdout.write('Thinking ')
    while time.time() < end_time:
        sys.stdout.write('\rThinking ' + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # clear the line

def box_top(width: int) -> str:
    """Top border of the box."""
    return f"\033[35m╔{'═' * width}╗\033[0m"

def box_middle(content: str, width: int) -> str:
    """Middle part of the box with the quote."""
    return f"\033[35m║{content:^{width}}║\033[0m"

def box_bottom(width: int) -> str:
    """Bottom border of the box."""
    return f"\033[35m╚{'═' * width}╝\033[0m"

# ---------------------------------------------------------------

def main() -> None:
    spinner()
    clear_screen()

    # We'll pad the quote with two spaces on each side to make it look nicer
    padded = f"  {COLORIZED}  "
    # The interior width of the box is the length of PHILOSOPHY plus 4 padding
    interior_width = len(PHILOSOPHY) + 4

    print(box_top(interior_width))
    print(box_middle(padded, interior_width))
    print(box_bottom(interior_width))

if __name__ == "__main__":
    main()