"""
Campbell's Soup Can #4174
Produced: 2026-07-12 17:27:45
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# ASCII art box with colored Woody-Allen style philosophical quote

# ANSI escape codes for colors
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"

def main():
    # One neurotic, self‑deprecating, existential quote in Woody Allen’s style
    quote = "'Deep down, I'm just a neurotic stand-up comedian performing on a stage of stars, convinced that the audience is judging my sunscreen.'"

    # Choose a width for the box (at least as long as the quote plus padding)
    width = max(60, len(quote) + 4)

    # Build the three lines of the box
    top = f"{CYAN}╔{'═'*width}╗{RESET}"
    middle = f"{CYAN}║{RESET} {YELLOW}{quote}{RESET} {CYAN}║{RESET}"
    bottom = f"{CYAN}╚{'═'*width}╝{RESET}"

    # Output the box
    print("\n")
    print(top)
    print(middle)
    print(bottom)
    print("\n")

if __name__ == "__main__":
    main()