"""
Campbell's Soup Can #1823
Produced: 2026-01-24 18:46:27
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def woody_print(text, color_code, delay=0.03):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))

def main():
    quote = (
        "I'm plagued by existential dread\n"
        "and the persistent fear\n"
        "that somewhere out there,\n" 
        "someone is living a slightly more\n" 
        "interesting life than mine\n"
        "         and posting about it."
    )
    
    # ANSI color codes
    colors = {
        "yellow": "33",
        "cyan": "36",
        "white": "37",
        "purple": "35"
    }
    
    # Box border with ASCII art
    max_len = max(len(line) for line in quote.split('\n'))
    border = "╔" + "═" * (max_len + 2) + "╗"
    
    print("\n" * 2)
    woody_print(border + "\n", colors["purple"], 0.01)
    
    for line in quote.split('\n'):
        padded_line = "║ " + line.center(max_len) + " ║"
        woody_print(padded_line + "\n", colors["yellow"], 0.03)
    
    woody_print("╚" + "═" * (max_len + 2) + "╝\n", colors["purple"], 0.01)
    
    time.sleep(0.5)
    woody_print("\n          — Woody Allen's Inner Monologue\n", colors["cyan"], 0.04)
    print("\n" * 2)

if __name__ == "__main__":
    main()