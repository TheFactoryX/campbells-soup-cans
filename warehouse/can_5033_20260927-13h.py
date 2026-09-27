"""
Campbell's Soup Can #5033
Produced: 2026-09-27 13:59:42
Worker: DeepSeek: DeepSeek V4 Flash Vision Exp (deepseek/deepseek-v4-flash-vision-exp)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def set_color(code):
    sys.stdout.write(f"\033[{code}m")
    sys.stdout.flush()

def reset():
    sys.stdout.write("\033[0m")
    sys.stdout.flush()

def type_text(text, delay=0.05, color_code=None):
    for ch in text:
        if color_code:
            set_color(color_code)
        else:
            set_color(random.randint(31, 36))
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    reset()
    print()

def draw_box_animated(text, padding=2, delay=0.04):
    width = len(text) + 2 * padding + 2

    # Top border
    set_color(33)
    print("+" + "-" * (width - 2) + "+")

    # Empty line
    print("|" + " " * (width - 2) + "|")

    # Quote line (with typing animation)
    set_color(33)
    sys.stdout.write("|" + " " * padding)
    for ch in text:
        set_color(random.randint(31, 36))
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

    set_color(33)
    sys.stdout.write(" " * padding + "|")
    sys.stdout.write("\n")

    # Empty line
    print("|" + " " * (width - 2) + "|")

    # Bottom border
    set_color(33)
    print("+" + "-" * (width - 2) + "+")
    reset()

def main():
    clear()

    # Header
    set_color(35)
    print("=" * 60)
    reset()

    title = " A MOMENT OF WOODY ALLEN PHILOSOPHY "
    for i, ch in enumerate(title):
        set_color(31 + (i % 6))
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    reset()
    print()

    set_color(35)
    print("=" * 60)
    reset()
    print()

    # Intro line
    type_text("I was having one of my existential thoughts...", delay=0.03, color_code=34)
    print()

    # The philosophical quote
    quote = "I'm not afraid of death, but I'm terrified of the waiting room."
    draw_box_animated(quote, padding=2, delay=0.04)

    print()
    time.sleep(0.5)

    # Signature
    set_color(36)
    sys.stdout.write("  — Woody Allen")
    reset()
    print()

    # Exit message
    time.sleep(1)
    print()
    set_color(32)
    print("Press Ctrl+C to exit...")
    reset()

    time.sleep(2)

if __name__ == "__main__":
    main()