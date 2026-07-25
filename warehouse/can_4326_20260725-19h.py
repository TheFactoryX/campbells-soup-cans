"""
Campbell's Soup Can #4326
Produced: 2026-07-25 19:34:18
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

# ANSI escape codes for colors
RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"

def main():
    width = 68  # interior width of the speech bubble

    # Header with title and star line
    print(f"{YELLOW}{BOLD}    ~ WOODY'S WISDOM ~    {RESET}")
    print(f"{YELLOW}   {'*'*20}  {RESET}")
    time.sleep(0.5)

    # Top border of the speech bubble
    top_border = f"{CYAN}╭{'─'*width}╮{RESET}"
    print(top_border)
    time.sleep(0.3)

    # The philosophical quote (Woody Allen style)
    quote_lines = [
        "I'm not afraid of death; I just don't want to be the",
        "one who has to explain why I'm here when nobody asked",
        "me to show up."
    ]

    for line in quote_lines:
        # One line of the bubble, colored and formatted
        bubble_line = f"{CYAN}│{RESET}{GREEN} {line:<{width}} {CYAN}│{RESET}"
        print(bubble_line)
        time.sleep(0.3)

    # Bottom border of the speech bubble
    bottom_border = f"{CYAN}╰{'─'*width}╯{RESET}"
    print(bottom_border)
    time.sleep(0.5)

    # Closing tag
    print(f"{YELLOW}{BOLD}— End of quote —{RESET}")

if __name__ == "__main__":
    main()