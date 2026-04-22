"""
Campbell's Soup Can #3404
Produced: 2026-04-22 19:40:55
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

def typewriter(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = "I'm not afraid of the void; I'm just terrified that the void is judging me."
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    width = len(quote) + 4  # padding for spaces and box chars
    top    = f"{CYAN}╔{'═' * width}╗{RESET}"
    middle = f"{CYAN}║ {YELLOW}{quote}{CYAN} ║{RESET}"
    bottom = f"{CYAN}╚{'═' * width}╝{RESET}"

    typewriter(top,    0.001)
    typewriter(middle, 0.001)
    typewriter(bottom, 0.001)

if __name__ == "__main__":
    main()