"""
Campbell's Soup Can #4479
Produced: 2026-08-08 13:12:08
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def clear_screen():
    print('\033[2J', end='')
    sys.stdout.flush()

def draw_box(line, delay=0.05):
    print(f"\033[41m\033[37m{line}\033[0m")
    time.sleep(delay)

def main():
    clear_screen()
    
    box_width = 62
    border = "+" + "-" * (box_width - 2) + "+"
    draw_box(f"+{'─' * 59}+")  # Line 1
    time.sleep(0.1)
    
    # Top border with glow animation
    for char in "╔" + "═"*59 + "╗":
        sys.stdout.write(f"\033[38;5;208m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    # Quote container
    parts = [
        "\033[33m\"Остановился бы ты смертью?\033[0m",
        "\033[36m– я же не собираюсь там жить!\033[0m",
        "\033[31mА вот не дожить до конца –\033[0m",
        "\033[34mЭто уже совсем иначе.\033[0m"
    ]
    
    for i in range(59):
        print(f"\033[41m\033[37m{'|' + ' ' * 58 + '|'}\033[0m", end='\r')
        if i < len(parts):
            middle = f"| {parts[i]:^58} |"
            sys.stdout.write(f"\033[41m\033[37m{middle}\033[0m\n")
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    
    # Bottom border
    for char in "╚" + "═"*59 + "╝":
        sys.stdout.write(f"\033[38;5;208m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    # Fallout effect
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{i}...")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n\033[0m")

if __name__ == "__main__":
    main()