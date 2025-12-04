"""
Campbell's Soup Can #708
Produced: 2025-12-04 11:30:53
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
A playful, colorfully animated Woody Allen‑style philosophical quote.
"""

import sys
import time
import random

# ANSI escape codes for colours and styles
CSI = "\033["

RESET = CSI + "0m"
BOLD = CSI + "1m"
DIM = CSI + "2m"
RED = CSI + "31m"
YELLOW = CSI + "33m"
CYAN = CSI + "36m"
MAGENTA = CSI + "35m"
GREEN = CSI + "32m"

# The Woody Allen‑style quote
QUOTE = (
    "I don't think anything is a function of why I became... "
    "just a neurotic, light‑bulb‑hanging, coffee‑drinking in an alley thing."
)

# Key fragments to underline with trembling highlight
KEYWORDS = ["neurotic", "light‑bulb‑hanging", "coffee‑drinking", "alley"]

def typewriter(text, speed=0.04, colour=YELLOW):
    """Print text one character at a time, with optional colour."""
    for ch in text:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)

def flash_bg(text, times=2, delay=0.2, colour=CYAN):
    """Flash the background colour of a line of text."""
    for _ in range(times):
        sys.stdout.write(colour + text + RESET + "\r")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(" " * len(text) + "\r")
        sys.stdout.flush()
        time.sleep(delay)

def replace_keywords(text, pattern, repl):
    """Replace specific words with colourful, trembling versions."""
    for word in pattern:
        if word in text:
            sleep = lambda: time.sleep(random.uniform(0.05, 0.15))
            # Build trembling effect
            tremor = ""
            for ch in word:
                tremor += (DIM if random.random() < 0.5 else "") + ch + RESET
            text = text.replace(word, tremor)
    return text

def display_boxed_text(text, border_char="="):
    """Display the text surrounded by a coloured box."""
    border = border_char * (len(text) + 4)
    print(RED + border + RESET)
    print(RED + border_char + " " + text + " " + border_char + RESET)
    print(RED + border + RESET)

def animated_stars(width, height=5, delay=0.05):
    """Simple starfield animation above the quote."""
    for _ in range(height):
        row = ""
        for _ in range(width):
            row += "*" if random.random() < 0.08 else " "
        print(GREEN + row + RESET)
        time.sleep(delay)

if __name__ == "__main__":
    # Clear screen
    sys.stdout.write(CSI + "2J" + CSI + "H")
    sys.stdout.flush()

    # Build colourful, trembling quote
    colourful_quote = replace_keywords(QUOTE, KEYWORDS, CYAN)

    # Starfield intro
    ascii_width = len(QUOTE) + 4
    animated_stars(ascii_width)

    # Flash the quote background for drama
    flash_bg(RESET + colourful_quote + RESET, times=3, delay=0.15, colour=MAGENTA)

    # Typewriter effect in bold + cyan
    typewriter("\n" + BOLD, speed=0.02)  # blink
    typewriter("\n")
    typewriter(colour=CYAN)
    typewriter(colour=CYAN, speed=0.06, text=colourful_quote)
    print(RESET)

    # Box the quote
    display_boxed_text(QUOTE)