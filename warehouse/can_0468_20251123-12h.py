"""
Campbell's Soup Can #468
Produced: 2025-11-23 12:52:43
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
A single-file, pure‑Python program that prints a Woody‑Allen style
philosophical quote with a bit of visual flair using ANSI colors.
"""

import sys
import time

# ANSI escape codes for colors and styles
RESET  = "\033[0m"
BOLD   = "\033[1m"
BLINK  = "\033[5m"
# Foreground colors
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
CYAN   = "\033[96m"

# Quote to be displayed
QUOTE = (
    f"{BOLD}{CYAN}When I think about meaning, "
    f"imagine doing a PhD in existential neuroses, "
    f"it's all just a tiny nitrogen balloon inside a "
    f"turkey brain—enjoy the wobble!{RESET}"
)

# A simple ASCII art frame
FRAME_TOP = f"{MAGENTA}+{'-' * 70}+{RESET}"
FRAME_BOTTOM = f"{MAGENTA}+{'-' * 70}+{RESET}"
FRAME_LEFT = f"{MAGENTA}|{RESET}"
FRAME_RIGHT = f"{MAGENTA}|{RESET}"

# Helper to print with a short delay
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Clear the screen (optional)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print the frame
    slow_print(FRAME_TOP, 0.002)
    for _ in range(2):
        slow_print(f"{FRAME_LEFT} {' ' * 70} {FRAME_RIGHT}", 0.001)
    
    # Animate the quote: fade in from left to right
    quote_lines = QUOTE.split("\n")
    for line in quote_lines:
        # Pad the line to center it inside the frame
        padded = line.center(70)
        # Sliding animation
        for i in range(-70, 1):
            sys.stdout.write("\033[?25l")  # Hide cursor
            sys.stdout.write(f"\r{FRAME_LEFT}{padded[i:i+70]}{FRAME_RIGHT}")
            sys.stdout.flush()
            time.sleep(0.002)
        sys.stdout.write("\n")
    
    # Bottom border
    slow_print(FRAME_BOTTOM, 0.002)
    # Restore cursor visibility
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    main()