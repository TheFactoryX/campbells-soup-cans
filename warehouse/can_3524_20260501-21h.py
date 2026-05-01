"""
Campbell's Soup Can #3524
Produced: 2026-05-01 21:07:46
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
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Woody Allen‑style quote (one philosophical nugget)
quote = "I'm not afraid of dying; I just don't want to be there when it happens, especially if there's no Wi‑Fi."

# Padding inside the box
padding = 2
inner_width = len(quote) + 2 * padding

# Top/bottom border
border = f"{CYAN}{BOLD}+{'-' * inner_width}+{RESET}"

# Simple neurotic face (just for fun)
face = f"{CYAN}{BOLD}   >_<   {RESET}"

def typewriter_line(text, color):
    """Print text with a typewriter effect, applying the given color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)  # tweak speed here
    sys.stdout.write(RESET)

def main():
    # Show a goofy face
    print(face)
    # Top border
    print(border)
    # Left border, padding, then animated quote, then padding, right border
    sys.stdout.write(f"{CYAN}{BOLD}|{RESET}")
    sys.stdout.write(" " * padding)
    typewriter_line(quote, YELLOW + BOLD)
    sys.stdout.write(" " * padding)
    sys.stdout.write(f"{CYAN}{BOLD}|{RESET}\n")
    # Bottom border
    print(border)

if __name__ == "__main__":
    main()