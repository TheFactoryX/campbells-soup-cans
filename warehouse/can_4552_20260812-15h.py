"""
Campbell's Soup Can #4552
Produced: 2026-08-12 15:14:11
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def sleep_print(text, color="", delay=0.05):
    """Print text character by character with ANSI color."""
    for ch in text:
        sys.stdout.write(f"\033[{color}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line after the text

def main():
    # ANSI color codes
    YELLOW = "1;33"
    CYAN = "1;36"
    GREEN = "1;32"

    # Clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Whimsical ASCII header (colored)
    header = (
        f"\033[{CYAN}m"
        "   .-'''-.   \n"
        "  /   _   \\  \n"
        " |   (o)   | \n"
        "  \\   ^   /  \n"
        "   `---'   \n"
        f"\033[0m"
    )
    print(header)

    # The philosophical quote (typewriter effect)
    quote = f"\033[{YELLOW}m\"I am not afraid of death; I just don't want to be there when it happens.\"\033[0m"
    sleep_print(quote, YELLOW, 0.03)

    # Attribution
    attribution = f"\033[{GREEN}m   — Woody Allen\033[0m"
    sleep_print(attribution, GREEN, 0.03)

    # Sparkle footer
    footer = f"\033[{CYAN}m   🌟✨🌟✨🌟  \033[0m"
    sleep_print(footer, CYAN, 0.03)

if __name__ == "__main__":
    main()