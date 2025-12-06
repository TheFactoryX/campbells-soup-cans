"""
Campbell's Soup Can #742
Produced: 2025-12-06 02:13:38
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
from contextlib import closing

def print_neon(text, color=37):
    styles = [30, 31, 32, 33, 34, 35, 36, 37]
    styles.remove(color)
    for char in text:
        sys.stdout.write(f"\033[{styles[color % len(styles)]}m{char}")
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()

def print_char(character, target_y, color=37):
    sys.stdout.write(f"\033[{target_y};0H\033[{color}m{character}\033[0m")
    sys.stdout.flush()

def main():
    quote = "I'm not arguing; I'm just explaining why I'm right."
    title = "WOODY ALLEN'S WISDOM"
    
    # Clear screen and hide cursor
    sys.stdout.write("\033[2J\033[?25l")
    
    # Crazy cursor animation
    rows, cols = 20, 70
    for _ in range(3):
        for y in range(1, rows-1):
            for x in range(1, cols-1):
                print_char('>' if x % 2 == 0 else '<', y, 33)
                time.sleep(0.001)
    
    # Print title
    print_neon("           WOOOOOOOOOODY ALLEN           ", 33)
    print_neon("            STYLE QUOTATIONS            ", 32)
    print()
 *4)
    
    # Print quote with box and neon effect
    for i in range(len(quote)+1):
        sys.stdout.write("\033[H\033[2J")
        print_neon(title)
        print_neon("┌─────────" + "──" * (len(quote)//2) + "────┐")
        print_neon("|" + " " * ((len(quote)//2)+10) + "|")
        print_neonce(f"|  {quote[:i].strip()}  |", 32)
        print_neon("|" + " " * ((len(quote)//2)+10) + "|")
        print_neon("└─────────" + "──" * (len(quote)//2) + "────┘")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Final appearance with blinking quote
    sys.stdout.write("\033[H\033[2J")
    print_neon(title)
    print_neon("┌─────────" + "──" * (len(quote)//2) + "────┐")
    print_neon("|        " + " " * len(quote) + "        |")
    print_neon("|  " + " " * ((len(quote)//2)+10) + "  |", 33)
    print_neon("|  " + quote + "  |", 32)
    print_neon("|  " + " " * ((len(quote)//2)+10) + "  |", 33)
    print_neon("└─────────" + "──" * (len(quote)//2) + "────┘")
    
    print()
    print_nefontsize("Press Ctrl+C to stop my neurotic ramblings", 31)

if __name__ == "__main__":
    try:
        main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\033[2J\033[0m")