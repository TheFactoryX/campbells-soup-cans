"""
Campbell's Soup Can #4428
Produced: 2026-08-04 03:37:04
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

def type_line(line, delay=0.05):
    """Print a line character by character to simulate typing."""
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # Eye‑catching title
    title = f"{YELLOW}{BOLD}Woody's Paradoxical Proverb{RESET}"
    print(title.center(80))
    print()

    # Decorative separator line
    decor = f"{CYAN}{'═' * 80}{RESET}"
    print(decor)

    # The quote (Woody‑style: neurotic, self‑deprecating, existential humor)
    quote = ("Life is a tragicomedy. I'm the curtain‑keeper while the play "
             "was being written. I don't fear death; I just don't want to "
             "be there when the lights go out.")

    # Box dimensions
    width = 80

    # Box borders
    top_border = f"╔{'═' * width}╗"
    bottom_border = f"╚{'═' * width}╝"
    line_inside = f"║ {CYAN}{quote}{RESET} ║"

    # Print the box with a typing animation
    type_line(top_border)
    type_line(line_inside)
    type_line(bottom_border)

    # Gentle closing flourish
    print(f"{GREEN}✨ End of Woody's wisdom ✨{RESET}")

if __name__ == "__main__":
    main()