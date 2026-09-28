"""
Campbell's Soup Can #5038
Produced: 2026-09-28 15:29:01
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BG_WHITE = "\033[47m"   # white background for box
BG_BLACK = "\033[40m"   # black background for contrast

def typewriter(text, delay=0.05, color=""):
    """Print text with a typewriter effect."""
    for ch in text:
        print(color + ch, end="", flush=True)
        time.sleep(delay)
    print(RESET, end="")

def main():
    # Glowing title
    print(BOLD + YELLOW + "\n  == WOODY'S EXISTENTIAL LAUGH ==\n" + RESET)
    time.sleep(0.5)

    # Decorative box using Unicode block characters
    top = BG_WHITE + "╔════════════════════════════════════════════════╗" + RESET
    middle1 = BG_WHITE + "║ " + CYAN + "\"I'm not afraid of the big bad nothing; I'm just terrified" + BG_WHITE + " ║" + RESET
    middle2 = BG_WHITE + "║ " + CYAN + "that when I get there, everyone's already moved on to the next" + BG_WHITE + " ║" + RESET
    middle3 = BG_WHITE + "║ " + CYAN + "episode of the universe.\"                      " + BG_WHITE + "║" + RESET
    bottom = BG_WHITE + "╚════════════════════════════════════════════════╝" + RESET

    # Print with a slow reveal for drama
    print()
    print(top)
    time.sleep(0.2)
    print(middle1)
    time.sleep(0.2)
    print(middle2)
    time.sleep(0.2)
    print(middle3)
    time.sleep(0.2)
    print(bottom)
    print()

if __name__ == "__main__":
    main()