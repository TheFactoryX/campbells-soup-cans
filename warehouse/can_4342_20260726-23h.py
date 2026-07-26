"""
Campbell's Soup Can #4342
Produced: 2026-07-26 23:13:01
Worker: Ling-3.0-flash (free) (inclusionai/ling-3.0-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GREY = "\033[90m"

def colored(text, color):
    return f"{color}{text}{RESET}"

def slow_print(text, color=WHITE, delay=0.035):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typewriter_effect(line, color=WHITE, speed=0.035):
    for char in line:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_frame(width=62, height=13):
    print()
    cornertl = colored("╭", MAGENTA)
    cornertr = colored("╮", MAGENTA)
    cornerbl = colored("╰", MAGENTA)
    cornerbr = colored("╯", MAGENTA)
    hline = colored("─", MAGENTA)
    vline = colored("│", MAGENTA)

    print(f"{cornertl}{hline * width}{cornertr}")
    for i in range(height):
        stars = "".join([colored("✧", YELLOW) if random.random() > 0.7 else " " for _ in range(width)])
        print(f"{vline}{stars}{vline}")
    print(f"{cornerbl}{hline * width}{cornerbr}")
    print()

def main():
    # Clear-ish separation
    print()
    print(colored("░" * 70, BLUE))
    print()

    # Title
    title = "🧠  WOODY'S COGNITIVE DISCOMFORT  🧠"
    print(colored(" " * 15 + title, CYAN))
    print()

    # Divider
    print(colored("═" * 70, BLUE))
    print()

    # ASCII Art - a little Woody silhouette feel
    art_lines = [
        f"{YELLOW}    ⌐■□/    {RESET}",
        f"{YELLOW}    [o_o]    {RESET}",
        f"{YELLOW}   (_(-_-)_) {RESET}",
        f"{RED}    ~~~~~~~~  {RESET}",
    ]
    for line in art_lines:
        print(colored(" " * 28 + line, YELLOW))
    print()

    # The quote in a box
    quote_width = 56
    print(colored("╔" + "═" * (quote_width) + "╗", MAGENTA))
    print(colored("║", MAGENTA) + " " * quote_width + colored("║", MAGENTA))

    quote = '"I spent the first half of my life trying to'
    quote2 = 'make sense of everything, and the second half'
    quote3 = 'of my life trying to stop making sense —"'
    quote4 = 'and I still can\'t figure out why the toilet'
    quote5 = 'keeps staring back at me with such judgment."'

    quote_lines = [quote, quote2, quote3, quote4, quote5]
    author = "— Woody Allen, probably... after two glasses of wine"

    # Color each line subtly differently
    line_colors = [CYAN, BLUE, GREEN, YELLOW, MAGENTA]
    for line, lc in zip(quote_lines, line_colors):
        padding = quote_width - len(line)
        print(colored("║", MAGENTA) + colored(" " + line, lc) + colored(" " * padding, WHITE) + colored("║", MAGENTA))

    # Empty line
    print(colored("║", MAGENTA) + " " * quote_width + colored("║", MAGENTA))

    # Author line
    auth_padded = f"  {author}"
    auth_padding = quote_width - len(auth_padded)
    print(colored("║", MAGENTA) + colored(" " + author, RED) + colored(" " * auth_padding, WHITE) + colored("║", MAGENTA))

    print(colored("║", MAGENTA) + " " * quote_width + colored("║", MAGENTA))
    print(colored("╚" + "═" * (quote_width) + "╝", MAGENTA))
    print()

    # Divider
    print(colored("═" * 70, BLUE))
    print()

    # Bottom ASCII art fun
    print(colored(" " * 20 + "╱╲", GREEN))
    print(colored(" " * 20 + "│  │", GREEN))
    print(colored(" " * 20 + "╰──╯", GREEN))
    print(colored(" " * 14 + "┌───┐", GREEN))
    print(colored(" " * 14 + "│ 🤔 │", GREEN))
    print(colored(" " * 13 + "└─────┘", GREEN))
    print()

    # Bottom tagline
    slow_print("  " + colored("The existential dread is free.", GREY), GREY, delay=0.05)

    # Footer decoration
    print()
    print(colored("░" * 70, BLUE))
    print()

if __name__ == "__main__":
    main()