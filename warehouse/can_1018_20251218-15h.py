"""
Campbell's Soup Can #1018
Produced: 2025-12-18 15:37:50
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, colorful Woody‑Allen‑style philosophical quote.
Runs with plain Python and ANSI escape codes.
"""

import sys
import time
import random

# ANSI escape codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
COLORS  = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]

def animate_char(char: str, delay: float = 0.04) -> None:
    """Print a single character in a random color and wait a short time."""
    sys.stdout.write(f"{random.choice(COLORS)}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(delay)

def animate_text(text: str, delay: float = 0.04) -> None:
    """Animate an entire string, character by character."""
    for ch in text:
        animate_char(ch, delay)
    sys.stdout.write("\n")

def build_speech_bubble(text: str) -> None:
    """Print an ASCII speech bubble around the quoted text."""
    lines = [line.strip() for line in text.split(".") if line.strip()]
    longest = max(len(line) for line in lines) + 2  # padding
    border = f"  {'-' * longest}"
    print(f"\033[33m{border}\033[0m")                      # top
    for line in lines:
        padded = line.ljust(longest)
        print(f"\033[33m  |{padded}|\033[0m")            # middle
    print(f"\033[33m  {'-' * longest}\033[0m")          # bottom

def main() -> None:
    # Header
    header = f"{BOLD}💭 Woody Allen says:{RESET}\n"
    print(header, end="")

    # The quote
    quote = (
        "I went to school to learn philosophy, but the curriculum was "
        "full of existential dread and overdue pizza.  "
        "Now I realize that the only thing I can truly guarantee is "
        "that I will still be here, complaining, while everyone else "
        "has already vanished into some cosmic void."
    )

    # Visual bubble
    build_speech_bubble(quote)

    # Animated, colorful quote
    print("\nNow, watching the words appear in a rainbow of colors:\n")
    animate_text(quote)

if __name__ == "__main__":
    main()