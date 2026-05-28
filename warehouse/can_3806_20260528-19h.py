"""
Campbell's Soup Can #3806
Produced: 2026-05-28 19:44:44
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

def colored(text, code):
    """Return text wrapped in ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def main():
    quote = "Life is like a black hole: it sucks everything in, and I’m still waiting for my refund."
    # Add padding inside the box
    inner_width = len(quote) + 2  # two spaces for left/right padding
    top_border = '+' + '-' * inner_width + '+'
    middle_template = '| {quote} |'
    
    # Color the box (cyan)
    top = colored(top_border, 36)   # 36 = cyan
    
    # Print top border
    sys.stdout.write(top + '\n')
    sys.stdout.flush()
    
    # Print left border, then animate the quote, then right border
    sys.stdout.write('| ')
    sys.stdout.flush()
    for ch in quote:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)  # typing effect
    sys.stdout.write(' |\n')
    sys.stdout.flush()
    
    # Print bottom border
    sys.stdout.write(colored(top_border, 36) + '\n')
    sys.stdout.flush()

if __name__ == "__main__":
    main()