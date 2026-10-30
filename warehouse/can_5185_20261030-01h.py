"""
Campbell's Soup Can #5185
Produced: 2026-10-30 01:00:09
Worker: Free Models Router (openrouter/free)
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

class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def type_text(text, color=C.WHITE, delay=0.05):
    for ch in text:
        sys.stdout.write(color + ch + C.RESET)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.03))

def nervous_loader():
    phrases = [
        "Calibrating neurosis",
        "Loading existential dread",
        "Searching for missing socks",
        "Contacting therapist",
    ]
    phrase = random.choice(phrases)
    for i in range(25):
        dots = "." * (i % 4)
        sys.stdout.write(f"\r{C.YELLOW}{C.BOLD}{phrase}{dots}{C.RESET}   ")
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()

def main():
    nervous_loader()
    print()

    width = 60
    print(C.MAGENTA + C.BOLD + "┌" + "─" * width + "┐" + C.RESET)

    lines = [
        "I'm not afraid of death. I'm just afraid of",
        "being dead at a party I didn't want to attend,",
        "in shoes that pinch, with no therapist on speed dial.",
    ]

    for line in lines:
        sys.stdout.write(C.CYAN + C.BOLD + "│" + C.RESET)
        type_text(line.center(width), C.WHITE, 0.06)
        sys.stdout.write(C.CYAN + C.BOLD + "│" + C.RESET + "\n")
        time.sleep(0.2)

    print(C.MAGENTA + C.BOLD + "└" + "─" * width + "┘" + C.RESET)
    print()

    face_colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.MAGENTA]
    face = [
        "      _____________      ",
        "     /             \     ",
        "    |  (O)   (O)    |    ",
        "    |       <       |    ",
        "    |     \___/     |    ",
        "     \_____________/     ",
    ]
    for i, row in enumerate(face):
        sys.stdout.write(face_colors[i % len(face_colors)] + C.BOLD + row + C.RESET + "\n")
        time.sleep(0.1)

    print()
    type_text("           — Woody Allen (probably, mid-panic attack)", C.YELLOW, 0.03)
    print()
    sys.stdout.write(
        C.RED + C.BOLD +
        "   (Disclaimer: No parties, shoes, or therapists were harmed in the making of this quote.)"
        + C.RESET + "\n"
    )

if __name__ == "__main__":
    main()