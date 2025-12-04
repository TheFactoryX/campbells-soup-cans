"""
Campbell's Soup Can #701
Produced: 2025-12-04 04:44:45
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes
CLEAR_SCREEN = "\033[2J\033[H"
RESET = "\033[0m"

# Color palette for gradient
COLORS = ["\033[91m",  # bright red
          "\033[93m",  # bright yellow
          "\033[92m",  # bright green
          "\033[96m",  # bright cyan
          "\033[95m",  # bright magenta
          "\033[94m"]  # bright blue

# The Woody‑Allen‑style quote
QUOTE = ("I keep asking myself why I’m afraid of nothing, "
         "and the answer is, apparently, that even nothing has an attitude.")

# Build an ASCII art box around the quote
border_len = len(QUOTE) + 8
top_border = f"┌{'─' * border_len}┐"
bottom_border = f"└{'─' * border_len}┘"
empty_line = f"│{' ' * border_len}│"

# Spinner animation for a touch of life
spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
spinner_delay = 0.1

def main():
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.flush()

    # Print top border
    sys.stdout.write("\033[96m" + top_border + RESET + "\n")
    sys.stdout.write("\033[96m" + empty_line + RESET + "\n")

    # Animate the quote with color gradient
    for i, ch in enumerate(QUOTE):
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.03)  # Slight delay for a smooth effect

    sys.stdout.write("\n")
    sys.stdout.write("\033[96m" + empty_line + RESET + "\n")
    sys.stdout.write("\033[96m" + bottom_border + RESET + "\n")

    # Spinner animation after the quote
    for _ in range(20):
        for frame in spinner_frames:
            sys.stdout.write("\r" + frame + "  ")
            sys.stdout.flush()
            time.sleep(spinner_delay)

    # Clean up spinner
    sys.stdout.write("\r  \n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
