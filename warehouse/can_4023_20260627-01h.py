"""
Campbell's Soup Can #4023
Produced: 2026-06-27 01:22:59
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen‑style philosophical quote printer.
Prints a randomly selected quote inside a colorful ASCII art box.
"""

import random
import time
import sys

# ANSI escape codes for colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"

# Woody Allen‑like philosophical quotes
QUOTES = [
    "I'm terrified of my own mortality, but I'm even more terrified that no one will notice when I'm finally forgotten.",
    "I don't want to achieve immortality through my work; I want to achieve it through not being forgotten for five minutes.",
    "Life is full of misery, loneliness, and suffering – and it's all over much too soon.",
    "I'm not afraid of death; I just don't want to be there when it happens because the last thing I'd see is my own mediocrity.",
    "My grandfather once said that life is a tragedy when seen from a distance, but a comedy when experienced up close – and I prefer the comedy because I'm always too close to my own jokes.",
]

def typewriter(text, color=None, delay=0.05):
    """
    Print text character by character to simulate a typewriter effect.
    `color` can be any ANSI code (e.g., YELLOW) or None.
    """
    for ch in text:
        sys.stdout.write(color + ch + RESET if color else ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the full text

def draw_box(content_lines, width=70):
    """
    Draw an ASCII art box around the given lines.
    Returns a list of strings representing the box with formatting.
    """
    top = f"{BOLD}{CYAN}╔{'═'*width}╗{RESET}"
    bottom = f"{BOLD}{CYAN}╚{'═'*width}╝{RESET}"
    left = f"{BOLD}{CYAN}║{RESET}"
    right = f"{BOLD}{CYAN}║{RESET}"

    box = [top]
    for line in content_lines:
        # Ensure each line fits inside the box
        padded = line.ljust(width - 2)
        box.append(f"{left} {YELLOW}{padded}{RESET} {right}")
    box.append(bottom)
    return box

def main():
    # Choose a random quote and author line
    quote = random.choice(QUOTES)
    author = "— Woody Allen"

    # Build the visual content
    lines = [quote, ""]  # empty line for spacing
    box = draw_box(lines)

    # Print the box with a typewriter effect on each line
    for line in box:
        typewriter(line, delay=0.03)
    # Print author line separately for extra flair
    print(f"{'':<4}{GREEN}{author}{RESET}")

if __name__ == "__main__":
    main()