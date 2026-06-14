"""
Campbell's Soup Can #3932
Produced: 2026-06-14 10:31:50
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, random

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def main():
    quote = "I don't believe in an afterlife, but I do bring a spare pair of socks just in case."
    colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]  # ANSI foreground colors
    width = len(quote) + 2  # padding for left/right spaces
    top_border = "╔" + "═" * width + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    print(color(top_border, 36))  # cyan border
    # typewriter effect with random colors
    for ch in quote:
        sys.stdout.write(color(ch, random.choice(colors)))
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # newline after the quote
    print(color(bottom_border, 36))

if __name__ == "__main__":
    main()