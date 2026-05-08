"""
Campbell's Soup Can #3606
Produced: 2026-05-08 14:17:02
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI Escape Codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Clear terminal screen
print("\033[2J\033[H", end="")
sys.stdout.flush()

# Loading animation
print(f"{BOLD}{RED}✨ Summoning Neurotic Existentialist Energy...{RESET}", end="")
sys.stdout.flush()
for _ in range(3):
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()
print("\n" * 2)

# Original Woody Allen style quote
QUOTE = "I don’t mind that the universe is expanding—I just hate that my waistline is expanding faster, and neither of them seem to have any meaning whatsoever."
ATTRIBUTION = "- Woody Allen (If he was really into cosmology and dieting)"

# Border setup
BORDER_LEN = len(QUOTE) + 2
TOP_BORDER = f"{CYAN}┌{'─' * BORDER_LEN}┐{RESET}"
BOTTOM_BORDER = f"{CYAN}└{'─' * BORDER_LEN}┘{RESET}"
SIDE_BORDER = f"{CYAN}│{RESET}"

# Print top border
print(TOP_BORDER)

# Start left border and quote styling
sys.stdout.write(f"{SIDE_BORDER} {YELLOW}{BOLD}")
sys.stdout.flush()

# Typewriter effect for the quote
for char in QUOTE:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)

# Close quote with right border
print(f"{RESET} {SIDE_BORDER}")

# Print bottom border
print(BOTTOM_BORDER)

# Print attribution
print(f"\n{ITALIC}{GREEN}{ATTRIBUTION}{RESET}")

# Footer
print(f"\n{BOLD}Press Ctrl+C to exit before the meaninglessness consumes you.{RESET}")
time.sleep(2)