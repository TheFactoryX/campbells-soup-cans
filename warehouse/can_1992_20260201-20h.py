"""
Campbell's Soup Can #1992
Produced: 2026-02-01 20:43:04
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import itertools
import random

# ANSI escape codes
RESET   = "\x1b[0m"
BOLD    = "\x1b[1m"
MAGENTA = "\x1b[35m"
YELLOW  = "\x1b[33m"
BLACK   = "\x1b[30m"

# Woody‑Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be on the Wi‑Fi when the universe goes dark."

WIDTH = 80  # interior width of the quote box

def spinner():
    """A simple loading spinner."""
    spinner_chars = itertools.cycle(['-', '\\', '|', '/'])
    for _ in range(15):
        sys.stdout.write(f"\rLoading Woody Allen quote...{next(spinner_chars)}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.10, 0.20))
    sys.stdout.write("\rLoading Woody Allen quote... done\n")

def draw_box(width: int, text: str) -> None:
    """Print a colourful box around the quote and reveal the text char by char."""
    # Top border
    top = f"{MAGENTA}╔{YELLOW}{'═'*width}{RESET}╗"
    sys.stdout.write(top + "\n")
    # Placeholder line (all spaces)
    placeholder = f"{MAGENTA}║{YELLOW}{' '*width}{RESET}║"
    sys.stdout.write(placeholder + "\n")
    # Bottom border
    bottom = f"{MAGENTA}╚{YELLOW}{'═'*width}{RESET}╝"
    sys.stdout.write(bottom + "\n")

    # Reveal the quote character by character
    for idx, ch in enumerate(text):
        sys.stdout.write(
            f"\r{MAGENTA}║{YELLOW}{text[:idx]}{RESET}{' '*(width-idx)}{RESET}║"
        )
        sys.stdout.flush()
        time.sleep(random.uniform(0.08, 0.12))

    # Final line with the full quote and trailing spaces
    spaces = " " * (width - len(text))
    sys.stdout.write(
        f"\r{MAGENTA}║{YELLOW}{text}{RESET}{spaces}{MAGENTA}║\n"
    )

def main() -> None:
    # Clear screen (optional, works on most terminals)
    print("\x1b[2J\x1b[H")
    
    # Engaging animation
    spinner()
    
    # Bold header
    header = f"{BOLD}{MAGENTA}W O O D Y A L L E N{RESET}"
    sys.stdout.write(header + "\n")
    time.sleep(0.5)
    
    # The philosophically funny quote
    draw_box(WIDTH, quote)

if __name__ == "__main__":
    main()