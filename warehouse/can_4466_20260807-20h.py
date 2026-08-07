"""
Campbell's Soup Can #4466
Produced: 2026-08-07 20:58:37
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
CYAN = "\033[36m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def typewriter(text: str, delay: float = 0.05) -> None:
    """Print text character‑by‑character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main() -> None:
    quote = "I'm not afraid of dying; I just don't want to be there when the universe cancels my subscription."
    width = len(quote) + 4  # padding inside the box

    top_border = f"{CYAN}┌{'─' * width}┐{RESET}"
    bottom_border = f"{CYAN}└{'─' * width}┘{RESET}"

    # Top border
    print(top_border)

    # Left border + space
    sys.stdout.write(f"{CYAN}│ {RESET}")
    # Animated quote in yellow
    typewriter(f"{YELLOW}{quote}{RESET}")
    # Right border + newline
    sys.stdout.write(f"{CYAN} │{RESET}\n")

    # Bottom border
    print(bottom_border)

if __name__ == "__main__":
    main()