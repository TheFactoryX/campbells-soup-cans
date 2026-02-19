"""
Campbell's Soup Can #2311
Produced: 2026-02-19 10:05:42
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import random
import sys

# ANSI escape sequences for colors, effects, and formatting
COLORS = {
    'red': '\033[38;5;1m',
    'green': '\033[38;5;34m',
    'yellow': '\033[38;5;214m',
    'blue': '\033[38;5;46m',
    'purple': '\033[38;5;201m',
    'cyan': '\033[38;5;51m',
    'magenta': '\033[38;5;208m',
    'black': '\033[30m',
    'white': '\033[38;5;232m',
    'bold': '\033[1m',
    'reset': '\033[0m',
    'inverse': '\033[7m',
    'bg_red': '\033[48;5;1m',
    'bg_green': '\033[48;5;22m',
    'bg_blue': '\033[48;5;39m',
    'bg_yellow': '\033[48;5;211m',
    'style_z': '\033[%s;%sd'  # Zombie-style message animation
}

# Quotes that capture the neurotic, existential flair
QUOTES = [
    "I'm not afraid of death; I just don't want to miss my favorite sitcom rerun.",
    "Life is like a PDF file on a CD-ROM - nobody knows what the hell is inside, and it's all grayed out.",
    "I tried to find peace in the chaos, but then I remembered I never had any peace to begin with.",
    "I’d give up my existence for a good quiche. The universe won’t let me, though.",
    "I felt alive once. Now I just feel like a poorly architected Python script waiting for GC."
]

class WoodyThought:
    def __init__(self):
        self.colors = list(COLORS.values()) + [COLORS['inverse'], COLORS['bold']]
        self.quote = random.choice(QUOTES)
    
    def squeeze_text(self, text, width=80):
        """Squishes text with ANSI art for a slack-jawed look"""
        return f"{COLORS['red']}<--(;ゝ_<)\n{text.center(width, ' ')}"
    
    def print_quote(self):
        # Top bar
        print(f"{COLORS['red']}/~.~~/\n{' ' * (10)}{'='*20}\n~/.~ →")
        
        # Main quote block
        for _ in range(3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{COLORS['cyan']}╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
            print(f" {random.choice(['', '', '', '', ' '])}
                {COLORS['magenta']}+───────+
                {COLORS['gray']}{self.squeeze_text(self.quote)[:70]}{RESET}
            {COLORS['blue']}║───███║─)
                {COLORS['yellow']}"{'\033[3m' + self.quote + '\033[0m'"
            print(f" {COLORS['cyan']}║     /  │\n   ██ Generation Error: {random.randint(1000,9999)} {random.choice([' buffer overflow', ' segmentation fault', ' syntax error', ' undefined method'])}\n")
            print(f"{COLORS['red']}╚╝{self.quote}")
            print(COLORS['reset'])
            time.sleep(0.5)
        
        # Final display with text flicker
        for i in range(5):
            clear_screen()
            print(f"{COLORS['white']}z o m g\n".
                   f"                       {random.choice([self.quote, '', ' ', '█', '╳', '┼', '─', '┴', '╢', '╠', '╥', '╤'])}".ljust(60),
            time.sleep(0.15)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    th = WoodyThought()
    while True:
        clear_screen()  # Clear previous output
        print(f"{COLORS['purple']}Theater Spotlight effect{RESET}")
        time.sleep(0.3)
        print(f"{COLORS['purple']}\n{time.strftime('%H:%M:%S')}\n{random.choice(['Radio Static', 'Netflix Buffering', 'Internal Monologue'])}")
        time.sleep(0.3)
        th.print_quote()
        input(f"{COLORS['purple']}Press ENTER to exit demolishing your cynicism {RESET}")

if __name__ == "__main__":
    main()
