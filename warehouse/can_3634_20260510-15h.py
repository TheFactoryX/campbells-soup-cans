"""
Campbell's Soup Can #3634
Produced: 2026-05-10 15:13:54
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
RESET = "\033[0m"
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

def print_colorful_quote():
    woody_quote = [
        "           _",
        "       .-' '-.",
        "      /       \\",
        "     | (o) (o) |",
        "     |    <    |",
        "     | \\___/  |",
        "      \\_____/]",
        "",
        "    Woody Allen's Wisdom",
        "",
        "\033[1m\"I used to be terrified of death, but then I realized I'm",
        "already late for my own funeral. It's the only appointment",
        "I can't reschedule—and even my procrastination is ahead of",
        "schedule.\"\033[0m",
        "",
        "       - The existential crisis of a neurotic New Yorker",
    ]
    
    # Animated opening
    border = "+" + "-" * 54 + "+"
    print("\n\033[1;37m" + border)
    
    for _ in range(2):
        print("|" + " " * 54 + "|")
    
    # Typing animation for each line
    for line in woody_quote:
        sys.stdout.write("\033[1;37m|\033[1;36m ")
        for char in line:
            color = random.choice(COLORS)
            sys.stdout.write(f"{color}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write("\n")
    
    for _ in range(2):
        print("\033[1;37m|" + " " * 54 + "|")
    
    print(border + RESET + "\n")
    
    # Final flourish
    print("\033[3mPS: According to my therapist, this quote is a cry for help.\033[0m")

if __name__ == "__main__":
    print_colorful_quote()