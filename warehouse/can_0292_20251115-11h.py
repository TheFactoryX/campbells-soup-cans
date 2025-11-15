"""
Campbell's Soup Can #292
Produced: 2025-11-15 11:25:30
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

# ANSI color codes for a neurotic palette
OFF_WHITE = "\033[38;5;253m"
NEUROTIC_BLUE = "\033[38;5;69m"
ANXIOUS_RED = "\033[38;5;160m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Brain in crisis mode
BRAIN = [
    "   |\\", "   | \\__",
    "   |    )", "   \   /",
    "    \\ |", "     ||",
    "     ||", "     ||",
    "     ||", "     \\|"
]

# Obnoxious party guest ASCII glasses
GLASSES = [
    "  -----O      O-----",
    " |      \\    /      |",
    " A       \\  /       A",
    "  \\_______\/_______/"
]

def build_quote():
    """Construct woody's latest masterpiece, guaranteed 100% angst and 0% gluten"""
    lines = [
        OFF_WHITE + "I've spent years contemplating the void," + RESET,
        NEUROTIC_BLUE + "and it turns out it was contemplating me back—" + RESET,
        ANXIOUS_RED + "specifically wondering why I still haven't" + RESET,
        ANXIOUS_RED + "mastered parallel parking at my age." + RESET
    ]
    return "\n".join(lines)

def shaky_frame():
    """Because even existential crises need stylish framing"""
    width = 50
    symbols = ['*', 'o', '~', '¬', '.']
    print(ANXIOUS_RED + "".join(random.choices(symbols, k=width)) + RESET)
    for _ in range(3):
        print(ANXIOUS_RED + random.choice(symbols) + RESET + " " * 48 + ANXIOUS_RED + random.choice(symbols) + RESET)
    print(ANXIOUS_RED + "".join(random.choices(symbols, k=width)) + RESET)

def animated_brain():
    """Make that existential dread wiggle like it deserves"""
    term_width = os.get_terminal_size().columns
    position = 0
    direction = 1
    for _ in range(20):
        print("\033[2J\033[H")  # Clear screen and jump to home
        for line in GLASSES:
            print(line.rjust(term_width - position))
        print(" " * position + build_quote())
        for line in BRAIN:
            print(" " * position + line)
        time.sleep(0.2)
        position += direction
        if position > 10 or position < 0:
            direction *= -1

animated_brain()

# Sudden existential punctuation
print(BOLD + NEUROTIC_BLUE + "..." + RESET)

# Bonus absurd statistic (because Woody always brings receipts)
print(f"\n{OFF_WHITE}(Based on 100% unscientific calculations: 73.2% chance this program{RESET}")
print(f"{OFF_WHITE}is more self-aware than the average New Yorker dining alone.{RESET}")