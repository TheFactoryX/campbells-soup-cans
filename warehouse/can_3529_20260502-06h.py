"""
Campbell's Soup Can #3529
Produced: 2026-05-02 06:20:12
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
COLOR_CYAN = "\033[96m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"
COLOR_MAGENTA = "\033[95m"

# Woody Allen‑style quote (original)
QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens."
)

def typewriter(text, delay=0.04):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def draw_box():
    """Draw a simple decorative box around the quote."""
    box = rf"""{COLOR_CYAN}
   _______________________
  /                       \
 |  {COLOR_YELLOW}{' ' * 23}{COLOR_CYAN}  |
 |  {COLOR_YELLOW}{QUOTE:^23}{COLOR_CYAN}  |
 |  {COLOR_YELLOW}{' ' * 23}{COLOR_CYAN}  |
  \_______________________/
{COLOR_RESET}"""
    print(box)

def main():
    # Optional: a quick "thinking" animation before the quote appears
    thinking = ["🤔", "💭", "🧠", "💫"]
    for _ in range(3):
        for symbol in thinking:
            sys.stdout.write(f"\r{COLOR_MAGENTA}{symbol} pondering...{COLOR_RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")  # clear the line

    # Print the decorated quote
    draw_box()

if __name__ == "__main__":
    main()