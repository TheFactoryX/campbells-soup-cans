"""
Campbell's Soup Can #4115
Produced: 2026-07-07 05:06:57
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A tiny, color‑bursting Woody‑Allen‑style quote shooter

import sys
import time
import random

# ANSI colour codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
YELLOW  = "\033[93m"

# ------------------------------------------------------------------
# Helper to print a string character‑by‑character for a little “typing” effect.
def typewriter(text: str, delay: float = 0.04) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ------------------------------------------------------------------
# Create a padded, coloured box around any text
def boxed(text: str, border_colour: str = CYAN) -> None:
    lines = text.splitlines()
    width  = max(len(line) for line in lines)
    top    = f"{border_colour}┌{'─' * (width + 2)}┐{RESET}"
    bot    = f"{border_colour}└{'─' * (width + 2)}┘{RESET}"
    print(top)
    for line in lines:
        print(f"{border_colour}│ {line.ljust(width)} │{RESET}")
    print(bot)

# ------------------------------------------------------------------
# A little “brain” that pulses while we build the quote
def pulse_brain(duration: float = 2.0) -> None:
    brain = [
        "    __",
        "  /'  '.",
        " | _    |",
        "(| (_)  |)",
        " '.___.'",
    ]
    frames = len(brain)
    start = time.time()
    while time.time() - start < duration:
        idx = random.randint(0, frames - 1)
        sys.stdout.write("\r" + YELLOW + BOLD + brain[idx] + RESET)
        sys.stdout.flush()
        time.sleep(0.15)
    print("\r" + " " * 20, end='\r')  # clear line

# ------------------------------------------------------------------
def main() -> None:
    # Animate the “neurotic” brain
    pulse_brain()

    # The funny Woody‑Allen‑style quote
    quote = (
        "I think I come to this world\n"
        "with too much angst and not enough coffee,\n"
        "and that’s why the Universe hires a psychiatrist."
    )

    # Box it up in a splash of colour
    boxed(quote, border_colour=CYAN)

    # A little cherry‑on‑top confession
    typewriter("\n" + MAGENTA + BOLD + "— Woody Allen (imagined)")

if __name__ == "__main__":
    main()
