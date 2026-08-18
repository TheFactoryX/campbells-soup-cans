"""
Campbell's Soup Can #4663
Produced: 2026-08-18 01:50:33
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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

def colored(text, code):
    """Wrap text with ANSI escape codes for color."""
    return f"\033[{code}m{text}\033[0m"

def slow_print(text, delay=0.05, color=None):
    """Print character by character for a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch if color else ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote_box(lines, border_color="1;35", text_color="1;33"):
    """Draw a colored box around the quote lines with animation."""
    width = max(len(l) for l in lines) + 4
    border = "+" + "-" * width + "+"
    slow_print(colored(border, border_color))
    for line in lines:
        slow_print(colored(f"| {line.ljust(width-2)} |", text_color))
    slow_print(colored(border, border_color))

# ASCII Art (Woody's face)
art = [
    "   _________   ",
    "  /         \\  ",
    " |  O    O  | ",
    " |   ~ ^ ~   | ",
    "  \\  '-'   /  ",
    "   '_____'"
]

for row in art:
    print(colored(row, "1;36"))

# Quote lines – one philosophical Woody‑Allan‑style quote
quote_lines = [
    "I am terrified of death, but I have",
    "written my own obituary in perfect rhyme,",
    "so at least the verses will outlive me."
]

# Display the quote in an animated, colorful box
print_quote_box(quote_lines)

# Optional attribution
print(colored("\n— Woody Allen (maybe)", "0;90"))