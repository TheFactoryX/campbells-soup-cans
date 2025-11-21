"""
Campbell's Soup Can #425
Produced: 2025-11-21 14:34:11
Worker: Inception: Mercury (inception/mercury)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# Woody‑Allen style quote (neurotic, funny, self‑deprecating, existential)
quote = ("I’m terrified of my own mortality, so I keep pretending I’ll never die—"
         "just to avoid the awkward silence that follows a good existential crisis.")

# Determine box width based on the longest line (the quote)
width = len(quote) + 4
border = "+" + "-" * (width - 2) + "+"

def print_boxed_quote():
    """Print the quote inside a colored ASCII box."""
    # Top border
    print(RED + border + RESET)
    # Empty line with padding
    print(RED + "|" + RESET + "  " + RED + "|" + RESET)
    # Quote line with left padding
    print(RED + "|" + RESET + "  " + CYAN + quote + RESET + "  " + RED + "|" + RESET)
    # Empty line
    print(RED + "|" + RESET + "  " + RED + "|" + RESET)
    # Bottom border
    print(RED + border + RESET)

def type_effect(text, delay=0.05):
    """Print text one character at a time to simulate typing."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # Simple blinking animation before the final display
    for _ in range(3):
        print_boxed_quote()
        time.sleep(0.3)
        # Clear the screen (ANSI escape)
        sys.stdout.write("\033[2J\033[H")
    # Final display with typing effect
    print_boxed_quote()
    print("\n")
    print("Typing the quote:")
    type_effect(CYAN + quote + RESET)

if __name__ == "__main__":
    main()