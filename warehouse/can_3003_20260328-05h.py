"""
Campbell's Soup Can #3003
Produced: 2026-03-28 05:35:17
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes for colors and styles
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"

def print_quote():
    quote = (
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it through not dying.\n\n"
        " - Woody Allen"
    )

    # Create a visually interesting border
    border = f"{MAGENTA}╭" + "─" * 50 + f"╮{END}"
    bottom_border = f"{MAGENTA}╰" + "─" * 50 + f"╯{END}"

    # Print the quote with colors and formatting
    print("\n" * 2)
    print(border)
    print(f"{MAGENTA}│{END}" + " " * 50 + f"{MAGENTA}│{END}")

    lines = quote.split("\n")
    for line in lines:
        padding = (50 - len(line)) // 2
        print(f"{MAGENTA}│{END}" + " " * padding + f"{BOLD}{line}{END}" + " " * (50 - len(line) - padding) + f"{MAGENTA}│{END}")

    print(f"{MAGENTA}│{END}" + " " * 50 + f"{MAGENTA}│{END}")
    print(bottom_border)

    # Add a blinking effect for dramatic pause
    for _ in range(3):
        print(f"{CYAN}{BOLD}⚡" + " " * 48 + f"⚡{END}")
        time.sleep(0.3)
        print(" " * 52)
        time.sleep(0.3)

    print(f"\n{YELLOW}{BOLD}Life is full of misery, loneliness, and suffering - and it's all over much too soon.{END}")
    print(f"\n{GREEN}Just kidding! (Or am I?){END}")

if __name__ == "__main__":
    print_quote()