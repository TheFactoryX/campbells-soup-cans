"""
Campbell's Soup Can #1346
Produced: 2026-01-02 15:34:29
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end="")

def typewriter(text, color=37, delay=0.04):
    for char in text:
        sys.stdout.write(f"\033[{color}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.8, 1.2))
    print()

def main():
    quote = (
        "You know, I finally figured out why the universe is expanding...\n"
        "It's trying to get away from my existential dread.\n"
        "But at the speed of light? Is that really necessary?"
    )
    
    colors = [31, 33, 35, 36]  # Red, Yellow, Purple, Cyan
    border_color = random.choice(colors)
    
    print("\n" * 2)
    typewriter(" " * 15 + "─" * 50, border_color)
    
    time.sleep(0.3)
    typewriter(" " * 15 + "│" + " " * 48 + "│", border_color)
    
    time.sleep(0.2)
    for line in quote.split('\n'):
        typewriter(" " * 15 + "│  " + line.center(46) + "  │", random.choice(colors))
        time.sleep(0.2)
    
    time.sleep(0.1)
    typewriter(" " * 15 + "│" + " " * 48 + "│", border_color)
    time.sleep(0.1)
    typewriter(" " * 15 + "─" * 50, border_color)
    
    # Woody Allen signature
    print("\n" + " " * 60, end="")
    typewriter("─ Woody Allen " + "\u2022" * 5, 37, 0.05)
    print("\n" * 2)

if __name__ == "__main__":
    main()