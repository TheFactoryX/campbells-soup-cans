"""
Campbell's Soup Can #1960
Produced: 2026-01-31 08:47:36
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody's Wisdom: a tiny animated quote in the style of Woody Allen

import time, os

# ANSI colors
RED   = "\033[91m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
BOLD  = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(txt, delay=0.05):
    """Print txt character by character with a short pause."""
    for ch in txt:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def print_woody_ascii():
    """Print Woody Allen’s silhouette letter by letter."""
    ascii_art = [
        "   _____   ",
        "  /______\\ ",
        " (\\___/\\   )",
        "   \\____/  ",
        "   ( O )   ",
        "   \\_/    "
    ]
    for line in ascii_art:
        typewriter(line, delay=0.03)

def animate_box(quote_text):
    width = 80
    inner_width = width - 2
    red   = RED
    green = GREEN
    border_char = f"{red}╔{RESET}"
    vertical_char = f"{red}║{RESET}"

    # top border
    print(border_char + "═"*width + f"{red}╗{RESET}")

    for line in quote_text.splitlines():
        if not line:
            print(vertical_char + " " * inner_width + vertical_char)
            continue

        # centre line inside inner area
        pad = (inner_width - len(line)) // 2
        inner = list(" " * inner_width)

        for idx, ch in enumerate(line):
            inner[idx + pad] = ch
            # gradually reveal the line
            print(f"{green}{vertical_char}{''.join(inner)}{vertical_char}{RESET}",
                  end='\r', flush=True)
            time.sleep(0.03)

        print()                     # advance to next line

    # bottom border
    print(f"{red}╚" + "═"*width + f"{red}╝{RESET}")

def main():
    clear_screen()
    print_woody_ascii()
    time.sleep(0.7)

    # Woody Allen‑style philosophical quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens."""
    animate_box(quote)

if __name__ == "__main__":
    main()