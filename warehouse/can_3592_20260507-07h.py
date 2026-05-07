"""
Campbell's Soup Can #3592
Produced: 2026-05-07 07:18:10
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

def colorize(text: str, code: str) -> str:
    """Wrap text with ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def typewriter(words, delay=0.04):
    """Print words one‑by‑one with a brief pause."""
    for i, w in enumerate(words):
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(" ")
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Optional: clear screen for a clean start
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Header
    header = "─── Woody Allen's Philosophical Wisdom ───"
    sys.stdout.write(colorize(header, "1;36") + "\n")
    sys.stdout.flush()
    time.sleep(0.5)

    # ASCII thought‑bubble art
    thought_art = (
        r"""
           .-""""-.
          /        \
         |  O    O  |
         |    __    |
          \  \__/  /
           '-....-'
              |\
              | \
           ~~~|  ~~~
        """
    )
    for line in thought_art.splitlines():
        sys.stdout.write(colorize(line, "1;33") + "\n")
        sys.stdout.flush()
        time.sleep(0.05)

    # The quote – each word in a random bright colour
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    words = quote.split()
    bright_colors = ["1;31", "1;32", "1;33", "1;34", "1;35", "1;36"]
    for w in words:
        c = random.choice(bright_colors)
        sys.stdout.write(colorize(w, c))
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Decorative separator
    sep = "═" * 60
    sys.stdout.write(colorize(sep, "1;31") + "\n")
    sys.stdout.flush()
    time.sleep(0.3)

    # Tiny spinner animation – Woody is thinking
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(20):
        for ch in spinner:
            sys.stdout.write(f"\r{colorize(ch, '1;35')}  Woody Allen is thinking...   ")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")   # clear the line
    sys.stdout.flush()

if __name__ == "__main__":
    main()