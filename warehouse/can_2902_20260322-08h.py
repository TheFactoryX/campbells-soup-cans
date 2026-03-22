"""
Campbell's Soup Can #2902
Produced: 2026-03-22 08:51:38
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

def print_woody_quote():
    # Woody Allen style quote
    quote = (
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it through not dying.\n\n"
        "- Woody Allen"
    )

    # Visual frame with colors
    frame_top = f"{BLUE}╔═══════════════════════════════════════════════════════════════╗{RESET}"
    frame_bottom = f"{BLUE}╚═══════════════════════════════════════════════════════════════╝{RESET}"
    empty_line = f"{BLUE}║{WHITE}                                                               {BLUE}║{RESET}"

    # Print with typewriter effect
    def slow_print(text, delay=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

    # Build the framed quote
    framed_quote = [
        frame_top,
        f"{BLUE}║{WHITE}  {BOLD}I don't want to achieve immortality through my work;{RESET}     {BLUE}║{RESET}",
        f"{BLUE}║{WHITE}  {BOLD}I want to achieve it through not dying.{RESET}                   {BLUE}║{RESET}",
        f"{BLUE}║{WHITE}                                                               {BLUE}║{RESET}",
        f"{BLUE}║{WHITE}  - Woody Allen                                           {BLUE}║{RESET}",
        frame_bottom
    ]

    # Animate each line appearing
    print("\n" * 2)
    for line in framed_quote:
        slow_print(line + "\n")
        time.sleep(0.1)

    # Add a final dramatic pause
    time.sleep(1)
    print(f"\n{MAGENTA}Life: 99% inspiration, 1% perspiration, and 100% anxiety.{RESET}\n")

if __name__ == "__main__":
    print_woody_quote()