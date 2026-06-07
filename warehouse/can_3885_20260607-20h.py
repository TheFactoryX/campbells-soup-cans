"""
Campbell's Soup Can #3885
Produced: 2026-06-07 20:37:41
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, delay=0.03):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def print_boxed_quote():
    quote = [
        "I don't want to achieve immortality through my work;",
        "I want to achieve it by not showing up to my own funeral."
    ]

    width = max(len(line) for line in quote) + 4  # padding inside box
    top_bottom = f"{CYAN}{BOLD}╔{'═' * (width-2)}╗{RESET}"
    middle = f"{CYAN}{BOLD}║{RESET}"
    bottom = f"{CYAN}{BOLD}╚{'═' * (width-2)}╝{RESET}"

    # Animate the box drawing
    typewriter(top_bottom, delay=0.005)
    time.sleep(0.1)

    for line in quote:
        padded = f" {line:<{width-2}} "
        sys.stdout.write(f"{CYAN}{BOLD}║{RESET} ")
        typewriter(padded, delay=0.04)
        sys.stdout.write(f" {CYAN}{BOLD}║{RESET}")
        print()
        time.sleep(0.1)

    typewriter(bottom, delay=0.005)

    # A tiny Woody‑Allen‑ish doodle (just for fun)
    doodle = [
        "          .-. ",
        "         (o o) ",
        "          | | ",
        "         '   ' ",
        "        /| ||\\",
        "       // | | \\\\",
        "      //  | |  \\\\",
        "     //   | |   \\\\",
        "    //____| |____\\\\",
        "   /_____________\\"
    ]
    print()
    for line in doodle:
        sys.stdout.write(MAGENTA)
        typewriter(line, delay=0.02)
        sys.stdout.write(RESET)
        time.sleep(0.05)

if __name__ == "__main__":
    print_boxed_quote()