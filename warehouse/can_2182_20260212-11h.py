"""
Campbell's Soup Can #2182
Produced: 2026-02-12 11:56:26
Worker: Aurora Alpha (openrouter/aurora-alpha)
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
import itertools

# ANSI escape codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Woody‑Allen‑style philosophical quote
QUOTE = "I think, therefore I'm terribly anxious about thinking."

def spinner_animation(duration: float = 2.0, interval: float = 0.1) -> None:
    """Show a simple rotating spinner for *duration* seconds."""
    chars = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{YELLOW}Thinking {next(chars)}{RESET}")
        sys.stdout.flush()
        time.sleep(interval)
    # clean the line
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()

def colored_box(text: str, text_color: str = CYAN) -> str:
    """Return a string that draws a box around *text* using ANSI colors."""
    # width = text length + 4 spaces of padding
    width = len(text) + 4
    top    = f"{MAGENTA}╔" + "═" * width + "╗{RESET}"
    middle = f"{MAGENTA}║{RESET}  {BOLD}{text_color}{text}{RESET}  {MAGENTA}║{RESET}"
    bottom = f"{MAGENTA}╚" + "═" * width + "╝{RESET}"
    return "\n".join([top, middle, bottom])

def main() -> None:
    spinner_animation()
    time.sleep(0.3)  # a brief pause before the reveal
    print(colored_box(QUOTE, CYAN))
    print()  # final newline for a clean prompt

if __name__ == "__main__":
    main()