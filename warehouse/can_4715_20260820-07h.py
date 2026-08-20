"""
Campbell's Soup Can #4715
Produced: 2026-08-20 07:56:54
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI color codes
COLORS = [31, 32, 33, 34, 35, 36, 37]  # red, green, yellow, blue, magenta, cyan, white

def color_text(text, color):
    return f"\033[{color}m{text}\033[0m"

def typewriter(text, delay=0.04):
    for ch in text:
        sys.stdout.write(color_text(ch, random.choice(COLORS)))
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Woody‑Allen‑style quote
    quote = "I think the universe is a cosmic joke, and I'm the punchline that keeps asking why."

    # Border dimensions
    width = len(quote) + 4  # two spaces on each side
    border = color_text("=" * width, 33)  # yellow border

    # Print top border
    print(border)

    # Print quote with typewriter effect inside borders
    sys.stdout.write(color_text("|  ", 32))  # green left border
    typewriter(quote, delay=0.04)
    sys.stdout.write(color_text("  |", 32))  # green right border
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Print bottom border
    print(border)

    # Simple blinking cursor animation
    for _ in range(6):
        sys.stdout.write("\033[?25l")  # hide cursor
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\033[?25h")  # show cursor
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    main()
