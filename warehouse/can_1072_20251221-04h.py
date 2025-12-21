"""
Campbell's Soup Can #1072
Produced: 2025-12-21 04:07:52
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
A playful tiny Python script that prints one Woody‑Allen‑style philosophical quote
with a typewriter animation, colorful framing, and a dash of ASCII flair.
"""

import sys
import time

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[96m"
MAG   = "\033[95m"
YEL   = "\033[93m"

QUOTE = ("I think the meaning of life is a cosmic joke, "
         "and my punchline is that I'm still waiting for the punchline to arrive.")

def typewriter(text: str, delay: float = 0.04):
    """Print text one character at a time with a short delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Title with emojis for extra flair
    title = f"{YEL}🗣️  Woody Allen Quote  🗣️{RESET}"
    print(title + "\n")

    # Prepare a box that fits the quote
    box_width = len(QUOTE) + 4
    border = CYAN + "+" + "-" * (box_width - 2) + "+" + RESET

    # Top of the box
    print(border)

    # Left border, space, colored quote, space, right border
    print(CYAN + "|" + RESET + " " + MAG, end="")
    typewriter(QUOTE)
    print(RESET + " " + CYAN + "|" + RESET)

    # Bottom of the box
    print(border)

    # Small animated flourish: blinking question mark
    for _ in range(4):
        print("\n" + CYAN + "?" + RESET, end="\r")
        time.sleep(0.3)
    print("\n")  # final newline

if __name__ == "__main__":
    main()
