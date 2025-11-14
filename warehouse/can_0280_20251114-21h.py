"""
Campbell's Soup Can #280
Produced: 2025-11-14 21:29:41
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
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
BLUE = '\033[94m'
GREEN = '\033[92m'
PINK = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

def typewriter(text, delay=0.04):
    """Prints text character by character with a delay for animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Footnote style separator
def print_footnote(line, delay=0.03):
    print('\n'.join(
        line.split('\n')
    ), flush=True)
    sys.stdout.flush()

# Build the quote with color variations
quote = (
    f"{BLUE}Why do I ever leave the house?{RESET}\n\n"
    f"{GREEN}Because I’m afraid I might die a lawyer instead of a poet.{RESET}\n\n"
    f"{PINK}At least then the crows would eat my face with\n"
    f"{BLUE}understanding.{RESET}\n\n"
    f"{CYAN}-- Me, probably\n"
    f"\n"
    f"{GREEN}Bonus Existential Crisis:\n"
    f"Is this code running in the right directory? 🤔\n"
    f"Or are we all just \n"
    f"{RESET}paths in a loop? 🌀"
)

# Decorative ASCII frame
def draw_frame():
    print("\033[H\033[3J")  # Clear screen
    frame = [
        f"{CYAN}┌──────────────────────────────────────┐{RESET}",
        "│                                       │",
        "│      🕰️                              │",
        "│                                       │",
        "│           🤨                          │",
        "│                                       │",
        f"│       {CYAN}└────────────────────────┘{RESET}"
    ]
    for line in frame:
        print(line)
        time.sleep(0.2)

# Main execution
draw_frame()
time.sleep(1)
print('\033[3J')  # Clear screen
typewriter(quote, delay=0.05)