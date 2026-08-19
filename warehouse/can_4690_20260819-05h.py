"""
Campbell's Soup Can #4690
Produced: 2026-08-19 05:46:29
Worker: Z.ai: GLM 5.2 (free) (z-ai/glm-5.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
DIM = "\033[2m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def typewriter(text, delay=0.03, color=""):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        # Random tiny jitter for nervous energy
        time.sleep(delay + random.uniform(0, 0.015))
    sys.stdout.write("\n")

def nervous_dots(text, color=""):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\n")

def flicker_word(text, color):
    """Flash a word a couple times before settling."""
    for _ in range(3):
        sys.stdout.write(f"\r{' ' * len(text)}\r")
        time.sleep(0.05)
        sys.stdout.write(f"\r{color}{BOLD}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\n")

def draw_frame(width, color):
    top = f"{color}╔{'═' * width}╗{RESET}"
    bot = f"{color}╚{'═' * width}╝{RESET}"
    print(top)
    print(bot)

def main():
    # Clear screen-ish intro
    print()
    print(f"{DIM}{ITALIC}(The philosopher clears his throat, nervously.){RESET}")
    print()
    time.sleep(0.6)

    # Nervous preamble
    nervous_dots("Hmm...", f"{YELLOW}")
    time.sleep(0.3)
    nervous_dots("Well...", f{YELLOW})
    time.sleep(0.3)
    nervous_dots("Look, I've thought about this a lot,", f"{DIM}")
    time.sleep(0.4)
    nervous_dots("probably more than is healthy,", f"{DIM}")
    time.sleep(0.4)
    nervous_dots("and honestly I...", f"{DIM}")
    time.sleep(0.5)

    print()
    time.sleep(0.4)

    # The big quote, framed and typed dramatically
    quote_lines = [
        f"{BOLD}{CYAN}I've spent my entire life searching for the{RESET}",
        f"{BOLD}{CYAN}meaning of existence, only to discover it{RESET}",
        f"{BOLD}{CYAN}was hiding in my other coat the whole time{RESET}",
        f"{BOLD}{CYAN}— and it shrunk in the wash.{RESET}",
    ]

    max_len = max(len("I've spent my entire life searching for the"),
                  len("meaning of existence, only to discover it"),
                  len("was hiding in my other coat the whole time"),
                  len("— and it shrunk in the wash."))
    box_w = max_len + 6

    # Top border
    print(f"{MAGENTA}╔{'═' * box_w}╗{RESET}")

    # Blank padded line
    print(f"{MAGENTA}║{' ' * box_w}║{RESET}")

    for line in quote_lines:
        # Strip ANSI for length calc, pad visually
        plain = (line
                 .replace(BOLD, "")
                 .replace(CYAN, "")
                 .replace(RESET, ""))
        pad = box_w - len(plain)
        left = pad // 2
        right = pad - left
        sys.stdout.write(f"{MAGENTA}║{' ' * (left + 1)}")
        sys.stdout.flush()
        # Type the content (strip surrounding box so it lands in place)
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.025)
        sys.stdout.write(f"{' ' * (right + 1)}{MAGENTA}║{RESET}\n")

    print(f"{MAGENTA}║{' ' * box_w}║{RESET}")
    print(f"{MAGENTA}╚{'═' * box_w}╝{RESET}")

    print()
    time.sleep(0.5)

    # Flickering attribution
    sys.stdout.write(f"{DIM}{ITALIC}    — A guy who once dropped a philosophy book ")
    sys.stdout.flush()
    time.sleep(0.4)
    flicker_word("in the bathtub", f"{RED}")
    print()
    print()
    time.sleep(0.6)

    # Tiny existential postscript
    nervous_dots("    ...it's fine. Everything's fine.", f"{DIM}")
    time.sleep(0.5)
    nervous_dots("    (It wasn't fine.)", f"{RED}{ITALIC}")
    print()

if __name__ == "__main__":
    main()