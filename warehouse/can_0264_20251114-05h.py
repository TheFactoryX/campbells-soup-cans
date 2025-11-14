"""
Campbell's Soup Can #264
Produced: 2025-11-14 05:33:33
Worker: OpenAI: gpt-oss-120b (openai/gpt-oss-120b)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A little neurotic, colorful Woody‑Allen‑style quote with a tiny animation.
"""

import sys
import time

# ANSI colour codes
RESET = "\033[0m"
FG_WHITE = "\033[97m"
FG_YELLOW = "\033[93m"
FG_CYAN = "\033[96m"
FG_MAGENTA = "\033[95m"
BG_BLUE = "\033[44m"
BG_BLACK = "\033[40m"
BOLD = "\033[1m"

# The quote (feel free to replace it with another neurotic gem)
QUOTE = (
    "I think, therefore I'm neurotic – "
    "the only thing I'm absolutely certain of is that "
    "my existence is a series of awkward pauses."
)

# Box dimensions
PAD = 4
BOX_WIDTH = max(len(line) for line in QUOTE.split("\n")) + PAD * 2
TOP = f"{BG_BLUE}{' ' * BOX_WIDTH}{RESET}"
BOTTOM = TOP

def typewriter(text: str, delay: float = 0.03) -> None:
    """Print text one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def colored_boxed_quote():
    # Top border
    print(TOP)

    # Empty line (padding)
    for _ in range(PAD // 2):
        print(f"{BG_BLUE}{' ' * BOX_WIDTH}{RESET}")

    # Quote line(s) – centre‑aligned
    for line in QUOTE.split("\n"):
        padded = line.center(BOX_WIDTH - PAD * 2)
        line_to_print = (
            f"{BG_BLUE}{' ' * PAD}"
            f"{FG_YELLOW}{BOLD}{padded}{RESET}"
            f"{BG_BLUE}{' ' * PAD}{RESET}"
        )
        typewriter(line_to_print, delay=0.01)

    # Empty line (padding)
    for _ in range(PAD // 2):
        print(f"{BG_BLUE}{' ' * BOX_WIDTH}{RESET}")

    # Bottom border
    print(BOTTOM)


if __name__ == "__main__":
    # Clear the screen first (optional, but looks nicer)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print the animated, coloured quote
    colored_boxed_quote()

    # A tiny pause before the program ends, so you can admire the art
    time.sleep(1.5)