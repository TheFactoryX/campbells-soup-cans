"""
Campbell's Soup Can #4548
Produced: 2026-08-12 08:39:15
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
RESET = "\033[0m"

def color_code(n):
    return f"\033[{n}m"

def typewriter(text, delay=0.07):
    for ch in text:
        sys.stdout.write(color_code(random.choice(COLORS)) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def print_border(width, color=36):
    line = color_code(color) + "=" * width + RESET
    sys.stdout.write(line + "\n")
    sys.stdout.flush()

def main():
    quote = "I think the universe is a cosmic joke, and I'm the punchline that keeps asking why."
    width = len(quote) + 4  # padding for borders

    # Top border
    print_border(width, color=36)

    # Left border
    sys.stdout.write(color_code(36) + "| " + RESET)
    sys.stdout.flush()

    # Quote with typewriter effect
    typewriter(quote, delay=0.07)

    # Right border
    sys.stdout.write(color_code(36) + " |\n" + RESET)
    sys.stdout.flush()

    # Bottom border
    print_border(width, color=36)

if __name__ == "__main__":
    main()
