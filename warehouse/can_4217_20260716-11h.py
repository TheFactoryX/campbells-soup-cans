"""
Campbell's Soup Can #4217
Produced: 2026-07-16 11:53:51
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
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

# ANSI color codes
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

quote = (
    "I told my analyst that life is meaningless, and he said, "
    "\"Yes, but try to enjoy the meaningless\n"
    "  parts before the meaningless parts kill you.\" "
    "So I bought a bagel. The bagel was also meaningless,\n"
    "  but at least it was round, which felt oddly spiritual."
)

def type_text(text, delay=0.012, color=YELLOW):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(lines, color):
    width = max(len(l) for l in lines) + 4
    top = color + "╔" + "═" * width + "╗" + RESET
    bottom = color + "╚" + "═" * width + "╝" + RESET
    print(top)
    for line in lines:
        pad = width - len(line) - 2
        print(color + "║ " + RESET + line + " " * pad + color + " ║" + RESET)
    print(bottom)

def main():
    # Title animation
    title = "WOODY ALLEN'S EXISTENTIAL BAGEL"
    for i in range(len(title) + 1):
        sys.stdout.write("\r" + BOLD + BLUE + title[:i] + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

    # Blinking subtitle
    for _ in range(3):
        sys.stdout.write("\r" + RED + BOLD + "  a philosophical thought  " + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + DIM + "  a philosophical thought  " + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

    # Typewriter quote
    print(GREEN + BOLD + "🎭 The Quote:" + RESET)
    time.sleep(0.5)
    type_text(quote, delay=0.01, color=YELLOW)

    # Boxed summary
    time.sleep(0.5)
    draw_box(
        [
            "CONCLUSION:",
            "  Death is just the universe's way of saying",
            "  \"You talk too much. Go home.\"",
            "  But home is also meaningless. So stay here.",
        ],
        color=RED,
    )

    # Final wiggle
    for _ in range(2):
        sys.stdout.write("\r" + BLUE + "   ~ fin ~   " + RESET)
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write("\r" + YELLOW + "   ~ fin ~   " + RESET)
        sys.stdout.flush()
        time.sleep(0.25)
    print(RESET)

if __name__ == "__main__":
    main()