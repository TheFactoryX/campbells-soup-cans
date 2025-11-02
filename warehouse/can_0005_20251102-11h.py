"""
Campbell's Soup Can #5
Produced: 2025-11-02 11:25:01
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, color‑rich Python script that prints a single Woody
Allen‑style philosophical quote in a typewriter animation inside
a framed box.
"""

import sys
import time
import shutil

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE  = "\033[34m"
MAGENTA = "\033[35m"
CYAN  = "\033[36m"
WHITE = "\033[37m"

# The Woody‑Allen‑style quote
QUOTE = (
    "Philosophy is an overpaying investment in the real estate of danger— "
    "my apartment is called ‘Existential’, and the rent is my panic."
)

# Determine terminal width for optional centering
term_size = shutil.get_terminal_size(fallback=(80, 24))
term_width = term_size.columns

# Box dimensions
PADDING_X = 2  # spaces inside the box on left/right
PADDING_Y = 1  # lines inside the box on top/bottom
border_chars = ("╔", "╗", "╚", "╝", "═", "║")

def create_empty_box(quote_width, pad_x, pad_y):
    """Return an empty box of given width and padding."""
    inner_width = quote_width + 2 * pad_x
    top = f"{border_chars[0]}{border_chars[4]*inner_width}{border_chars[1]}"
    side = f"{border_chars[5]}"
    bottom = f"{border_chars[2]}{border_chars[4]*inner_width}{border_chars[3]}"
    empty_line = f"{side}{' '*inner_width}{side}"
    # Lines: top + pad_y empty lines + bottom
    return [top] + [empty_line]*pad_y + [bottom]

def typewriter_effect(text, color=YELLOW, delay=0.05):
    """Print the box with characters appearing one by one."""
    # Prepare the box template
    box = create_empty_box(len(text), PADDING_X, PADDING_Y)
    displayed = ""
    for i in range(len(text)+1):
        # Update displayed substring
        displayed = text[:i]
        # Build the inner line with padding
        inner_width = len(text) + 2 * PADDING_X
        inside = (
            " " * PADDING_X +  # left padding
            displayed.ljust(inner_width - 2 * PADDING_X) +  # text
            " " * PADDING_X  # right padding
        )
        # Replace the middle line of the box
        middle_index = 1 + PADDING_Y  # after top + pad_y lines
        box[middle_index] = f"{border_chars[5]}{inside}{border_chars[5]}"
        # Clear the screen (optional for animation)
        sys.stdout.write("\033[H\033[J")  # cursor to home, clear screen
        # Optionally center the box on the terminal
        box_str = "\n".join(box)
        lines = box_str.splitlines()
        # Build final output
        out_lines = []
        for line in lines:
            if len(line) < term_width:
                # Center horizontally
                left_padding = (term_width - len(line)) // 2
                out_lines.append(" " * left_padding + line)
            else:
                out_lines.append(line)
        final_output = BOLD + color + "\n".join(out_lines) + RESET
        sys.stdout.write(final_output)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    """Main function to run the typewriter animation."""
    typewriter_effect(QUOTE)
    # Keep the final frame until user presses Enter
    sys.stdout.write("\n\nPress Enter to exit...")
    sys.stdin.readline()

if __name__ == "__main__":
    main()
