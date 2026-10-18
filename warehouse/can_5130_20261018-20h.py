"""
Campbell's Soup Can #5130
Produced: 2026-10-18 20:44:36
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"

def typewriter(text, delay=0.03, color=""):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def draw_box(text, width=60):
    """Draw an ASCII box around the text."""
    lines = text.split("\n")
    max_len = max([len(line) for line in lines])
    line_len = min(max_len, width - 4)
    # Top border
    print(BOLD + CYAN + "┌" + "─" * (line_len + 2) + "┐" + RESET)
    for line in lines:
        # Pad line to width
        padded_line = line.ljust(line_len)
        print(BOLD + CYAN + "│" + RESET + " " + padded_line + " " + BOLD + CYAN + "│" + RESET)
    # Bottom border
    print(BOLD + CYAN + "└" + "─" * (line_len + 2) + "┘" + RESET)

def main():
    # Title with some fun
    print(BOLD + MAGENTA + "🎭 Woody's Existential Ramblings 🎭" + RESET)
    print()

    # Quote in Woody Allen style
    quote = (
        f"{BOLD}{YELLOW}“{RESET} {CYAN}I'm not afraid of death; I just don't want to be there when the universe "
        f"decides to hit the reset button and accidentally erase my Wi‑Fi password.{RESET} {BOLD}{YELLOW}”{RESET}"
    )

    # Print with typewriter effect
    print()
    typewriter(quote, delay=0.05, color=GREEN)

    print()
    # Optional ASCII art (e.g., a thinking dude)
    art = (
        "   " + GREEN + "/\\   " + RESET + "\n"
        "  " + GREEN + "( o ) " + RESET + "\n"
        "   " + GREEN + "╲╱   " + RESET
    )
    draw_box(art)

if __name__ == "__main__":
    main()