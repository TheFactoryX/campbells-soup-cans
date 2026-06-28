"""
Campbell's Soup Can #4039
Produced: 2026-06-28 16:36:36
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

# Woody Allen-style philosophical quote
woody_quote = "I spent decades seeking enlightenment, only to find it was hiding behind my couch cushions next to the remote and my dignity."

# ANSI color codes
COLORS = {
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

# Animated spinner before reveal
def pre_show_animation():
    spinner = ['|', '/', '-', '\\']
    for _ in range(12):
        for spin in spinner:
            print(f"{COLORS['blue']}{spin}{COLORS['reset']}", end='\r', flush=True)
            time.sleep(0.07)
    print(" " * 3, end='\r')  # Clear spinner
    time.sleep(0.3)

# Star pattern reveal
def star_reveal():
    stars = [
        "      ✨      ",
        "     🌟🌟     ",
        "    🌟🌟🌟    ",
        "   🌟🌟🌟🌟   ",
        "  🌟🌟🌟🌟🌟  ",
        " 🌟🌟🌟🌟🌟🌟 ",
        "🌟🌟🌟🌟🌟🌟🌟🌟🌟",
        " 🌟🌟🌟🌟🌟🌟 ",
        "  🌟🌟🌟🌟🌟  ",
        "   🌟🌟🌟🌟   ",
        "    🌟🌟🌟    ",
        "     🌟🌟     ",
        "      ✨      "
    ]
    for line in stars:
        print(f"{COLORS['yellow']}{line}{COLORS['reset']}")
        time.sleep(0.1)

# Animated quote reveal in a box
def quote_animation():
    box_width = len(woody_quote) + 6
    top_border = f"{COLORS['blue']}┏{'━' * (box_width - 2)}┓{COLORS['reset']}"
    bottom_border = f"{COLORS['blue']}┗{'━' * (box_width - 2)}┛{COLORS['reset']}"
    
    print(top_border)
    
    # Animated quote line
    print(f"{COLORS['blue']}┃ {COLORS['yellow']}{COLORS['bold']}", end='')
    for char in woody_quote:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print(f"{COLORS['reset']} ┃")
    
    print(bottom_border)

# Main execution sequence
pre_show_animation()
star_reveal()
time.sleep(0.5)
quote_animation()