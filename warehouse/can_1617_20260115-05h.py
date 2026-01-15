"""
Campbell's Soup Can #1617
Produced: 2026-01-15 05:43:15
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
BLINK = '\033[5m'

# Woody Allen-style quote
quote = (
    f"{ITALIC}Life is absurdly short{YELLOW} - just when you finally get the hang of "
    f"temporal existence,{RESET}{ITALIC}\nyou realize you've been standing in "
    f"{CYAN}metaphysical line{RESET}{ITALIC} for the cosmic bathroom.{RESET}\n"
    f"{BLINK}{MAGENTA}(And of course, there's no toilet paper.){RESET}"
)

# ASCII art with animation
def display_animated_art():
    frames = [
        r"    (\   /)     ",
        r"    (•ᴗ•) 🕒    ",
        r"    / 　 \      ",
        r"   ╰┬┴┬╯       "
    ]
    for frame in frames:
        print(f"\033[H{MAGENTA}{frame}{RESET}")
        time.sleep(0.3)
        sys.stdout.flush()

# Print text with typewriter effect
def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char not in ['\n', ' ']:
            time.sleep(delay)

# Main program
print('\033[2J\033[H')  # Clear screen
display_animated_art()
time.sleep(0.5)

# Calculate box dimensions
lines = quote.split('\n')
max_length = max(len(line.replace('\033[0m', '').replace('\033[3m', '').replace('\033[33m', '').replace('\033[36m', '').replace('\033[35m', '').replace('\033[5m', '')) for line in lines)
box_width = max_length + 4

# Print fancy box
print(f"\033[H{MAGENTA}╭{'─' * box_width}╮{RESET}")
for line in lines:
    cleaned_length = len(line.replace('\033[0m', '').replace('\033[3m', '').replace('\033[33m', '').replace('\033[36m', '').replace('\033[35m', '').replace('\033[5m', ''))
    padding = ' ' * (box_width - cleaned_length - 2)
    print(f"{MAGENTA}│{RESET} {BOLD}{line}{padding} {MAGENTA}│{RESET}")
    time.sleep(0.2)
print(f"{MAGENTA}╰{'─' * box_width}╯{RESET}")

# Type the quote with delay
print("\n")
type_text(quote)
print("\n")

# Keep the terminal from closing immediately
input("\nPress Enter to confront the existential void...")