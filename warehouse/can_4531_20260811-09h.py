"""
Campbell's Soup Can #4531
Produced: 2026-08-11 09:13:40
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

def woody_quote():
    # ANSI color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    GREEN = "\033[1;32m"
    MAGENTA = "\033[1;35m"

    # Clear screen
    sys.stdout.write("\033[2J")
    sys.stdout.flush()

    # Title
    print(f"{YELLOW}{BOLD}*** Woody's Midnight Musings ***{RESET}\n")

    # ASCII art: a contemplative tree with a thought bubble
    art = f"""{CYAN}
           ,--.
          ( ___ )
         (_______)   .--.
           | |   \\-'   /
           | |     '-'
           | |
          .-' '-.
         '   _   '
           (O)_(O)
    {RESET}
    """
    print(art)

    # The quote, wrapped in a nice box
    quote = (
        f"{MAGENTA}{BOLD}╔══════════════════════════════════════════╗{RESET}\n"
        f"{MAGENTA}║{RESET} {GREEN}{BOLD}“{RESET}"
        f"{CYAN}I'm not afraid of the big bad void out there; "
        f"I just don't want to be the one answering its doorbell.{RESET}"
        f"{GREEN}{BOLD}”{RESET}  "
        f"{MAGENTA}║{RESET}\n"
        f"{MAGENTA}╚══════════════════════════════════════════╝{RESET}"
    )

    # Simple typewriter effect
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.02)

    print("\n")
    print(f"{YELLOW}{BOLD}--- End of one small slice of existential cheese ---{RESET}")

if __name__ == "__main__":
    woody_quote()