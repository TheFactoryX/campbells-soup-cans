"""
Campbell's Soup Can #768
Produced: 2025-12-07 07:29:07
Worker: Perplexity: Sonar Pro Search (perplexity/sonar-pro-search)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# A custom Woody Allen–style philosophical quote
quote = "I don’t mind dying; I just wish it didn’t involve so much paperwork, and that I could complain about it afterward."

# Fun box with a wobbly, jittery effect
def print_wobbly_box(text, width=60):
    border = "═" * width
    pad = (width - len(text) - 2) // 2
    left_pad = " " * pad
    right_pad = " " * (width - len(text) - 2 - pad)

    # Top border with jitter
    print(f"  ╔{border}╗")
    
    # Middle line with jittery movement
    for _ in range(3):
        offset = random.choice([-1, 0, 1])
        print(f"  ║{left_pad}{' ' * offset}{text}{' ' * (2 - offset)}{right_pad}║")
        time.sleep(0.15)
    
    # Final centered line
    print(f"  ║{left_pad} {text} {right_pad}║")
    print(f"  ╚{border}╝")

# Typewriter effect for the quote
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear screen and add some flair
print("\033[2J\033[H", end="")  # Clear screen and move cursor to top

# Title with color
print(f"{BOLD}{MAGENTA}🎭 A Moment of Neurotic Wisdom 🎭{RESET}\n")

# ASCII art of a tiny, anxious man with glasses
print(f"{CYAN}")
print("     ,--.   ")
print("    / o  \\  ")
print("   |  ^   | ")
print("   \\ -- /  ")
print("    `--'   ")
print("     ||    ")
print("     ||    ")
print(f"{RESET}")

# Print the quote in a wobbly box
print_wobbly_box(f"{YELLOW}{quote}{RESET}")

# Add a blinking cursor effect at the end
print()
print(f"{BOLD}{WHITE}💭{RESET} {ITALIC}...and then I started overthinking it.{RESET}")

# Optional: make the last line blink a few times
for _ in range(3):
    print(f"\033[2K\r{BOLD}{WHITE}💭{RESET} {ITALIC}...and then I started overthinking it.{RESET}", end="")
    time.sleep(0.5)
    print(f"\033[2K\r{BOLD}{WHITE}💭{RESET} {ITALIC}...and then I started overthinking it.{RESET}", end="")
    time.sleep(0.5)
print()

# Reset terminal
print(RESET, end="")