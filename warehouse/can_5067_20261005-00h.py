"""
Campbell's Soup Can #5067
Produced: 2026-10-05 00:55:59
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Crisis Machine
A single Python file — no external dependencies, pure ANSI magic.
"""

import time
import sys


class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    BG_BLACK = '\033[40m'


def slow_print(text, color="", delay=0.025):
    """Typewriter effect with ANSI colors."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def draw_box(color, width=62):
    h_line = "═" * (width - 2)
    print(color + "╔" + h_line + "╗" + Colors.RESET)


def draw_box_close(color, width=62):
    h_line = "═" * (width - 2)
    print(color + "╚" + h_line + "╝" + Colors.RESET)


def main():
    w = 62

    # ── Opening: existential preamble ──
    print("\n" * 2)
    draw_box(Colors.CYAN + Colors.BOLD, w)
    print(Colors.CYAN + Colors.BOLD + "║" + " " * (w - 2) + "║" + Colors.RESET)
    slow_print(Colors.CYAN + Colors.BOLD + "║   🎬  WOODY ALLEN'S THOUGHTS ON EXISTENCE  🎬  ║", Colors.CYAN + Colors.BOLD, 0.015)
    print(Colors.CYAN + Colors.BOLD + "║" + " " * (w - 2) + "║" + Colors.RESET)
    draw_box_close(Colors.CYAN + Colors.BOLD, w)
    print()
    time.sleep(0.4)

    # ── The neurotic setup ──
    draw_box(Colors.YELLOW, w)
    print(Colors.YELLOW + "║" + Colors.RESET, end="")
    slow_print(" I've been in psychoanalysis for 17 years and all I've learned", Colors.WHITE, 0.018)

    print(Colors.YELLOW + "║" + Colors.RESET, end="")
    slow_print(" is that the universe is completely indifferent, my neurosis is", Colors.WHITE, 0.018)

    print(Colors.YELLOW + "║" + Colors.RESET, end="")
    slow_print(" genetic, and my fear of commitment extends to breakfast cereal.", Colors.WHITE, 0.018)
    draw_box_close(Colors.YELLOW, w)
    print()
    time.sleep(0.3)

    # ── THE QUOTE ──
    draw_box(Colors.RED + Colors.BOLD, w)
    print(Colors.RED + Colors.BOLD + "║" + Colors.RESET, end="")
    slow_print("  \"I don't want to achieve immortality through my work;", Colors.WHITE, 0.02)

    print(Colors.RED + Colors.BOLD + "║" + Colors.RESET, end="")
    slow_print("   I want to achieve it through not dying.\"", Colors.WHITE, 0.02)

    print(Colors.RED + Colors.BOLD + "║" + Colors.RESET)
    draw_box_close(Colors.RED + Colors.BOLD, w)
    print()
    time.sleep(0.4)

    # ── Woody face (ASCII art) ──
    print(Colors.MAGENTA)
    slow_print("         _____", Colors.MAGENTA, 0.01)
    slow_print("        /     \\___", Colors.MAGENTA, 0.01)
    slow_print("       |  O   O  |", Colors.MAGENTA, 0.01)
    slow_print("       |    ^    |", Colors.MAGENTA, 0.01)
    slow_print("       |  \\___/  |", Colors.MAGENTA, 0.01)
    slow_print("        \\_______/", Colors.MAGENTA, 0.01)
    print(Colors.RESET)
    print()

    # ── Bonus punchline ──
    draw_box(Colors.GREEN + Colors.ITALIC, w)
    print(Colors.GREEN + Colors.ITALIC + "║" + Colors.RESET, end="")
    slow_print(" Life is full of misery, loneliness, and suffering —", Colors.WHITE, 0.018)

    print(Colors.GREEN + Colors.ITALIC + "║" + Colors.RESET, end="")
    slow_print(" and it's all over much too soon. (Also, the Wi-Fi is terrible.)", Colors.WHITE, 0.018)
    draw_box_close(Colors.GREEN + Colors.ITALIC, w)
    print()

    # ── Footer ──
    time.sleep(0.5)
    print(Colors.DIM + "  ── Somewhere in the Bronx, a therapist is weeping softly ──" + Colors.RESET)
    print(Colors.DIM + "  ── Analysis bill: $1,200/hr. Existential dread: priceless ──" + Colors.RESET)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Colors.RED + "  Too existential even for Woody. Exiting..." + Colors.RESET)
        sys.exit(0)