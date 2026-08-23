"""
Campbell's Soup Can #4791
Produced: 2026-08-23 14:40:11
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def print_colored_char(char, color_code):
    sys.stdout.write(f"{color_code}{char}\033[0m")
    sys.stdout.flush()

def main():
    sys.stdout.write('\033[2J\033[H')  # Clear screen and move home
    
    quote = [
        "Suffering is inevitable, but my ability to feel sorry for myself is what",
        "truly defines me."
    ]
    
    max_line = max(len(line) for line in quote) + 2  # Plus 2 for left/right borders
    border = '+' + '-' * (max_line - 2) + '+'
    border_length = len(border)
    
    # Colors: top/bottom border in blue, lines in rainbow
    border_color = '\033[1;34m'  # Bright blue
    line_colors = [
        '\033[31m',  # Red
        '\033[36m',  # Cyan
        '\033[32m',  # Green
    ]
    
    def animate_border(text, delay=0.015):
        for c in text:
            if c in '+-':
                print_colored_char(c, border_color)
            else:
                print_colored_char(c, '\033[0m')  # Reset for '+'
            time.sleep(delay)
        print()
        time.sleep(0.5)
    
    # Animate top border
    animate_border(border)
    print('\033[F', end='')  # Move cursor up
    
    # Print quote lines with animation
    for i, line in enumerate(quote):
        centered = line.center(max_line - 2)  # Adjust for borders
        full_line = f"|{centered}|"
        line_color = line_colors[i % len(line_colors)]
        
        for c in full_line:
            if c == '|':
                print_colored_char(c, border_color)
            elif c == ' ':
                print_colored_char(c, '\033[0m')
            else:
                print_colored_char(c, line_color)
            time.sleep(0.012)
        print()
        time.sleep(0.4)
    
    # Finalize with bottom border
    print('\n')
    animate_border(border)
    
    # Add philosophical afterthought
    sys.stdout.write('\033[1;93m')
    sys.stdout.write("  - Woody Allen would probably say this about himself too\n")
    sys.stdout.flush()
    time.sleep(1)

if __name__ == "__main__":
    main()