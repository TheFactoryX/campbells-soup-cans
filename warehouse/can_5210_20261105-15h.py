"""
Campbell's Soup Can #5210
Produced: 2026-11-05 15:28:02
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def clear_screen():
    print("\033[2J\033[H", end="")

def print_color(text, color, bold=False):
    if bold:
        print(f"\033[1;{color}m{text}\033[0m")
    else:
        print(f"\033[{color}m{text}\033[0m")

def main():
    clear_screen()
    time.sleep(0.2)
    print_color("   ( (", 33)
    print_color("    ) )", 33)
    print_color("   ( (", 33)
    print_color("  (       )", 33)
    print_color(" ( (_____) )", 33)
    print_color("", 33)
    print("\033[0m")
    time.sleep(0.5)
    print_color("THE MEANING OF LIFE?", 35, bold=True)
    time.sleep(0.5)
    quote = "I'm not afraid of the void; I'm just afraid I'll run out of coffee before I get there."
    print_color("WOODY SAYS:", 31, bold=True)
    time.sleep(0.5)
    print_color('"', 93)
    for ch in quote:
        print(f"\033[93m{ch}\033[0m", end='', flush=True)
        time.sleep(0.04)
    print()
    print_color('"\n', 93)
    time.sleep(0.5)
    print_color("And that's the truth, as I remember it.", 32)

if __name__ == "__main__":
    main()