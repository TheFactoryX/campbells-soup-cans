"""
Campbell's Soup Can #3654
Produced: 2026-05-12 09:48:45
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

def typewriter(text: str, delay: float = 0.04, color: str = "\033[93m"):
    """Print text character by character with a slight delay and color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # reset color

def print_boxed_quote():
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "But if I *am* there, I hope they have decent Wi‑Fi so I can stream my own funeral."
    )
    # Prepare lines
    lines = quote.split(". ")
    # Ensure each line ends with a period for nice formatting
    lines = [ln.strip() + ("." if not ln.endswith(".") else "") for ln in lines if ln]

    # Determine width
    max_len = max(len(l) for l in lines)
    width = max_len + 4  # padding inside box

    # Top border
    print("\033[95m" + "╔" + "═" * width + "╗" + "\033[0m")
    # Print each line with typewriter effect
    for line in lines:
        padded = f"  {line.ljust(max_len)}  "
        sys.stdout.write("\033[95m║\033[0m")
        typewriter(padded, delay=0.03, color="\033[96m")
        sys.stdout.write("\033[95m║\033[0m\n")
    # Bottom border
    print("\033[95m" + "╚" + "═" * width + "╝" + "\033[0m")

if __name__ == "__main__":
    print_boxed_quote()