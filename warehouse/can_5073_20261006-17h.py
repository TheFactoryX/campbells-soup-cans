"""
Campbell's Soup Can #5073
Produced: 2026-10-06 17:11:26
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

def color(code):
    """Return ANSI escape sequence for the given color code."""
    return f"\033[{code}m"

def printc(text, code, end='\n'):
    """
    Print text with the specified color code.
    Supports custom end parameter (default newline).
    """
    sys.stdout.write(color(code) + text + color(0))
    if end:
        sys.stdout.write(end)
    sys.stdout.flush()

def box_print(quote, width=70, border_color='1;33', text_color='1;32', delay=0.04):
    """
    Display the quote inside a colorful ASCII box with a typing effect.
    - width: minimum box width (characters between borders)
    - border_color: ANSI code for the box border
    - text_color: ANSI code for the quote text
    - delay: time (seconds) between character prints
    """
    # Split the quote into lines and trim trailing spaces
    lines = [line.rstrip() for line in quote.split('\n')]
    # Determine actual width (at least the requested width, but long enough for all lines)
    actual_width = max(width, max(len(line) for line in lines))

    # Top border
    printc('╔' + '═' * actual_width + '╗', border_color)

    for line in lines:
        padded = line.ljust(actual_width)   # pad with spaces to reach width

        # Left border (instant)
        printc('║', border_color, end='')

        # Type out each character of the padded line
        for ch in padded:
            printc(ch, text_color, end='')
            time.sleep(delay)

        # Right border (instant, with newline)
        printc('║', border_color)

    # Bottom border
    printc('╚' + '═' * actual_width + '╝', border_color)

# Woody‑ish Allen‑style philosophical quote (split across multiple lines for readability)
quote = """I don't worry about the meaning of life.
I worry about the Wi‑Fi signal in my brain.
It's patchy, and I can't even stream my thoughts without buffering.
— Woody‑ish Allen"""

# Render the quote with colors, box, and a playful typing animation
box_print(quote, width=70, border_color='1;33', text_color='1;32', delay=0.04)