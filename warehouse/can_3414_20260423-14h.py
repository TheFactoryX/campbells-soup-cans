"""
Campbell's Soup Can #3414
Produced: 2026-04-23 14:12:09
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
COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, delay=0.03, color="") -> None:
    """Print text character by character with optional color."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    quote = (
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it by never losing my keys again."
    )

    # Box dimensions
    lines = quote.splitlines()
    max_len = max(len(line) for line in lines)
    width = max_len + 4  # padding
    horiz = "═" * (width - 2)

    # Top border
    sys.stdout.write(f"{BOLD}{COLORS[2]}╔{horiz}╗{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.1)

    # Quote lines with typewriter effect
    for line in lines:
        padded = f"  {line.ljust(max_len)}  "
        sys.stdout.write(f"{BOLD}{COLORS[4]}║{RESET}")
        typewriter(padded, delay=0.04, color=COLORS[5])
        time.sleep(0.05)

    # Bottom border
    sys.stdout.write(f"{BOLD}{COLORS[2]}╚{horiz}╝{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # Optional final flicker
    for _ in range(3):
        sys.stdout.write(f"\033[5m{BOLD}{COLORS[0]}  Think about it...  {RESET}\033[0m")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\033[2K\r")  # clear line
        sys.stdout.flush()
        time.sleep(0.4)

if __name__ == "__main__":
    main()