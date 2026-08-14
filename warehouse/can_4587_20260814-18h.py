"""
Campbell's Soup Can #4587
Produced: 2026-08-14 18:06:20
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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

# ANSI color codes (foreground)
COLORS = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan
RESET = "\033[0m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_border():
    # a simple colorful box top and bottom
    top = "".join(chr(random.choice([9608, 9617, 9618, 9619])) for _ in range(40))
    print("\033[1;35m" + top + RESET)  # magenta bold

def typewriter(text, delay=0.04):
    for ch in text:
        color_code = random.choice(COLORS)
        sys.stdout.write(f"\033[{color_code}m{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def main():
    clear_screen()
    print_border()
    # Woody Allen‑style philosophical quote (original)
    quote = "I’m not afraid of dying; I’m just terrified of showing up to my own funeral in mismatched socks."
    print("\n")  # a little breathing room
    typewriter(quote, delay=0.05)
    print()
    print_border()
    # a tiny animated cursor blink for fun
    for _ in range(3):
        sys.stdout.write("\033[1;33m_\033[0m")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

if __name__ == "__main__":
    main()