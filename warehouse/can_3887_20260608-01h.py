"""
Campbell's Soup Can #3887
Produced: 2026-06-08 01:34:08
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

# Woody Allen‑style quote (original)
quote = '"I am not afraid of death, I just don\'t want to be there when it happens."'

def box(text, color):
    """Return a colored boxed version of text."""
    inner = f"|  {text}  |"
    border = "+" + "-" * (len(inner) - 2) + "+"
    return (
        f"{color}{border}{RESET}\n"
        f"{color}{inner}{RESET}\n"
        f"{color}{border}{RESET}"
    )

def typewriter(text, delay=0.04):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def animate_quote():
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for _ in range(2):  # two cycles
        for col in colors:
            sys.stdout.write("\033[2J\033[H")  # clear screen, move cursor home
            sys.stdout.write(box(quote, col))
            sys.stdout.flush()
            time.sleep(0.6)

    # final display in white with a slight typewriter effect inside the box
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(box(quote, WHITE))
    sys.stdout.flush()
    # optionally, type the quote inside the box for extra flair
    inner = f"|  {quote}  |"
    border = "+" + "-" * (len(inner) - 2) + "+"
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(f"{WHITE}{border}{RESET}\n")
    sys.stdout.write(f"{WHITE}|  ")
    typewriter(quote, 0.05)
    sys.stdout.write(f"{WHITE}  |{RESET}\n")
    sys.stdout.write(f"{WHITE}{border}{RESET}\n")

if __name__ == "__main__":
    animate_quote()