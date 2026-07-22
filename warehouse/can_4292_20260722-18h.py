"""
Campbell's Soup Can #4292
Produced: 2026-07-22 18:33:51
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def animate_frame(text, frame, colors):
    current_color = colors[frame % len(colors)]
    return f"\033[1;{current_color}m{text[:frame*2]}{f'▓' * (len(text) - frame*2)}"

def show_quote():
    quote = [
        "\\|/__________________________________________________|/|\\",
        " \\|/   Life is meaningless, but then again, so am I.   /|\\",
        "  \\|                    Nor am I particularly good at it.   /|",
        "   \\|           Yet here we all are, fumbling along.         /|",
        "    \\|                 Why bother? Why not? Maybe.          /|",
        "     \\|             Philosophizing ≠ results.              /|",
        "      \\|             -Woody Allen Rejects Existentialism  / |",
        "       \\|____________________________________☕____________/|",
    ]
    
    colors = ["0;31;40", "0;32;40", "0;33;40", "0;34;40"]
    width = 75
    
    middle_index = len(quote) // 2
    lines = list(quote)
    lines.insert(middle_index, " " * (width - 4) + "▓▓▓▓")
    
    for i in range(len(lines) * 2):
        sys.stdout.write('\r' + '\033[H' + '\n' * max(0, width // 2 - 1))
        frame = i
        header = animate_frame("     \u25cb  THE ABYSS OF MEANINGLESSNESS  \u25cb  ", frame, colors)
        body = animate_frame(lines[(i % len(lines))], frame, colors)
        sys.stdout.write(header + '\n' + body + '\n' + ' ' * width + f'\033[{frame%2+30}m|\n')
        time.sleep(0.05)

if __name__ == "__main__":
    show_quote()