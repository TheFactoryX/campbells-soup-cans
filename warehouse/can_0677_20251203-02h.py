"""
Campbell's Soup Can #677
Produced: 2025-12-03 02:19:04
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
A tiny, colorful Woody‑Allen‑style quote printer.
Runs with plain Python, no external dependencies.
"""

import sys
import time

# ANSI escape codes for colors and styles
RESET  = '\033[0m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'

def type_writer(text: str, delay: float = 0.08, color: str = '') -> None:
    """Prints `text` one character at a time, with an optional color."""
    for ch in text:
        sys.stdout.write(f'{color}{ch}{RESET}' if color else ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def spinner(duration: float = 1.0, delay: float = 0.1) -> None:
    """Displays a brief spinning cursor while the program 'prepares'."""
    symbols = ['|', '/', '-', '\\']
    end = time.time() + duration
    idx = 0
    while time.time() < end:
        sys.stdout.write(f'\r{CYAN}Preparing... {symbols[idx % len(symbols)]}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
        idx += 1
    sys.stdout.write('\r' + ' ' * 30 + '\r')  # clear the line

def main() -> None:
    # A little header
    header = f"{BOLD}{MAGENTA}  _______          _                {{Woody Allen}}  _______   \n" \
             f" |__   __|        | |               | |      | |  \n" \
             f"    | |  _ __  ___| |_ __ _  ___    | |__   | |  \n" \
             f"    | | | '__|/ _ \\ | __/ _` |/ __|   | '_ \\  | |  \n" \
             f"    | | | |  |  __/ | || (_| | (__    | |_) | | |  \n" \
             f"    |_| |_|   \\___|_|\\__\\__,_|\\___|   |_.__/  |_|  \n"
    print(header)

    spinner(duration=1.2)

    # The quote, boxed and colorful
    quote = (
        "   \"I never auditioned for a role where I could be wise; "
        "I just keep asking myself why the universe can't be a sitcom.\"   "
        f"  –{BOLD}Woody Allen{RESET}"
    )
    box_width = len(quote) + 4
    top_bottom = f"{GREEN}+{'-' * box_width}+{RESET}"
    middle = f"{GREEN}| {YELLOW}{quote}{RESET} |{GREEN}{RESET}"

    # Print the box with type-writer effect
    print('\n' + top_bottom)
    type_writer(middle, delay=0.025)
    print(top_bottom + '\n')

    # Farewell note
    type_writer(f"{DIM}— And that's the end of my thoughts, we all know silence is the answer.{RESET}")

if __name__ == "__main__":
    main()
