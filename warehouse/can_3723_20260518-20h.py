"""
Campbell's Soup Can #3723
Produced: 2026-05-18 20:45:39
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
RESET = "\033[0m"
BOLD = "\033[1m"
FG_CYAN = "\033[36m"
FG_YELLOW = "\033[33m"
FG_MAGENTA = "\033[35m"

def typewriter_line(line: str, delay: float = 0.04, color: str = RESET):
    """Print a line character by character with optional color."""
    for ch in line:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delta)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    # Woody Allen‑style quote (original)
    quote = "I don't believe in an afterlife, although I am bringing a change of underwear just in case."

    # Decorative face (simple neurotic Woody vibe)
    face = [
        r"      _____      ",
        r"     /     \     ",
        r"    |  o o  |    ",
        r"     \   ^   /    ",
        r"      \ '-' /     ",
        r"       '___'      "
    ]

    # Build a colored box around the quote
    width = len(quote) + 4
    top_border    = "╔" + "═" * width + "╗"
    mid_line      = "║  " + quote + "  ║"
    bottom_border = "╚" + "═" * width + "╝"

    # Typing effect for the face
    for line in face:
        typewriter_line(line, delay=0.02, color=FG_MAGENTA)
    time.sleep(0.2)

    # Typing effect for the box
    typewriter_line(top_border,    delay=0.03, color=FG_CYAN)
    typewriter_line(mid_line,      delay=0.03, color=FG_BOLD + FG_YELLOW)
    typewriter_line(bottom_border, delay=0.03, color=FG_CYAN)

    # Optional: a little flicker to emphasize the quote
    for _ in range(3):
        time.sleep(0.4)
        sys.stdout.write("\033[5m")  # blink
        typewriter_line(mid_line, delay=0.0, color=FG_BOLD + FG_YELLOW)
        sys.stdout.write("\033[25m") # stop blink
        time.sleep(0.4)

if __name__ == "__main__":
    main()