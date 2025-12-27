"""
Campbell's Soup Can #1207
Produced: 2025-12-27 06:47:15
Worker: ByteDance Seed: Seed 1.6 (bytedance-seed/seed-1.6)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import sys

# ANSI Escape Codes for Colors & Formatting (no external dependencies)
RESET = "\033[0m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR_SCREEN = "\033[2J\033[H"  # Clear screen + move cursor to top-left
CYAN = "\033[36m"
LIGHT_CYAN = "\033[96m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"

# Woody Allen-style neurotic philosophical quote (original creation)
WOODY_QUOTE = [
    f"{MAGENTA}I spent three hours debating if my oat milk latte’s foam texture{RESET}",
    f"{MAGENTA}was a cosmic sign I’m wasting my life—turns out it was just{RESET}",
    f"{YELLOW}a barista who hates me. Existential dread’s easy; fixing a lousy latte requires courage I don’t possess.{RESET}"
]

# ASCII Rounded Box Dimensions (tailored to quote length)
BOX_WIDTH = 78
EMPTY_LINE = f"│{(' ' * (BOX_WIDTH - 2))}│"

def print_woody_box(border_color):
    """Print rounded ASCII box with colored border and quote"""
    print(f"{border_color}╭{('─' * (BOX_WIDTH - 2))}╮{RESET}")
    print(f"{border_color}{EMPTY_LINE}{RESET}")
    for line in WOODY_QUOTE:
        centered_line = line.center(BOX_WIDTH - 2)
        print(f"{border_color}│{centered_line}│{RESET}")
    print(f"{border_color}{EMPTY_LINE}{RESET}")
    print(f"{border_color}╰{('─' * (BOX_WIDTH - 2))}╯{RESET}")

def main():
    try:
        print(HIDE_CURSOR, end="")  # Hide cursor during animation
        # Subtle border color cycle animation (5 cycles)
        for _ in range(5):
            print(CLEAR_SCREEN, end="")
            print_woody_box(CYAN)
            time.sleep(0.7)
            print(CLEAR_SCREEN, end="")
            print_woody_box(LIGHT_CYAN)
            time.sleep(0.7)
        # Final static box (cyan border for clarity)
        print(CLEAR_SCREEN, end="")
        print_woody_box(CYAN)
        print(f"\n{CYAN}* (Neurotic pause intensifies) *{RESET}")
    finally:
        print(SHOW_CURSOR, end="")  # Restore cursor even if program exits early
        print(RESET)  # Reset all formatting

if __name__ == "__main__":
    try:
        main()
        # Keep output visible before exiting (for terminal users)
        time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n{RESET}{SHOW_CURSOR}")
        sys.exit(0)