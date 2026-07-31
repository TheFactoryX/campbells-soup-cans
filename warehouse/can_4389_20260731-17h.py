"""
Campbell's Soup Can #4389
Produced: 2026-07-31 17:52:02
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

quote = (
    "I’m not afraid of death; I just don’t want to be there when it happens."
)

def color_for_index(i):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    return colors[i % len(colors)]

def type_animated(text, delay=0.03):
    for i, ch in enumerate(text):
        sys.stdout.write(color_for_index(i) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def boxed_print(lines, color):
    width = max(len(l) for l in lines) + 4
    border = color + '═' * width + RESET
    print(color + border + RESET)
    for line in lines:
        padded = f" {line} ".ljust(width - 2)
        print(color + f"│{padded}│" + RESET)
    print(color + border + RESET)

def main():
    # Fancy intro
    intro = "Press Enter for some existential wisdom..."
    for ch in intro:
        sys.stdout.write(color_for_index(ord(ch) % 6) + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write('\n')
    input()

    # Print the quote in a colorful box
    lines = quote.split(';')
    boxed_print(lines, MAGENTA)
    # Add a little bouncing heart animation
    heart = RED + '♥' + RESET
    for _ in range(3):
        sys.stdout.write(heart)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b' + heart)
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == '__main__':
    main()