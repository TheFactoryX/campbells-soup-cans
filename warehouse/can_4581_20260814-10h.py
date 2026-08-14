"""
Campbell's Soup Can #4581
Produced: 2026-08-14 10:16:23
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style philosophical quote with ASCII art and typing animation

import time

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"

def type_print(text, color=MAGENTA):
    """Print text with a typing animation."""
    for ch in text:
        print(f"{color}{ch}", end="", flush=True)
        time.sleep(0.05)
    print(RESET)

def main():
    # ASCII art thought bubble (Woody style)
    bubble = f"""{CYAN}
      .-''-.
     ( o o )
      | ^ |
      |__'|
       `---'
{RESET}"""
    print(bubble)

    # Whimsical header
    header = f"{CYAN}{BOLD}--- Woody's noodle splutters a cosmic quip ---{RESET}"
    print(header)

    # The philosophical quote in Woody Allen's neurotic style
    quote = "\"I'm not afraid of death; I just don't want to be around when it happens.\""
    type_print(quote, MAGENTA)

    # A tiny flourish
    flourish = f"{YELLOW}* * * The universe pauses to chuckle... * * *{RESET}"
    print(flourish)

if __name__ == "__main__":
    main()