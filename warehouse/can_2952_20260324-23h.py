"""
Campbell's Soup Can #2952
Produced: 2026-03-24 23:46:43
Worker: Inception: Mercury Coder (inception/mercury-coder)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes for colors
RESET   = "\033[0m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

# Box drawing characters
top    = f"{CYAN}┌{'─'*50}┐{RESET}"
bottom = f"{CYAN}└{'─'*50}┘{RESET}"
mid    = f"{CYAN}│{RESET}"

# The Woody‑Allen‑style quote
quote_line = f"{YELLOW}I think, therefore I am...{RESET}"
extra_line = f"{YELLOW}but I'm still terrified of the dentist. {RESET}"

def print_with_delay(text, delay=0.02):
    """Print text character by character with a short delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    print_with_delay(top)
    print_with_delay(f"{mid} {MAGENTA}🎭 {RESET} {quote_line}{mid}")
    time.sleep(0.5)
    print_with_delay(f"{mid} {MAGENTA}🎭 {RESET} {extra_line}{mid}")
    print_with_delay(bottom)

if __name__ == "__main__":
    main()