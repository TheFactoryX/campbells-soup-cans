"""
Campbell's Soup Can #3511
Produced: 2026-04-30 20:19:22
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
]
RESET = "\033[0m"

def color_text(text, color_code):
    return f"{color_code}{text}{RESET}"

def draw_box(content, border_color):
    lines = content.split("|")
    width = max(len(line) for line in lines) + 4
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = []
    for line in lines:
        padded = line.center(width - 2)
        middle.append("║" + padded + "║")
    box = [top_bottom] + middle + [top_bottom]
    colored = [color_text(line, border_color) for line in box]
    return "\n".join(colored)

def main():
    quote = (
        "I don't fear the void; I just hope it has decent Wi‑Fi.\n"
        "|                                   |\n"
        "|  Life is a tragicomedy where the  |\n"
        "|  punchline is always missed, and  |\n"
        "|  the intermission lasts forever.  |"
    )
    # Animation: cycle colors a few times
    for _ in range(3):
        for col in COLORS:
            sys.stdout.write("\033[2J\033[H")  # Clear screen
            sys.stdout.write(draw_box(quote, col))
            sys.stdout.flush()
            time.sleep(0.2)
    # Final display in a bright cyan
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(draw_box(quote, COLORS[5]))
    sys.stdout.flush()

if __name__ == "__main__":
    main()