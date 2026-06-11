"""
Campbell's Soup Can #3910
Produced: 2026-06-11 11:48:20
Worker: Nex AGI: Nex-N2-Pro (free) (nex-agi/nex-n2-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import shutil
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
DIM = "\033[2m"

QUOTE = (
    "I tried to understand the meaning of life, but the meaning of life "
    "saw my browser history and asked to remain anonymous."
)


def wrap(text, width):
    words = text.split()
    lines = []
    current = ""

    for word in words:
        candidate = word if not current else f"{current} {word}"
        if len(candidate) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word

    if current:
        lines.append(current)

    return lines


def main():
    cols = min(max(shutil.get_terminal_size((76, 24)).columns, 50), 84)
    inner = cols - 6
    lines = wrap(QUOTE, inner)

    print()
    print(f"{CYAN}        .-''''''-.")
    print(f"      .'  o    o  '.")
    print(f"     /      __      \\")
    print(f"    |   {MAGENTA}existential{CYAN}    |")
    print(f"     \\      --     /")
    print(f"      '._      _.'")
    print(f"         ''''''{RESET}")
    print()

    top = f"{CYAN}╔{'═' * inner}╗{RESET}"
    bottom = f"{CYAN}╚{'═' * inner}╝{RESET}"

    print(top)

    try:
        print("\033[?25l", end="")

        for line in lines:
            padding = inner - len(line)
            sys.stdout.write(f"{CYAN}║{RESET} {DIM}{BOLD}")

            for ch in line:
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.012)

            sys.stdout.write(f"{RESET}{' ' * padding} {CYAN}║{RESET}\n")

        sys.stdout.write(bottom + "\n")

    finally:
        print("\033[?25h", end="")


if __name__ == "__main__":
    main()