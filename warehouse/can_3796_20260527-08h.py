"""
Campbell's Soup Can #3796
Produced: 2026-05-27 08:48:28
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
BOLD = "\033[1m"
RESET = "\033[0m"

def type_writer(text: str, delay: float = 0.07) -> None:
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main() -> None:
    # Woody Allen‑style quote (original)
    quote = "I’m not pessimistic; I’m just well‑informed about how badly everything will go."

    # Build the box components
    inner_width = len(quote) + 4  # space for "║ " and " ║"
    top_border    = f"{CYAN}{BOLD}╔{'═'*inner_width}╝{RESET}"
    bottom_border = f"{CYAN}{BOLD}╚{'═'*inner_width}╝{RESET}"
    # The line we will animate (includes colours)
    inner_line    = f"{CYAN}{BOLD}║ {YELLOW}{quote}{CYAN} ║{RESET}"

    # Display
    print(top_border)
    type_writer(inner_line, delay=0.06)
    print(bottom_border)

if __name__ == "__main__":
    main()