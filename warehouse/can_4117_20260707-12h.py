"""
Campbell's Soup Can #4117
Produced: 2026-07-07 12:09:19
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
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

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_slow(text, color="\033[93m", delay=0.03):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        pause = delay + random.uniform(0, 0.05)
        if char in [',', ';', '—']:
            pause += random.uniform(0.3, 0.7)
        elif char in ['.', '?', '!']:
            pause += random.uniform(0.5, 1.0)
        time.sleep(pause)
    sys.stdout.write("\033[0m")

def main():
    clear_screen()
    
    print("\033[94m\033[1m")
    print(" " * 12 + "✧✧✧  T H E   E X I S T E N T I A L   R E V I E W  ✧✧✧")
    print("\033[0m")
    time.sleep(0.8)
    
    print("\033[96m")
    print("        .---.")
    print("       ((o o))")
    print("       |  ^  |")
    print("      /|     |\\")
    print("     / |     | \\")
    print("       '-----'")
    print("\033[90m     (neurotically adjusting glasses)\033[0m")
    time.sleep(0.5)
    
    width = 75
    print()
    print("\033[95m+" + "=" * width + "+")
    print("\033[95m|" + " " * width + "|")
    
    lines = [
        "I asked the void for the meaning of life, and the void asked if I'd",
        "lost weight. We both know it was just being polite."
    ]
    
    for line in lines:
        sys.stdout.write("\033[95m| \033[0m")
        print_slow(line, color="\033[93m")
        padding = width - 2 - len(line)
        if padding > 0:
            sys.stdout.write(" " * padding)
        sys.stdout.write("\033[95m|\n")
        
    print("\033[95m|" + " " * width + "|")
    print("\033[95m+" + "=" * width + "+\033[0m")
    
    time.sleep(0.5)
    sys.stdout.write("\033[90m— Fin. \033[5m_\033[0m\n\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()