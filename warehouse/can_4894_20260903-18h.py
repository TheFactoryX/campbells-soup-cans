"""
Campbell's Soup Can #4894
Produced: 2026-09-03 18:40:12
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen style philosophical quote generator.
Prints a single witty, self‑deprecating quote in a colorful ASCII box.
"""

import time

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

def type_out(text: str, color: str = "", delay: float = 0.04) -> None:
    """Print text character‑by‑character, optionally in colour."""
    if color:
        print(color, end="", flush=True)
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    if color:
        print(RESET, end="", flush=True)
    print()  # newline after the whole string

def main() -> None:
    # The Woody‑Allen‑style quote (single line, self‑deprecating, existential)
    quote = '"I’m terrified of death, but I can’t wait for the next act."'

    # Build a decorative ASCII box
    # Top border
    top = f"{CYAN}╔════════════════════════════════════════════════════════╗{RESET}"
    # Middle line with the quote, centred-ish
    middle = f"{CYAN}║{RESET}  {YELLOW}{quote}{RESET}  {CYAN}║{RESET}"
    # Empty line for spacing
    empty = f"{CYAN}║{RESET}   {CYAN}║{RESET}"
    # Author line (in green)
    author = f"{CYAN}║{RESET}   {GREEN}— Woody Allen{RESET}   {CYAN}║{RESET}"
    # Bottom border
    bottom = f"{CYAN}╚════════════════════════════════════════════════════════╝{RESET}"

    # Print everything with a little “type‑writer” flair
    type_out(top, "")
    type_out(middle, "")
    type_out(empty, "")
    type_out(author, "")
    type_out(bottom, "")

    # A tiny final flourish – a blinking asterisk
    print(f"\n{BOLD}{MAGENTA} *   (the universe nods)   *{RESET}")

if __name__ == "__main__":
    main()