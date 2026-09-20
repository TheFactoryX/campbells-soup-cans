"""
Campbell's Soup Can #4995
Produced: 2026-09-20 12:23:44
Worker: Nex AGI: Nex-N2.5-Mini (free) (nex-agi/nex-n2.5-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
PURPLE = "\033[35m"

WIDTH = 74
QUOTE = (
    "I’m not afraid of death. I’m afraid that at the end of life’s grand "
    "cosmic mystery, the answer will be: “Could you repeat the question? "
    "I spent the whole time worrying about the answer.”"
)


def color(text, code):
    return f"{code}{text}{RESET}"


def panel(side, content=""):
    return f"{side}{content:<{WIDTH - 2}}{side}"


def quote_panel(text, code):
    return f"║  {color(text.ljust(64), code)}  ║"


def animate_progress(label):
    for i in range(1, 31):
        percent = i * 3
        bar = color("█" * i, GREEN) + color("░" * (30 - i), DIM)
        sys.stdout.write(f"\r{bar} {percent:02d}%  {label}")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\r" + " " * (WIDTH + 2) + "\n")


def typewriter(line, first=False):
    display = ("“" + line) if first else line
    for n, char in enumerate(display, 1):
        sys.stdout.write("\r" + quote_panel(display[:n], YELLOW))
        sys.stdout.flush()
        pause = 0.030 if char in ".?!" else 0.008
        time.sleep(pause)
    print(quote_panel(display, RESET))


def main():
    sys.stdout.write("\033c")
    print(panel("╔", color("═" * 72, PURPLE)))
    title = " ✦  E X I S T E N T I A L   C O M E D Y  ✦ "
    print(panel("║", f"  {color(title.center(68), BOLD)}  "))
    print(panel("║", color("─" * 72, PURPLE)))
    print(panel("║"))

    animate_progress("PREPARING EXISTENTIAL PANIC")

    wrapped = textwrap.wrap(
        QUOTE,
        width=64,
        break_long_words=False,
        break_on_hyphens=False,
    )
    for index, line in enumerate(wrapped):
        typewriter(line, first=index == 0)

    print(panel("║"))
    print(panel("║", color("  ·  anxiety, lightly seasoned  ·", DIM)))
    print(panel("╚", color("═" * 72, PURPLE)))
    print()

    for _ in range(5):
        sys.stdout.write(color("▮", RED))
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write(color(" ", RED))
        sys.stdout.flush()
        time.sleep(0.12)
    print(color("— the human condition", DIM))


if __name__ == "__main__":
    main()