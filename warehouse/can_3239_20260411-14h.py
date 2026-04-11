"""
Campbell's Soup Can #3239
Produced: 2026-04-11 14:55:18
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single‑file, self‑contained Python program that prints
a funny Woody‑Allen‑style philosophical quote.
It uses ANSI escape codes for color, a little animation,
and a cute ASCII frame to make the output visually interesting.
"""

import sys
import time
import random
import os

# ANSI color definitions
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

# The Woody‑Allen‑style quote
QUOTE = (
    "I stopped sleeping on a bed of roses,\n"
    "and started sleeping on a pile of existential dread.\n"
    "I thought I could avoid death, but I just kept postponing it to the next coffee break."
)

# ASCII frame characters
FRAME_LEFT   = "╭"
FRAME_RIGHT  = "╮"
FRAME_BOTTOM = "─"
FRAME_CORNER = "┴"
FRAME_PLANE  = "│"
FRAME_BOTLEFT  = "╰"
FRAME_BOTRIGHT = "╯"

def clear_screen():
    """Clear the terminal screen in a cross‑platform way."""
    os.system("cls" if os.name == "nt" else "clear")

def animate_print(text, delay=0.05, flicker=False):
    """Print text with a typing animation. Optionally flicker letters."""
    for ch in text:
        if flicker and ch != "\n":
            sys.stdout.write(f"{random.choice([RED,BOLD,YELLOW])}{ch}{RESET}")
        else:
            sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def draw_box(lines, padding=1):
    """Draw a rectangular box around the given lines of text."""
    max_len = max(len(line.replace("\x1b[31m","").replace("\x1b[0m","")) for line in lines)
    width = max_len + 2 * padding + 2
    top = FRAME_LEFT + FRAME_BOTTOM * (width - 2) + FRAME_RIGHT
    bottom = FRAME_BOTLEFT + FRAME_BOTTOM * (width - 2) + FRAME_BOTRIGHT
    print(f"{CYAN}{BOLD}{top}{RESET}")
    for line in lines:
        stripped = len(line.split("\x1b[")[0])  # naive length without ANSI
        pad_space = " " * padding
        space_needed = max_len - stripped
        print(f"{CYAN}{FRAME_PLANE}{RESET} {pad_space}{line}{pad_space}{' ' * space_needed} {CYAN}{FRAME_PLANE}{RESET}")
    print(f"{CYAN}{bottom}{RESET}")

def main():
    clear_screen()
    # Welcome banner with a dash of flair
    banner_lines = [
        f"{MAGENTA}{BOLD}  .d8888b.  .d8888b.  .d8888b.  .d8888b.",
        f"  d88P  Y88b d88P  Y88b d88P  Y88b d88P  Y88b",
        f"  888    888 888    888 888    888 888    888",
        f"  888        888   888  888    888 888    888",
        f"  888  88888 8888888888 888    888 888    888",
        f"  888    888 888    888 888    888 888    888",
        f"  888    888 888    888 888    888 888    888",
        f"  Y8888888P  Y8888888P Y8888888P  Y8888888P"
    ]
    banner_lines = [f"{GREEN}{line}{RESET}" for line in banner_lines]
    draw_box(banner_lines, padding=2)

    time.sleep(1)

    # Animate the quote
    quote_lines = QUOTE.split("\n")
    # Make each line a bit random color for mood
    color_options = [RED, YELLOW, MAGENTA]
    for i, line in enumerate(quote_lines):
        color = random.choice(color_options)
        animated_line = f"{color}{BOLD}{line}{RESET}"
        animate_print(animated_line, delay=0.03)
        time.sleep(0.2)

    time.sleep(0.5)
    # Final flourish
    flourish = f"{BLUE}{BOLD}—Stay quirky, my existential nerds!{RESET}"
    animate_print(flourish, delay=0.07)

if __name__ == "__main__":
    main()