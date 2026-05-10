"""
Campbell's Soup Can #3637
Produced: 2026-05-10 18:06:58
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter_effect(text, delay=0.03, color_code="\033[1;33m"):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color_code + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def blink_text(text, times=3):
    """Make text blink"""
    for i in range(times):
        sys.stdout.write(f"\033[1;31m{blink}\033[0m\n")
        time.sleep(0.1)
        sys.stdout.write(f"\033[1;31m{text}\033[0m\n")
        time.sleep(0.1)
    sys.stdout.write("\033[0m")

# ASCII Art Woody Allen looking worried
woody_art = r"""
    .-""-.
   /      \
  |  o  o  |
   \  -  /
    '-..-'
"""

# The philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Color codes
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Create the box
def print_box(text, width=50):
    box_top = f"{BLUE}{BOLD}╔{'═' * width}╗{RESET}"
    box_bottom = f"{BLUE}{BOLD}╚{'═' * width}╝{RESET}"
    
    # Center the text
    lines = text.split('\n')
    box_height = len(lines) + 2
    
    print(box_top)
    for line in lines:
        padding = (width - len(line)) // 2
        print(f"{BLUE}{BOLD}║{RESET} {line}{' ' * (width - len(line) - 2)}{BLUE}{BOLD}║{RESET}")
    print(box_bottom)

# Main display
print(f"\n{GREEN}{BOLD}")
print("╔══════════════════════════════════════════════════════════════════╗")
print("║                    WOODY ALLEN'S PHILOSOPHY                     ║")
print("╚══════════════════════════════════════════════════════════════════╝")
print(RESET)

# Print Woody Allen ASCII art with animation
print(f"{YELLOW}{BOLD}{woody_art}{RESET}")
time.sleep(0.5)

# Print the quote with typewriter effect
print(f"\n{BLUE}{BOLD}Woody says:{RESET}")
time.sleep(0.3)
typewriter_effect(f'"{quote}"{RESET}', delay=0.02, color_code=RED)

# Extra flourish
print("\n")
print(f"{GREEN}{BOLD}╔══════════════════════════════════════════════════════════════════╗")
print("║  Life is a carnival, and I'm too nervous to ride the Ferris wheel  ║")
print("╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

# Blink effect for emphasis
time.sleep(0.5)
print(f"{YELLOW}{BOLD}In other words:{RESET}")
time.sleep(0.3)
blink_text("Existence is just nature's way of saying, 'You've run out of excuses.'", times=2)