"""
Campbell's Soup Can #5143
Produced: 2026-10-21 10:09:45
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens - the ultimate commitment issue."
    width = len(quote) + 4  # account for "║ " and " ║"
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    print("\033[31m" + top + "\033[0m")
    print("\033[33m" + "║ " + quote + " ║" + "\033[0m")
    print("\033[31m" + bottom + "\033[0m")
    art = r"""
   .-""""-.
  / -   -  \
 |  .-. .- |
 |  \o| |o/
  \   ^   /
   '-...-'
"""
    print("\033[35m" + art + "\033[0m")
    print("\033[32m" + "- Woody Allen (probably)" + "\033[0m")

if __name__ == "__main__":
    main()