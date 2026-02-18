"""
Campbell's Soup Can #2303
Produced: 2026-02-18 21:49:59
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ----------------------------------------------------------------------
# Woody‑Allen‑style philosophical quote
# ----------------------------------------------------------------------
QUOTE = "I think, therefore I’m anxious about thinking."

# ----------------------------------------------------------------------
# ANSI colour codes (no external libraries required)
# ----------------------------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"

# ----------------------------------------------------------------------
# Box‑drawing characters (Unicode)
# ----------------------------------------------------------------------
TL = "╔"
TR = "╗"
BL = "╚"
BR = "╝"
HL = "═"
VL = "║"

# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04, colour: str = CYAN) -> None:
    """Print `text` one character at a time, coloured."""
    for ch in text:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def print_boxed_quote() -> None:
    """Print the quote inside a coloured ASCII box."""
    pad = 2                              # spaces on each side of the quote
    width = len(QUOTE) + pad * 2         # inner width of the box

    # top border
    sys.stdout.write(YELLOW + TL + HL * width + TR + RESET + "\n")
    # empty line
    sys.stdout.write(YELLOW + VL + " " * width + VL + RESET + "\n")

    # quote line – left border, padding, typewriter, trailing spaces, right border
    sys.stdout.write(YELLOW + VL + RESET + " " * pad)
    typewriter(QUOTE, delay=0.03, colour=CYAN)
    trailing = width - len(QUOTE) - pad
    sys.stdout.write(" " * trailing + YELLOW + VL + RESET + "\n")

    # empty line
    sys.stdout.write(YELLOW + VL + " " * width + VL + RESET + "\n")
    # bottom border
    sys.stdout.write(YELLOW + BL + HL * width + BR + RESET + "\n")

def thinking_animation(cycles: int = 3, delay: float = 0.5) -> None:
    """Simple “thinking…” animation before the reveal."""
    for i in range(cycles):
        dots = "." * (i + 1) + " " * (cycles - i - 1)
        sys.stdout.write(BOLD + CYAN + dots + RESET + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    # clear the line
    sys.stdout.write("\r" + " " * cycles + "\r")

def main() -> None:
    thinking_animation()
    print_boxed_quote()

if __name__ == "__main__":
    main()