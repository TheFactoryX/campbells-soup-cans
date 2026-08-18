"""
Campbell's Soup Can #4670
Produced: 2026-08-18 08:53:15
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

COLORS = [31,32,33,34,35,36,37]
RESET = '\033[0m'

def color_char(c):
    return f'\033[{random.choice(COLORS)}m{c}{RESET}'

def typewriter(text, delay=0.05):
    for c in text:
        sys.stdout.write(color_char(c))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_border(width=80, delay=0.01):
    line = '=' * width
    for c in line:
        sys.stdout.write(f'\033[35m{c}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    ascii_art = [
        "   .-\"\"\"\"-.",
        "  /        \\\\",
        " |  O  O   |",
        r" |   /\    |",
        r"  \  --   /",
        "   '-..-'"
    ]
    for art_line in ascii_art:
        typewriter(art_line, delay=0.02)

    quote = "I think the universe is a cosmic joke, and I'm the punchline that keeps asking why."
    width = 85
    print_border(width)
    padding = (width - len(quote) - 2) // 2
    line = '|' + ' ' * padding + quote + ' ' * (width - len(quote) - padding - 2) + '|'
    typewriter(line, delay=0.02)
    print_border(width)

if __name__ == "__main__":
    main()
