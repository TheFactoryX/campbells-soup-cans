"""
Campbell's Soup Can #4215
Produced: 2026-07-16 06:31:17
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

colors = [91, 92, 93, 94, 95, 96]  # Red, Green, Yellow, Blue, Magenta, Cyan

quote = "I used to be indecisive. Now I'm not so sure. But I'm certain that my uncertainty is either profound wisdom or just anxiety. Either way, it's exhausting."

def print_animated_colored_text(text):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"\033[{color}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

box_width = len(quote) + 4

print("\n\033[1;37m+" + "=" * box_width + "+\033[0m")
print("\033[1;37m|" + " " * box_width + "|\033[0m")
print("\033[1;37m|  \033[0m", end="")
print_animated_colored_text(quote)
remaining_spaces = box_width - len(quote) - 2
print(" " * remaining_spaces + "\033[1;37m  |\033[0m")
print("\033[1;37m|" + " " * box_width + "|\033[0m")
print("\033[1;37m+" + "=" * box_width + "+\033[0m")
print(f"\n\033[3;97m — A neurotic philosopher probably named Woody\033[0m\n")