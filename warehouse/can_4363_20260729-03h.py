"""
Campbell's Soup Can #4363
Produced: 2026-07-29 03:40:37
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, random

def main():
    quote = "I'm not pessimistic; I'm just well-informed about how badly things will go."
    # decorative box
    border = "╔" + "═" * (len(quote) + 4) + "╗"
    bottom = "╚" + "═" * (len(quote) + 4) + "╝"
    colors = [91, 92, 93, 94, 95, 96, 97]  # bright ANSI colors

    # clear screen and move cursor home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # top border
    print("\033[96m" + border + "\033[0m")
    # left side of box
    print("\033[96m║ \033[0m", end="")
    # typewriter effect with random colors per character
    for ch in quote:
        color = random.choice(colors)
        sys.stdout.write(f"\033[{color}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    # right side of box
    print("\033[96m ║\033[0m")
    # bottom border
    print("\033[96m" + bottom + "\033[0m")
    # footer
    print("\033[93m\" - Woody Allen (probably)\"\033[0m")

if __name__ == "__main__":
    main()