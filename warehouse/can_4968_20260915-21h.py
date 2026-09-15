"""
Campbell's Soup Can #4968
Produced: 2026-09-15 21:23:13
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter_effect(text, color_code):
    """Print text with typewriter effect in specified color using ANSI codes."""
    colored_text = f"{color_code}{text}"
    for c in colored_text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    # Reset color and add newline
    print('\033[0m')

def main():
    # Woody Allen-inspired philosophical quote (self-deprecating and existential)
    quote = "The secret to my success is that I never stopped to ask if I'm failing. Which means I'm probably failing anyway."

    # Calculate box dimensions based on quote length
    quote_length = len(quote)
    box_width = quote_length + 6  # Add padding for aesthetics

    # Create borders using ANSI color codes
    top_border = f"\033[36m+{('-' * (box_width - 2))}+\033[0m"
    
    # Empty lines above and below the quote
    empty_line = f"| {' ' * (box_width - 2)} |"

    # Print the box with typewriter effect for the quote line
    print(top_border)
    print(f"\033[97m{empty_line}\033[0m")  # Empty top line in white
    
    # Display the quote itself using a slow typing effect in yellow
    typewriter_effect(f"| {quote} |", "\033[93m")
    
    # Empty bottom line in white
    print(f"\033[97m{empty_line}\033[0m")
    
    # Print bottom border in cyan
    print(top_border)

if __name__ == "__main__":
    main()