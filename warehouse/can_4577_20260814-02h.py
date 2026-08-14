"""
Campbell's Soup Can #4577
Produced: 2026-08-14 02:45:58
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

def clear():
    sys.stdout.write("\x1b[H\x1b[J")  # clear screen
    sys.stdout.flush()

def c(text, col):
    return f"\x1b[{col}m{text}\x1b[0m"

def main():
    clear()
    # Fancy header
    print(c("*" * 40, "33"))               # yellow
    time.sleep(0.2)

    # Top border of the box (cyan)
    print(c("╔" + "═" * 38 + "╗", "36"))
    time.sleep(0.1)

    # The Woody Allen quote (yellow)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print(c(f"║   {quote}   ", "33"))
    time.sleep(0.2)

    # Bottom border of the box (cyan)
    print(c("╚" + "═" * 38 + "╝", "36"))
    time.sleep(0.1)

    # Fancy footer
    print(c("*" * 40, "33"))               # yellow
    time.sleep(2)                         # let it linger

if __name__ == "__main__":
    main()