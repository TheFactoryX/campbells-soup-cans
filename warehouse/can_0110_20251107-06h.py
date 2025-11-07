"""
Campbell's Soup Can #110
Produced: 2025-11-07 06:45:31
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ASCII art for film reel (Woody Allen reference)
FILM_REEL = [
    "   ____________",
    "  /            \\",
    " |  o    o    o |",
    " |  o    o    o |",
    " |  o    o    o |",
    "  \____________/",
    "       ||||",
    "       ||||",
    "       ||||"
]

# Woody Allen style quote
QUOTE = "I'm not a neurotic person. I'm a person with neuroses. Which is, as you know, the same thing, but with fewer letters and a lot more anxiety."

# Clear screen (works in most terminals)
print("\033[2J", end="")

# Print film reel animation (rotating)
for _ in range(3):
    for frame in FILM_REEL:
        print(frame)
        time.sleep(0.1)
    # Clear current frame and print next (without moving cursor)
    print("\033[9A\033[0K", end="")  # Move up 9 lines, clear line

# Print the quote with typewriter effect
print(f"\n{CYAN}{QUOTE}{RESET}\n")
sys.stdout.flush()  # Ensure immediate output

# Add some decorative elements
print(f"{YELLOW}{'='*30}{RESET}")
print(f"{CYAN}   A Woody Allen-esque moment in the chaos of existence{RESET}")
print(f"{YELLOW}{'='*30}{RESET}")
sys.stdout.flush()

# Final animation: make the quote glow
for _ in range(3):
    print(f"\033[30;46m{QUOTE}\033[0m")  # Black text on cyan
    time.sleep(0.3)
    print(f"\033[30;43m{QUOTE}\033[0m")  # Black text on yellow
    time.sleep(0.3)
    print(f"\033[30;42m{QUOTE}\033[0m")  # Black text on green
    time.sleep(0.3)
    print("\033[2K", end="")  # Clear line after each
    sys.stdout.flush()