"""
Campbell's Soup Can #799
Produced: 2025-12-08 16:44:51
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

CLEAR = "\033[H\x1b[J"  # ANSI escape to clear the console
QUOTE = ("I'm not afraid of death; I'm afraid of the mystery of death. "
         "I'm terrified of the taproom draft there. Just in case.")

def blink_quote():
    colors = [
        "\033[46;30m",  # Green background, black text - calm
        "\033[41;37m",  # Red background, white text - alert
        "\033[45;37m",  # Magenta background, white text - dramatic
        "\033[43;30m",  # Yellow background, black text - serious
    ]
    blink = "\033[5m"  # ANSI blink code
    index = 0

    while True:
        sys.stdout.write(CLEAR)
        color = colors[index % len(colors)]
        msg = color + QUOTE + "\033[0m"  # Reset color after quote
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.1)

        # Optional: blink with color change
        sys.stdout.write(CLEAR)
        if index % 3 == 0:
            sys.stdout.write(blink + color + QUOTE + "\033[0m")
        else:
            sys.stdout.write("\033[46;30m" + QUOTE + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)

        index += 1

if __name__ == "__main__":
    blink_quote()