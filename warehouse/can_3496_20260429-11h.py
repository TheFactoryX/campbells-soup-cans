"""
Campbell's Soup Can #3496
Produced: 2026-04-29 11:54:31
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI Escape Codes for formatting (pure Python, no deps)
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
WHITE = "\033[97m"
GREY = "\033[90m"

# Original Woody Allen-style quote: neurotic, existential, funny, self-deprecating
quote = "I’m perfectly fine with the concept of existential nihilism—I just wish the universe had sent a memo before canceling the meaning of my life, because I already RSVP’d to the ‘purpose’ banquet and bought a new tie."

# Box configuration for visual flair
PAD_LEFT = 2
PAD_RIGHT = 2
QUOTE_LEN = len(quote)
INNER_WIDTH = QUOTE_LEN + PAD_LEFT + PAD_RIGHT

# Double-line Unicode box borders (supported by all modern terminals)
top_border = f"{CYAN}╔{'═' * INNER_WIDTH}╗{RESET}"
middle_line = f"{CYAN}║{' ' * INNER_WIDTH}║{RESET}"
bottom_border = f"{CYAN}╚{'═' * INNER_WIDTH}╝{RESET}"

# Print header
print(f"{BOLD}{YELLOW}✎  WOODY ALLEN-ESQUE EXISTENTIAL QUOTE DISPENSER (NEUROTIC MODE ACTIVATED)  ✎{RESET}")
print()

# Print empty box frame
print(top_border)
print(middle_line)
print(bottom_border)

# Move cursor to the quote start position inside the box:
# - Up 2 lines to the empty middle line of the box
# - Right 3 columns (1 past left border ║ + 2 left padding spaces)
sys.stdout.write(f"\033[2A\033[3C")
sys.stdout.flush()

# Typewriter animation for the quote
sys.stdout.write(f"{ITALIC}{WHITE}")  # Start italic white text
for char in quote:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)  # Adjust typing speed here (lower = faster)
sys.stdout.write(RESET)  # Reset text formatting
sys.stdout.flush()

# Move cursor below the box
print("\n")

# Funny fake attribution
print(f"{GREY}{DIM}- Muttered by a man who’s worried he left the oven on, and also that the oven is a metaphor for his soul{RESET}")

# Extra neurotic visual flair
print()
print(f"{GREY}{DIM}*nervously adjusts glasses*{RESET}")
time.sleep(0.5)
print(f"{GREY}{DIM}*fidgets with tie*{RESET}")
time.sleep(0.5)
print(f"{GREY}{DIM}*checks if the universe is still canceling on him*{RESET}")
time.sleep(0.5)
print()