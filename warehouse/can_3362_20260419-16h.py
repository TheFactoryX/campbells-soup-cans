"""
Campbell's Soup Can #3362
Produced: 2026-04-19 16:57:43
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def main():
    # Clear the terminal
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # ANSI color codes (bright colors)
    colors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
    ]
    reset = "\033[0m"

    # Woody Allen‑style quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens, "
        "and I also don't want to miss the last episode of my favorite show."
    )

    # Top decorative border
    border_top = "╔" + "═" * (len(quote) + 2) + "╗"
    sys.stdout.write(colors[0] + border_top + reset + "\n")
    time.sleep(0.1)

    # Typewriter effect with rainbow colors
    for i, ch in enumerate(quote):
        color = colors[i % len(colors)]
        sys.stdout.write(color + ch + reset)
        sys.stdout.flush()
        time.sleep(0.03)  # typing speed

    sys.stdout.write("\n")
    time.sleep(0.1)

    # Bottom decorative border
    border_bottom = "╚" + "═" * (len(quote) + 2) + "╝"
    sys.stdout.write(colors[0] + border_bottom + reset + "\n")
    sys.stdout.flush()

    # A tiny Woody Allen‑esque face (glasses & neurotic vibe)
    face = r"""
      (\_/)
      ( •_•)
      / >👓
    """
    for line in face.splitlines():
        if line.strip():
            sys.stdout.write(colors[2] + line + reset + "\n")
        else:
            sys.stdout.write(line + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()