"""
Campbell's Soup Can #4960
Produced: 2026-09-14 06:18:02
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

def typewriter(text, delay=0.06):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def main():
    # Woody Allen‑style quote (original)
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens. "
        "Besides, the afterlife probably has terrible Wi‑Fi."
    )

    # ANSI color codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    # Top border
    print(f"{MAGENTA}╔{'═' * 58}╗{RESET}")

    # Quote with typewriter effect, colored
    sys.stdout.write(f"{YELLOW}║ {RESET}")
    typewriter(quote, 0.05)
    sys.stdout.write(f"{YELLOW}║{RESET}")
    # Move cursor back to start of line to re‑print the closing border later
    # (the typewriter already printed a newline, so we just print the border)

    # Bottom border
    print(f"{MAGENTA}╚{'═' * 58}╝{RESET}")

if __name__ == "__main__":
    main()