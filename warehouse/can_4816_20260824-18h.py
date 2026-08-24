"""
Campbell's Soup Can #4816
Produced: 2026-08-24 18:59:12
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
CYAN = "\033[36m"
YELLOW = "\033[33m"

def typewriter(text: str, delay: float = 0.05, color: str = "") -> None:
    """Print text character by character with optional color."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main() -> None:
    quote = "I'm not afraid of dying; I just wish the universe had a better Wi‑Fi signal."
    width = len(quote) + 4  # padding inside the box

    # Top border
    sys.stdout.write(CYAN + BOLD + "+" + "-" * (width - 2) + "+" + RESET + "\n")

    # Interior line with typing effect
    inner = "| " + quote + " " * (width - len(quote) - 2) + " |"
    typewriter(inner, delay=0.07, color=YELLOW)

    # Bottom border
    sys.stdout.write(CYAN + BOLD + "+" + "-" * (width - 2) + "+" + RESET + "\n")

if __name__ == "__main__":
    main()