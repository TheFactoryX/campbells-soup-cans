"""
Campbell's Soup Can #3745
Produced: 2026-05-21 19:17:09
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def animate_text(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(f"\033[{color}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote_lines = [
        "I'm not afraid of dying—I just",
        "don't want to be there when it",
        "happens. Especially not during rush hour."
    ]
    
    max_line_length = max(len(line) for line in quote_lines)
    box_width = max_line_length + 4  # 2 for | and space on each side
    
    # Top border
    top_border = '+' + '-' * (box_width - 2) + '+'
    animate_text(top_border, '91', 0.01)  # Red border
    
    for line in quote_lines:
        padded_line = f"| {line.center(max_line_length)} |"
        animate_text(padded_line, '93', 0.05)  # Yellow text
    
    # Bottom border
    animate_text(top_border, '91', 0.01)
    
if __name__ == "__main__":
    main()