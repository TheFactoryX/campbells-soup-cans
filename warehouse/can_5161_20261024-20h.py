"""
Campbell's Soup Can #5161
Produced: 2026-10-24 20:50:55
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# Enable ANSI colors on Windows
if os.name == "nt":
    os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


def slow_print(text, delay=0.02, color=WHITE):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def animate_dots(prefix, count=5, delay=0.35):
    for i in range(count):
        sys.stdout.write(
            "\r" + BOLD + MAGENTA + prefix + "." * (i + 1) + RESET
        )
        sys.stdout.flush()
        time.sleep(delay)
    print()


WOODY = (
    f"{MAGENTA}        _____________{RESET}\n"
    f"{MAGENTA}       /             \\{RESET}\n"
    f"{CYAN}      |   O       O   |{RESET}  <-- me, overthinking\n"
    f"{CYAN}      |       <       |{RESET}\n"
    f"{MAGENTA}       \\     ___     /{RESET}\n"
    f"{MAGENTA}        '-----------'{RESET}\n"
    f"         |     |\n"
    f"        /       \\\n"
)

QUOTE = (
    "I'm not afraid of dying. I'm just afraid of being dead at a party "
    "where everyone else is alive, the music is too loud, and nobody saved me a seat."
)

CLOSING = "— Probably my therapist, if I could afford one."


def main():
    os.system("cls" if os.name == "nt" else "clear")

    animate_dots("Initializing neurotic existential crisis", 5, 0.35)
    print()
    print(WOODY)
    print()

    width = 72
    inner = width - 4

    top = BOLD + CYAN + "╔" + "═" * (width - 2) + "╗" + RESET
    bottom = BOLD + CYAN + "╚" + "═" * (width - 2) + "╝" + RESET
    side = BOLD + CYAN + "║" + RESET

    print(top)
    print(side + " " * inner + side)

    title = " A WOODY ALLEN MOMENT "
    pad_left = max(0, (inner - len(title)) // 2)
    pad_right = inner - len(title) - pad_left
    print(
        side
        + " " * pad_left
        + YELLOW + BOLD + title + RESET
        + " " * pad_right
        + side
    )

    print(side + " " * inner + side)

    # Wrap the quote manually
    words = QUOTE.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= inner:
            line = (line + " " + word).strip()
        else:
            print(side + " " + DIM + WHITE + line.ljust(inner) + RESET + " " + side)
            line = word
    if line:
        print(side + " " + DIM + WHITE + line.ljust(inner) + RESET + " " + side)

    print(side + " " * inner + side)
    print(bottom)
    print()

    slow_print("  " + CLOSING, delay=0.03, color=ITALIC + MAGENTA)
    print()


if __name__ == "__main__":
    main()