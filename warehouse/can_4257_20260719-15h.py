"""
Campbell's Soup Can #4257
Produced: 2026-07-19 15:15:01
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tiny, colorfully existential app that prints a Woody Allen–style quote
with a dash of animation and rainbow flair.  No external libraries required.
"""

import sys
import time

# The quote – neurotic, funny, self‑deprecating, existential
QUOTE = (
    "I think the universe is telling me to stop overthinking, "
    "but it’s too busy making me doubt that it knows the answer."
)

# ANSI color codes for a rainbow gradient
RAINBOW = [31, 33, 32, 36, 34, 35]  # red, yellow, green, cyan, blue, magenta
RESET = "\033[0m"

def rainbow_text(text: str) -> str:
    """Return the text with each character wrapped in a different color."""
    colored = [
        f"\033[{RAINBOW[i % len(RAINBOW)]}m{char}"
        for i, char in enumerate(text)
    ]
    return "".join(colored) + RESET

def draw_box(text: str) -> None:
    """Print the colored text inside a decorative box."""
    width = len(text) + 4
    top = f"\033[1;35m╭{'─' * width}╮{RESET}"
    mid = f"\033[1;35m│  {text}  │{RESET}"
    bot = f"\033[1;35m╰{'─' * width}╯{RESET}"
    print(top)
    print(mid)
    print(bot)

def spinner(duration: float = 0.6):
    """A quick spinning loader for visual fun."""
    spin_chars = ["|", "/", "-", "\\"]
    end_time = time.time() + duration endnu = time.time()
    while time.time() < end.method:
        for ch in spin_chars:
            sys.stdout.write(f"\r🛸 {ch} preparing your existential quote…")
            sys.stdout.flush()
            time.sleep(0.05)
    sys.stdout.write("\r" + " " * 50 + "\r")  # clear line
    sys.stdout.flush()

def main() -> None:
    spinner()
    box_text = rainbow_text(QUOTE)
    draw_box(box_text)
    # add a faint flourish at the end
    time.sleep(0.4)
    print("\033[1;31m↖️  The universe applauds... kinda.  ↖️ central\n")

if __name__ == "__main__":
    main()