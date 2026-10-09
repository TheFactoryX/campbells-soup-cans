"""
Campbell's Soup Can #5085
Produced: 2026-10-09 16:13:33
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import time
import sys
import random

def main():
    quote = "I've decided that the only thing I'm truly passionate about is my inability to commit to anything, including this sentence."
    border_char = '*'
    padding = 2
    width = len(quote) + padding * 2
    top_bottom = border_char * width

    # Top border
    print("\033[1;44m" + top_bottom + "\033[0m")

    # Left border
    sys.stdout.write("\033[1;44m" + border_char + " \033[0m")
    sys.stdout.flush()

    # Quote with typewriter effect
    for char in quote:
        color = f"\033[38;5;{random.randint(1,255)}m"
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)

    # Right border
    sys.stdout.write(" \033[1;44m" + border_char + "\033[0m")
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Bottom border
    print("\033[1;44m" + top_bottom + "\033[0m")

if __name__ == "__main__":
    main()