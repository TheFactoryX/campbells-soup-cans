"""
Campbell's Soup Can #5023
Produced: 2026-09-25 18:37:20
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def main():
    part1 = "I’m not afraid of dying; I just don’t want to be there"
    part2 = "when it happens – the waiting room is always full of people who think they have time."
    top    = color("╔════════════════════════════════════════════════════════════════╗", "33")
    bottom = color("╚════════════════════════════════════════════════════════════════╝", "33")
    line1  = color("║  ", "33") + color(part1, "35") + color("  ║", "33")
    line2  = color("║  ", "33") + color(part2, "35") + color("  ║", "33")
    for line in (top, line1, line2, bottom):
        print(line)
        time.sleep(0.07)

if __name__ == "__main__":
    main()