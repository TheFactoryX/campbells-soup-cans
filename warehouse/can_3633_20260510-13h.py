"""
Campbell's Soup Can #3633
Produced: 2026-05-10 13:56:03
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

# Woody Allen-style philosophical quote
quote = ("I don't fear death—I just don't want to be there when it happens. "
         "It's awkward enough showing up for my own life.")

def animate_text(text, delay):
    """Animate text by printing characters with delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_decorated_quote(quote, border_color, text_color):
    """Print a decorated animated quote box."""
    width = len(quote) + 4
    border = f"\033[{border_color}m{'—' * width}\033[0m"

    # Print top border
    print(border)

    # Print animated quote line
    sys.stdout.write(f"\033[{border_color}m| \033[0m")
    sys.stdout.write(f"\033[{text_color}m")
    animate_text(quote, 0.05)
    sys.stdout.write(f"\033[0m")
    sys.stdout.write(f"\033[{border_color}m |\033[0m")
    print()

    # Print bottom border with decorative element
    print(border)
    print(f"\033[{border_color}m( ˘ ὤ⋏ὤ ˘ )\033[0m")  # Tiny Woody face

# ANSI color codes
BORDER_COLOR = 95  # Magenta
TEXT_COLOR = 93    # Yellow

# Display the quote with animation
sys.stdout.write("\033[2J\033[;H")  # Clear screen and move cursor to top
print_decorated_quote(quote, BORDER_COLOR, TEXT_COLOR)