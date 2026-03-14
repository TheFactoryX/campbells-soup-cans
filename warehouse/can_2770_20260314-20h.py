"""
Campbell's Soup Can #2770
Produced: 2026-03-14 20:45:48
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
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"

def slow_print(text, delay=0.03):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    quote = (
        "I’m convinced that the secret to happiness is low expectations… "
        "which explains why I’m still waiting for my cat to apologize "
        "for knocking over my plant."
    )

    # Add padding inside the box
    padded = f"  {quote}  "
    width = len(padded)

    # Top border
    print(f"{MAGENTA}{BOLD}┌{'─' * (width - 2)}┐{RESET}")

    # Left border, then quote with typing effect, then right border
    sys.stdout.write(f"{MAGENTA}{BOLD}│{RESET}")
    slow_print(padded, delay=0.04)
    sys.stdout.write(f"{MAGENTA}{BOLD}│{RESET}\n")

    # Bottom border    print(f"{MAGENTA}{BOLD}└{'─' * (width - 2)}┘{RESET}")

if __name__ == "__main__":
    main()