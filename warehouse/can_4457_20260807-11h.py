"""
Campbell's Soup Can #4457
Produced: 2026-08-07 11:08:22
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

# Woody Allen‑style quote (original)
QUOTE = (
    "I'm not afraid of the unknown; I'm just terrified of the known "
    "and the fact that I probably misunderstood it anyway."
)

# ANSI bright colors
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

RESET = "\033[0m"


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def draw_quote(start_idx: int):
    """Print the quote inside a cyan box with a typewriter effect and cycling colors."""
    clear_screen()
    width = len(QUOTE) + 4  # +2 for spaces, +2 for borders
    # Cyan for the box
    sys.stdout.write("\033[96m")
    sys.stdout.write("+" + "-" * width + "+\\n")
    sys.stdout.write("| ")
    # Typewriter effect with rotating colors
    for i, ch in enumerate(QUOTE):
        color = COLORS[(start_idx + i) % len(COLORS)]
        sys.stdout.write(f"{color}{ch}")
        sys.stdout.flush()
        time.sleep(0.03)  # typing speed
    # Close the line in cyan
    sys.stdout.write(f"{RESET}\033[96m |\\n")
    sys.stdout.write("+" + "-" * width + "+\\n")
    sys.stdout.write(RESET)
    sys.stdout.flush()


def main():
    clear_screen()
    # Animate a few cycles with different starting colors
    for cycle in range(5):
        draw_quote(cycle * 4)  # shift start index each round
        time.sleep(0.7)        # pause between cycles
    # Final static version in white for a clean finish
    clear_screen()
    width = len(QUOTE) + 4
    sys.stdout.write("\033[97m")  # White
    sys.stdout.write("+" + "-" * width + "+\\n")
    sys.stdout.write("| " + QUOTE + " |\\n")
    sys.stdout.write("+" + "-" * width + "+\\n")
    sys.stdout.write(RESET)
    sys.stdout.flush()


if __name__ == "__main__":
    main()