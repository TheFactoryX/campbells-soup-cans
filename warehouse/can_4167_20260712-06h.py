"""
Campbell's Soup Can #4167
Produced: 2026-07-12 06:45:58
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

def main():
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens."
    )
    width = len(quote) + 4
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    colors = [
        "\033[91m",  # red
        "\033[93m",  # yellow
        "\033[92m",  # green
        "\033[96m",  # cyan
        "\033[95m",  # magenta
    ]

    # Top border with a tiny delay for effect
    for ch in top_bottom:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    # Two empty inner lines
    for _ in range(2):
        sys.stdout.write("║")
        sys.stdout.flush()
        time.sleep(0.02)
        for _ in range(width - 2):
            sys.stdout.write(" ")
            sys.stdout.flush()
            time.sleep(0.005)
        sys.stdout.write("║\n")
        sys.stdout.flush()
        time.sleep(0.02)

    # Quote line, character‑by‑character color cycling
    sys.stdout.write("║  ")
    sys.stdout.flush()
    time.sleep(0.02)
    for i, ch in enumerate(quote):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("  ║\n")
    sys.stdout.flush()
    time.sleep(0.02)

    # Two more empty inner lines
    for _ in range(2):
        sys.stdout.write("║")
        sys.stdout.flush()
        time.sleep(0.02)
        for _ in range(width - 2):
            sys.stdout.write(" ")
            sys.stdout.flush()
            time.sleep(0.005)
        sys.stdout.write("║\n")
        sys.stdout.flush()
        time.sleep(0.02)

    # Bottom border
    for ch in top_bottom:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

if __name__ == "__main__":
    main()