"""
Campbell's Soup Can #5187
Produced: 2026-10-30 14:09:27
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
import random
import os

# Enable ANSI escape codes on Windows terminals
if os.name == "nt":
    os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def typewriter(text, color=RESET, delay=0.04):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def neurotic_twitch():
    faces = ["(¬_¬ )", "(╯°□°)╯", "(•_•)>⌐■-■", "(╯︵╰,)", "(◕‿◕)", "(っ˘̩╭╮˘̩)っ"]
    for _ in range(10):
        face = random.choice(faces)
        sys.stdout.write(f"\r{CYAN}{face}  accessing neurotic core...{RESET}   ")
        sys.stdout.flush()
        time.sleep(random.uniform(0.07, 0.17))
    print()


def main():
    clear_screen()

    print(MAGENTA + BOLD + "╔" + "═" * 58 + "╗" + RESET)
    print(
        MAGENTA
        + BOLD
        + "║"
        + " " * 5
        + "WOODY ALLEN-STYLE EXISTENTIAL GENERATOR"
        + " " * 6
        + "║"
        + RESET
    )
    print(MAGENTA + BOLD + "╚" + "═" * 58 + "╝" + RESET)
    print()

    neurotic_twitch()
    time.sleep(0.3)

    quote_lines = [
        "I don't want to achieve immortality through my work.",
        "I want to achieve it by not dying.",
        "The universe is 13.8 billion years old, indifferent,",
        "and I'm already late for my own existence.",
    ]
    attribution = "— Woody Allen (probably, and in therapy)"

    box_width = 60

    print(CYAN + "┌" + "─" * box_width + "┐" + RESET)
    for line in quote_lines:
        print(CYAN + "│ " + YELLOW + line.ljust(box_width - 2) + CYAN + " │" + RESET)
        time.sleep(0.25)
    print(CYAN + "├" + "─" * box_width + "┤" + RESET)
    print(CYAN + "│ " + MAGENTA + BOLD + attribution.center(box_width - 2) + CYAN + " │" + RESET)
    print(CYAN + "└" + "─" * box_width + "┘" + RESET)
    print()

    typewriter(GREEN + "(⊙_⊙)  I have a feeling this isn't going to end well." + RESET, delay=0.03)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "Aborted by existential dread." + RESET)