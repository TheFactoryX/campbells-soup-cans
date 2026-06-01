"""
Campbell's Soup Can #3838
Produced: 2026-06-01 10:32:54
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Simple Woody Allen style quote
quote = (
    "I'm not afraid of death; I just don't want to be there when it happens."
)

# ASCII art border (a nervous face)
border_top    = f"{CYAN}╔{'═'*(len(quote)+4)}╗{RESET}"
border_mid    = f"{CYAN}║  {quote}  ║{RESET}"
border_bottom = f"{CYAN}╚{'═'*(len(quote)+4)}╝{RESET}"

# Animate the quote appearing character by character with a slight pulse
def animate():
    sys.stdout.write(border_top + "\n")
    sys.stdout.flush()
    time.sleep(0.2)
    # build the middle line gradually
    middle = f"{CYAN}║  {RESET}"
    for ch in quote:
        # choose a color that shifts slightly for fun
        color = YELLOW if (ord(ch) % 2 == 0) else GREEN
        sys.stdout.write(middle + color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
        middle += color + ch + RESET
    # finish the middle line
    sys.stdout.write(f"{CYAN}  ║{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(border_bottom + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    animate()
    # optional: a tiny blinking cursor effect after the quote
    for _ in range(3):
        sys.stdout.write(f"{MAGENTA}█{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.4)
    print()  # final newline