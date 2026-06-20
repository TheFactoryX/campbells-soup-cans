"""
Campbell's Soup Can #3974
Produced: 2026-06-20 16:51:09
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

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def animate_print(text, delay=0.03):
    """Prints text character by character with animation effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Decorative introduction
print(f"\n{MAGENTA}{'=' * 50}{RESET}")
animate_print(f"{CYAN}{BOLD}Philosophical Musings by a Neurotic Mind{RESET}", 0.05)
print(f"{MAGENTA}{'=' * 50}{RESET}\n")

# The main quote content
quote_lines = [
    f"{GREEN}I've spent so much time{RESET}",
    f"{YELLOW}worrying about death{RESET}",
    f"{BLUE}that I've forgotten to live...{RESET}",
    f"{RED}which is probably just as well,{RESET}",
    f"{MAGENTA}because living seems to involve{RESET}",
    f"{CYAN}a lot of walking and conversation.{RESET}",
    f"{GREEN}And I'm pretty sure {RED}existential dread{BOLD}{GREEN} counts as cardio.{RESET}"
]

# Animated quote presentation
for line in quote_lines:
    time.sleep(0.5)  # Pause before each line
    animate_print(line.center(60))

# Closing animation
print(f"\n{MAGENTA}{'-' * 50}{RESET}")
time.sleep(0.3)
animate_print(f"{RED}Total runtime anxiety:  ∞{RESET}", 0.1)
time.sleep(0.5)
animate_print(f"{BLUE}(But this quote was only 1.21 seconds long!){RESET}", 0.03)

# Final flourish
print(f"\n{MAGENTA}{'=' * 50}{RESET}")
sys.exit(0)