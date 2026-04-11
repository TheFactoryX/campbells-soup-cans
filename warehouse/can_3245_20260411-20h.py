"""
Campbell's Soup Can #3245
Produced: 2026-04-11 20:51:03
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
A single-file, pure‑Python program that prints a whimsical Woody Allen‑style
philosophical quote with a touch of color and animation.
"""

import sys
import time
import math

# ANSI escape codes for colors and effects
RESET   = "\u001b[0m"
BOLD    = "\u001b[1m"
ITALIC  = "\u001b[3m"
BLINK   = "\u001b[5m"
RAISE   = "\u001b[21m"
GREEN   = "\u001b[32m"
CYAN    = "\u001b[36m"
YELLOW  = "\u001b[33m"

# The quote: self‑deprecating, existential, Woody Allen‑ish
QUOTE = (
    f"{RAISE}{BOLD}{GREEN}“I’m terrified of the big deep blue thing that’s like my "
    f"future, but why’d I ever think I could outwit it?{RESET}”"
)

# ASCII art: a slow‑scrolling lightbulb to simulate "idea" flashing
LIGHTBULB = [
    "     .-''''-.",
    "   .'  |   `. ",
    "  :    )    ;",
    "  |   /   _/|",
    "  :  :    |  ;",
    "  `. :   .` |",
    "   `-.__.-` ",
    "      ||    ",
    "      ||    ",
    "      ||    ",
    "      ||    ",
    "      ||    ",
    "      ||    ",
    "     _||_   ",
]

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\u001b[2J\u001b[H")
    sys.stdout.flush()

def animate_lightbulb():
    """Fade a lightbulb in and out using an alpha ramp."""
    alpha_cycle = [0, 0.15, 0.3, 0.45, 0.6, 0.8, 1.0, 0.8, 0.6, 0.45, 0.3, 0.15, 0]
    for alpha in alpha_cycle:
        clear_screen()
        # Draw the lightbulb with varying brightness
        bright = int(alpha * 255)
        color = f"\u001b[38;2;{bright};{bright};{bright}m"
        for line in LIGHTBULB:
            sys.stdout.write(color + line + "\n")
        sys.stdout.flush()
        time.sleep(0.12)

def draw_boxed_quote():
    """Print the quote inside a stylized ASCII box with colors."""
    lines = QUOTE.strip().split("\n")
    width = max(len(line) for line in lines) + 4
    border = YELLOW + "+" + "-" * width + "+" + RESET
    print(border)
    for line in lines:
        padded = line.ljust(width - 2)
        print(YELLOW + "|" + RESET + f"  {padded}  " + YELLOW + "|" + RESET)
    print(border)

def main():
    # Intro animation
    animate_lightbulb()
    # Clear screen one last time
    clear_screen()
    # Present the quote in a fancy box
    draw_boxed_quote()
    # Pause briefly
    time.sleep(2)

if __name__ == "__main__":
    main()