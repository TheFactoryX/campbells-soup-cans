"""
Campbell's Soup Can #4633
Produced: 2026-08-16 17:33:34
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def type_line(line, color):
    for ch in line:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # newline after the line

def draw_box(title, quote_lines):
    width = max(len(title), max((len(l) for l in quote_lines), default=0)) + 4
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    print(top)
    # Title line
    title_line = "║ " + title.center(width - 4) + " ║"
    print(title_line)
    print("║" + " " * (width - 2) + "║")
    for line in quote_lines:
        padded = "║ " + line.ljust(width - 4) + " ║"
        print(padded)
    print("║" + " " * (width - 2) + "║")
    print(bottom)

def woody_ascii():
    # Simple Woody‑Allen‑like neurotic face
    face = [
        "   _____   ",
        "  /     \\  ",
        " |  o o  | ",
        " |   ^   | ",
        " |  '-'  | ",
        "  \\_____/  "
    ]
    for line in face:
        print("\033[93m" + line + RESET)  # yellow for the face

def main():
    clear_screen()
    woody_ascii()
    print()  # space

    title = "A Woody Allen‑style Thought"
    quote = [
        "I don't fear the void; I fear that the void has Wi‑Fi",
        "and I forgot the password."
    ]

    # Choose a random color for each line of the quote
    colored_quote = [random.choice(COLORS) + line + RESET for line in quote]

    # Draw a fancy box around the quote
    draw_box(title, quote)

    # Now animate the quote inside the box with typing effect
    print("\n" + "\033[96m" + "Typing it out, because anticipation is half the neurosis..." + RESET)
    time.sleep(0.5)
    for line, color in zip(quote, colored_quote):
        type_line(line, color)
        time.sleep(0.3)

    # Final flourish
    print("\n" + "\033[95m" + "Remember: existential dread is just a bad Wi‑Fi signal away." + RESET)

if __name__ == "__main__":
    main()