"""
Campbell's Soup Can #4817
Produced: 2026-08-24 19:44:38
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote generator - pure Python."""
import sys
import time

# ANSI color codes as reusable strings
R = "\033[0m"  # reset
B = "\033[1m"  # bold
C = "\033[96m"  # cyan
Y = "\033[93m"  # yellow
G = "\033[92m"  # green
M = "\033[95m"  # magenta

W = 50  # box width


def main():
    # ── cheerful neurotic header ──────────────────────────────────────
    print(f"\n{C}┌{'─' * W}┐{R}")
    print(f"{C}│{B} Neurotic Philosophy Generator {C}│{R}")
    print(f"{C}└{'─' * W}┘{R}\n")

    # ── ASCII art: a slightly neurotic brain ───────────────────────────
    art = r"""
   .--.     .--.
  / o o\   / o o\
 (   ^  ^ ) (   ^  ^ )
  \  --  /   \  --  /
   `----'     `-----"""
    print(f"{M}{art}{R}")

    # ── Woody Allen style philosophical quote ─────────────────────────
    quote = [
        f"{Y}I don't want to achieve immortality through my work.{R}",
        f"{G}I just want to achieve it by not dying.{R}",
        f"{M}...and I'm pretty sure the afterlife has terrible lighting.{R}"
    ]

    top = f"{B}┌{'─' * W}┐{R}"
    bottom = f"{B}└{'─' * W}┘{R}"
    side = f"{B}│{' ' * W}│{R}"

    print(top)
    print(side)
    for line in quote:
        print(f"{B}│{R}   {line}   {B}│{R}")
    print(side)
    print(bot)
    print()

    # ── final neurotic footnote ───────────────────────────────────────
    print(f"{Y}Quick thought:{R} {B}If we're all going to die anyway,{R}")
    print("at least the code compiles.{R}\n")


if __name__ == "__main__":
    main()