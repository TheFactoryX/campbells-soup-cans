"""
Campbell's Soup Can #2557
Produced: 2026-03-04 05:59:26
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_woody_quote():
    # ANSI escape codes for colors
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    quote = [
        f"{RED}I don't want to achieve immortality through my work; {RESET}",
        f"{YELLOW}I want to achieve it through not dying. {RESET}",
        "",
        f"{GREEN}Besides, my work is mostly just me talking to myself in a room.{RESET}",
        f"{BLUE}If that's art, then my refrigerator is a masterpiece.{RESET}",
        "",
        f"{MAGENTA}The universe is expanding, but my waistline is expanding faster.{RESET}",
        f"{CYAN}At this rate, I'll be the center of my own black hole soon.{RESET}"
    ]

    # Print quote with typewriter effect
    def typewriter(text, delay=0.05):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)

    # Print quote line by line with animation
    for line in quote:
        if line.strip():
            typewriter(line)
            print()
        else:
            print()
        time.sleep(0.3)

    # Print Woody Allen face with ASCII art
    print()
    print(f"{BOLD}