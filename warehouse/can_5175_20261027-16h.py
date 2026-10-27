"""
Campbell's Soup Can #5175
Produced: 2026-10-27 16:39:50
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
import random

# Enable ANSI escape sequences on Windows terminals
os.system('')

# ANSI color palette
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'


def slow_print(text, delay=0.04, color=WHITE):
    """Typewriter-style printing with color."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def neurotic_loading():
    """Simulate an existential calculation."""
    thoughts = [
        "Consulting inner child...",
        "Scheduling appointment with dread...",
        "Checking under the bed for meaning...",
        "Calculating the odds of happiness...",
        "Waiting for the universe to text back...",
    ]
    for thought in thoughts:
        sys.stdout.write(f"\r{MAGENTA}{BOLD}{thought}{RESET}")
        sys.stdout.flush()
        time.sleep(0.55)
    print("\n")


def print_neurotic_face():
    """Tiny ASCII Woody Allen having a moment."""
    face = f"""
{CYAN}
       ___   ___
     /'   `\/   `\
    | (o)   (o) |  <-- existential crisis
    |     <     |
     \  ---  /
      `-----'
       |   |
       |___|
{RESET}
"""
    print(face)


QUOTE = (
    "I don't want to achieve immortality through my work. "
    "I want to achieve it by not dying, preferably while wearing clean underwear."
)


def wrap_text(text, width):
    """Simple word wrap for the quote box."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= width - 4:
            current = (current + " " + word).strip()
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    width = 70

    print(f"{YELLOW}{BOLD}{'=' * width}{RESET}")
    print(f"{MAGENTA}{BOLD}   WOODY ALLEN'S EXISTENTIAL THOUGHT OF THE DAY{RESET}".center(width))
    print(f"{YELLOW}{BOLD}{'=' * width}{RESET}\n")

    neurotic_loading()
    print_neurotic_face()

    # Quote box
    top = f"{CYAN}┌{'─' * (width - 2)}┐{RESET}"
    bottom = f"{CYAN}└{'─' * (width - 2)}┘{RESET}"

    print(top)
    for line in wrap_text(QUOTE, width):
        padded = line.ljust(width - 4)
        print(f"{CYAN}│ {RESET}{BOLD}{WHITE}{padded}{RESET}{CYAN} │{RESET}")
    print(bottom)
    print()

    slow_print("— Woody Allen (probably, while in therapy)", delay=0.03, color=GREEN)
    print()
    print(f"{RED}* sighs neurotically *{RESET}")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Abandoning existence mid-thought. Wise choice.{RESET}")
        sys.exit(0)