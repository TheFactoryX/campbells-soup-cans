"""
Campbell's Soup Can #1855
Produced: 2026-01-26 08:50:39
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors and styles
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

def print_with_delay(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = "I'm not saying life is meaningless, but if it were a book,\nI'd return it for a better plot twist."
    author = "- Woody Allen's Python Script"

    # Create a box around the text
    box_width = max(len(line) for line in quote.split('\n')) + 4
    top_bottom = MAGENTA + '*' * (box_width + 4) + RESET
    spacer = MAGENTA + '*' + ' ' * (box_width + 2) + '*' + RESET

    # Animated display
    print('\n' * 2)
    print_with_delay(top_bottom)
    print_with_delay(spacer)
    
    for line in quote.split('\n'):
        padded_line = line.center(box_width)
        print_with_delay(MAGENTA + "*  " + RESET + YELLOW + padded_line + RESET + MAGENTA + "  *" + RESET)
    
    print_with_delay(spacer)
    print_with_delay(MAGENTA + '*  ' + RESET + CYAN + author.center(box_width) + RESET + MAGENTA + '  *' + RESET)
    print_with_delay(spacer)
    print_with_delay(top_bottom)
    
    # Keep window open
    input("\n\n(Press Enter to escape existential crisis)")

if __name__ == "__main__":
    main()