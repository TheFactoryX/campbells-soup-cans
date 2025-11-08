"""
Campbell's Soup Can #143
Produced: 2025-11-08 16:34:47
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained Python program that displays a Woody‑Allen style
philosophical quote with a splash of color and a dash of animation.
"""

import sys
import time
import random

# ANSI escape codes for styling
RESET   = "\033[0m"
BOLD    = "\033[1m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
BLACK   = "\033[30m"
WHITE_BG= "\033[107m"

# ------------------------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------------------------

def _clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J\033[H")  # Clear buffer and move cursor home
    sys.stdout.flush()

def _spinner(duration: float):
    """Display a rotating spinner for the given duration in seconds."""
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{CYAN}Loading...{symbols[idx % len(symbols)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write("\r" + " " * 20 + "\r")  # clear line

def _typewriter(text: str, delay: float = 0.05):
    """Print text to stdout with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

# ------------------------------------------------------------------------------
# Main display logic
# ------------------------------------------------------------------------------

def _build_boxed_quote(quote: str) -> str:
    """Wrap the quote in a decorative ASCII box."""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    top = f"{WHITE_BG}{BLACK}{'─' * (max_len + 4)}{RESET}"
    middle = "\n".join(
        f"{WHITE_BG}{BLACK}  {YELLOW}{line.ljust(max_len)}{BLACK}  {RESET}"
        for line in lines
    )
    bottom = f"{WHITE_BG}{BLACK}{'─' * (max_len + 4)}{RESET}"
    return f"{top}\n{middle}\n{bottom}\n"

def main():
    _clear_screen()

    # Header
    header = f"{BOLD}{MAGENTA}Woody Allen's After‑Death Philosophy{RESET}"
    _typewriter(header + "\n\n", delay=0.04)

    # Show a short loading animation
    _spinner(2.0)

    # The quote (neurotic, funny, existential)
    quote = (
        "\"I’m terrified of death, but I’m even more terrified\n"
        "that the universe will have misprinted the bill for its services.\"\n"
        "- Woody Allen"
    )

    boxed_quote = _build_boxed_quote(quote)
    _typewriter(boxed_quote, delay=0.06)

    # Bottom nicety
    sys.stdout.write(f"\n{CYAN}Enjoy your existential dread at your own pace!{RESET}\n")

if __name__ == "__main__":
    main()