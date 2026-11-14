"""
Campbell's Soup Can #5243
Produced: 2026-11-14 22:24:53
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

GRAY = "\033[90m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"

def typing_title(text, color, delay=0.06):
    for ch in text:
        print(f"{color}{BOLD}{ch}", end="", flush=True)
        time.sleep(delay)
    print(f"{RESET}\n")

def typewriter(text, color, delay=0.015):
    line = ""
    for ch in text:
        line += ch
        print(f"{color}{line}\033[2K\r", end="", flush=True)
        time.sleep(delay)
    print(f"{RESET}\n")

def existential_dread():
    print(f"{GRAY}...connecting to the void...{RESET}")
    time.sleep(0.8)

    typing_title("WOODY ALLEN-ISH", YELLOW)

    cloud = r"""
      .-""-.
     /      \
    |        |
    |  o  o  |
    |    ^   |
    |        |
    |        |
     \      /
      '-..-'
    """
    print(f"{CYAN}{cloud}{RESET}")

    quote = "I'm not afraid of dying. I'm just afraid the universe will look back at me and say, 'Really? THIS was the best it ever got?'"

    typewriter(quote, GREEN)

    print(f"{MAGENTA}— a very Woody Allen-ish sentiment{RESET}")

if __name__ == "__main__":
    existential_dread()