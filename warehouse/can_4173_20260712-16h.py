"""
Campbell's Soup Can #4173
Produced: 2026-07-12 16:15:02
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\0 = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def typewriter_no_newline(text: str, color: str = WHITE, delay: float = 0.07) -> None:
    """Print text character by character without adding a newline."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def main() -> None:
    quote = "I don't believe in an afterlife, although I am willing to change my mind after I die."
    # decorative box width based on quote length
    width = len(quote) + 4  # 2 spaces padding each side

    # top border
    print(f"{CYAN}╔{'═' * width}╗{RESET}")
    # left border
    sys.stdout.write(f"{CYAN}║  {RESET}")
    # typewriter effect for the quote
    typewriter_no_newline(quote, color=WHITE, delay=0.06)
    # right border and newline after quote
    print(f"{CYAN}  ║{RESET}")
    # bottom border
    print(f"{CYAN}╚{'═' * width}╝{RESET}")

    # tiny Woody‑Allen‑ish face (optional)
    time.sleep(0.2)
    print(f"\n{MAGENTA}   (̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  {RESET}")

if __name__ == "__main__":
    main()