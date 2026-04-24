"""
Campbell's Soup Can #3431
Produced: 2026-04-24 19:13:08
Worker: inclusionAI: Ling-2.6-flash (free) (inclusionai/ling-2.6-flash:free)
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
import random

# ANSI color codes
class Colors:
    CYAN    = '\033[36m'
    MAGENTA = '\033[35m'
    YELLOW  = '\033[33m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    BLUE    = '\033[34m'
    WHITE   = '\033[37m'
    BOLD    = '\033[1m'
    RESET   = '\033[0m'
    BG_BLUE = '\033[44m'
    BG_PINK = '\033[45m'

# Woody Allen style quote
quote = (
    "I’m not scared of death; I just don’t want to be there "
    "when the Wi‑Fi drops and the coffee goes cold."
)

# Tiny ASCII brain
brain_art = [
    "        (\\__/) ",
    "        (•ㅅ•) ",
    "        /  V  \\ ",
    "       /       \\ ",
    "      |  EXISTENTIAL  | ",
    "       \\  DREAD  / ",
    "        \\       / ",
    "         )     ( ",
    "         (     ) ",
    "    ||---||   ||---|| ",
]

def type_print(text, delay=0.03):
    """Typewriter effect with color cycling."""
    colors = [Colors.CYAN, Colors.MAGENTA, Colors.YELLOW, Colors.WHITE, Colors.GREEN]
    for i, ch in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.01))
    print(Colors.RESET)

def draw_box(lines, width=60, pad=2):
    """Draw a framed box around the quote."""
    margin = ' ' * pad
    h_line = Colors.BOLD + Colors.CYAN + '╔' + '═' * (width - 2) + '╗' + Colors.RESET
    print(h_line)
    for line in lines:
        content = line.center(width)
        print(Colors.BOLD + Colors.CYAN + '║' + Colors.RESET + margin + content + margin + Colors.BOLD + Colors.CYAN + '║' + Colors.RESET)
    print(h_line)

def main():
    # Clear screen with a color splash
    print(Colors.BG_BLUE + Colors.WHITE + "\n" * 20 + " " * 40 + "Loading Woody…\n" + Colors.RESET)
    time.sleep(0.5)

    # Animate brain art with color shifts
    for i, line in enumerate(brain_art):
        colored = ""
        for ch in line:
            if ch in "()\\/|":
                colored += Colors.BG_PINK + Colors.BOLD + ch + Colors.RESET
            elif ch in "EXISTENTIAL":
                colored += Colors.RED + ch
            elif ch in " DREAD ":
                colored += Colors.YELLOW + ch
            else:
                colored += Colors.CYAN + ch
            time.sleep(0.05)
        print(colored.center(60))
    time.sleep(0.7)

    # Box the quote with typewriter effect
    print("\n")
    draw_box([quote], width=70, pad=3)

    # Fade-in final flourish
    print("\n" + Colors.BOLD + Colors.WHITE + "        — Woody Allen, probably —" + Colors.RESET)

    # Subtle blink on the quote
    for _ in range(2):
        time.sleep(0.4)
        print('\033[F\033[J', end='')  # cursor up & clear line
        draw_box([quote], width=70, pad=3)
        time.sleep(0.2)

    print(Colors.BG_BLUE + Colors.WHITE + "\n" * 10 + " " * 30 + "Existential crisis resolved.\n" + Colors.RESET)

if __name__ == "__main__":
    main()