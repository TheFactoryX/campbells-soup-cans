"""
Campbell's Soup Can #4185
Produced: 2026-07-13 19:49:07
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def animate_spinner():
    """Fun little spinner animation before the quote"""
    spinner = ['|', '/', '-', '\\']
    for _ in range(4):
        for char in spinner:
            sys.stdout.write(f'\r{WHITE}Overthinking in progress... {char}{RESET}')
            sys.stdout.flush()
            time.sleep(0.1)

def type_with_flair(text, delay=0.03):
    """Prints text with typing effect and color"""
    for char in text:
        sys.stdout.write(f'{YELLOW}{char}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(lines):
    """Draws a decorative box around the quote"""
    width = max(len(line) for line in lines) + 4
    print(f'{CYAN}╔{"═" * width}╗')
    for line in lines:
        print(f'║ {line.center(width-2)} ║')
    print(f'╚{"═" * width}╝{RESET}')

# ANSI Color Codes
WHITE = '\033[97m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# The Woody Allen-style quote
quote = [
    f"{RED}I told my therapist about my fear of existential dread.{RESET}",
    f"{GREEN}He said, 'That's very profound.'{RESET}",
    f"{YELLOW}Now I'm worried I'm not profound enough.{RESET}"
]

animate_spinner()
print(f'\n{WHITE}Here’s my latest philosophical breakthrough:{RESET}\n')

draw_box(quote)

# Bonus ASCII art of a neurotic brain
print(f"{CYAN}")
print("       ___")
print("     /     \\")
print("    |  O O  |")
print("    |   >   |")
print("     \\ ___ /")
print("       | |")
print("      /   \\")
print("     /_____",)

# Wait a moment at the end
time.sleep(0.5)
print(f"\n{WHITE}...and that's why I'm switching to aromatherapy.{RESET}")