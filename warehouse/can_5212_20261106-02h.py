"""
Campbell's Soup Can #5212
Produced: 2026-11-06 02:26:26
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[96m"
C_MAGENTA = "\033[95m"
C_YELLOW = "\033[93m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"

QUOTE = (
    "I don't want to achieve immortality through my work. "
    "I want to achieve it by not dying — preferably while lying down, "
    "in a well-lit room, with my analyst on speed dial."
)

def slow_print(text, delay=0.04, color=C_RESET):
    for ch in text:
        sys.stdout.write(color + ch + C_RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_neurotic_head():
    art = [
        f"{C_CYAN}      .-----------.{C_RESET}",
        f"{C_CYAN}     /             \\{C_RESET}",
        f"{C_CYAN}    |  O       O    |{C_RESET}",
        f"{C_CYAN}    |       <       |{C_RESET}",
        f"{C_CYAN}    |   \\   ^   /   |{C_RESET}",
        f"{C_CYAN}     \\   -------   /{C_RESET}",
        f"{C_CYAN}      '-----------'{C_RESET}",
        f"{C_MAGENTA}         (overthinking){C_RESET}"
    ]
    for line in art:
        print(line)
        time.sleep(0.04)

def main():
    print()
    draw_neurotic_head()
    print()

    # Decorative box
    print(C_YELLOW + C_BOLD + "╔" + "═" * 58 + "╗" + C_RESET)
    print(C_YELLOW + C_BOLD + "║" + "  A WOODY ALLEN-STYLE PHILOSOPHICAL MOMENT".center(58) + "║" + C_RESET)
    print(C_YELLOW + C_BOLD + "╚" + "═" * 58 + "╝" + C_RESET)
    print()

    # Typewriter effect for the quote
    slow_print(QUOTE, delay=0.035, color=C_GREEN)

    print()
    print(C_MAGENTA + "   ~ Existential dread, served with a side of bagels ~" + C_RESET)
    print()

if __name__ == "__main__":
    main()