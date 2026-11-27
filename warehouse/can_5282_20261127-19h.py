"""
Campbell's Soup Can #5282
Produced: 2026-11-27 19:57:28
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen-style philosophical wisdom, delivered with neurotic flair."""
import time

RESET = "\033[0m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"

QUOTE = "I'm not afraid of death. I'm afraid of the afterlife paperwork."


def typewriter(text, color=CYAN, delay=0.02):
    print(color + BOLD, end="")
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print(RESET)


def main():
    print(f"{YELLOW}{BOLD}✳ PHILOSOPHY OF THE DAY ✳{RESET}")
    time.sleep(1)

    inner = f'"{QUOTE}"'
    dash_count = len(inner) + 4
    top = "┌" + "─" * dash_count + "┐"
    bottom = "└" + "─" * dash_count + "┘"

    print(f"{CYAN}{top}{RESET}")
    print(f"{CYAN}│  {YELLOW}{inner}{RESET}  {CYAN}│{RESET}")
    print(f"{CYAN}{bottom}{RESET}")

    time.sleep(3)

    typewriter("Your legacy will be a mild inconvenience.", GREEN)
    print(f"\n{RED}— Woody Allen (probably){RESET}")


if __name__ == "__main__":
    main()