"""
Campbell's Soup Can #4878
Produced: 2026-08-31 23:51:28
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

# Woody Allen‑style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Box parts
top = "   _________   "
mid_top = "  /         \\  "
mid = f' |  "{YELLOW}{quote}{CYAN}"  | '
mid_bot = "  \\_________/  "

# Apply cyan box color
line0 = f"{CYAN}{top}{RESET}"
line1 = f"{CYAN}{mid_top}{RESET}"
line2 = f"{CYAN}{mid}{RESET}"
line3 = f"{CYAN}{mid_bot}{RESET}"

def slow_print(text, delay=0.03):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def spinner(duration=1.5):
    """Show a simple thinking spinner."""
    symbols = ["|", "/", "-", "\\"]
    end = time.time() + duration
    idx = 0
    while time.time() < end:
        sys.stdout.write(f"\r{symbols[idx % 4]} Thinking...")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

if __name__ == "__main__":
    spinner()
    slow_print(line0)
    slow_print(line1)
    slow_print(line2)
    slow_print(line3)