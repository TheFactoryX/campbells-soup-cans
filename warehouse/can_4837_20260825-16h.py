"""
Campbell's Soup Can #4837
Produced: 2026-08-25 16:55:14
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_with_delay(text, delay=0.03, end='\n'):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def create_box(width, height, border_char='█', fill_char=' '):
    """Create a box with borders."""
    box = []
    # Top border
    box.append(border_char * width)
    # Middle lines
    for _ in range(height - 2):
        box.append(border_char + fill_char * (width - 2) + border_char)
    # Bottom border
    box.append(border_char * width)
    return box

def center_text(text, width):
    """Center text within a given width."""
    padding = (width - len(text)) // 2
    return ' ' * padding + text + ' ' * (width - len(text) - padding)

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
WHITE = '\033[97m'
BLACK_BG = '\033[40m'
BLUE_BG = '\033[44m'
YELLOW_BG = '\033[43m'

# Clear screen
print('\033[2J\033[H', end='')

# Print a dramatic introduction
print_with_delay(f"{BOLD}{CYAN}★ ★ ★ WOODY ALLEN'S EXISTENTIAL CORNER ★ ★ ★{RESET}", 0.05)
print()

# Create the quote
quote_lines = [
    f"{YELLOW}{ITALIC}\"I've been on a date that lasted 14 hours.", 
    "I didn't get home until the next day.", 
    "And when I woke up, I wasn't sure if it was a dream", 
    "or if I'd actually married the restaurant.\"{RESET}"
]

# Create a fancy box around the quote
box_width = 70
box_height = len(quote_lines) + 4
box = create_box(box_width, box_height, '═', ' ')

# Print the box with colors
for i, line in enumerate(box):
    if i == 0 or i == box_height - 1:
        # Borders
        print(f"{BLUE_BG}{WHITE}{line}{RESET}")
    else:
        # Content lines
        if i == 1:
            # Empty line
            print(f"{BLUE_BG}{WHITE}{line}{RESET}")
        elif i == box_height - 2:
            # Empty line
            print(f"{BLUE_BG}{WHITE}{line}{RESET}")
        else:
            # Quote lines
            quote_line = quote_lines[i - 2]
            centered = center_text(quote_line.replace('\033[93m\033[3m', '').replace('\033[0m', ''), box_width - 2)
            # Re-add colors
            if 'I' in quote_line:
                colored_line = centered.replace('I', f'{RED}I{RESET}')
            else:
                colored_line = centered
            print(f"{BLUE_BG}{WHITE} {colored_line} {RESET}")

print()
print_with_delay(f"{MAGENTA}— A neurotic existential crisis, brought to you by Python{RESET}", 0.05)
print()

# Add some decorative elements
print_with_delay(f"{GREEN}┌─┐┌─┐┌─┐ ┌─┐┌─┐┌─┐{RESET}", 0.1)
print_with_delay(f"{GREEN}│ ││ ││ │ └─┘│ ││ │{RESET}", 0.1)
print_with_delay(f"{GREEN}└─┘└─┘└─┘   └─┘└─┘└─┘{RESET}", 0.1)
print()

# Final philosophical musing
print_with_delay(f"{YELLOW}{BOLD}Life is like a bad haircut — it looks worse before it looks better.", 
                "But at least you learn to appreciate the bald spots.{RESET}", 0.05)
print()
print_with_delay(f"{CYAN}... and that's why I carry a comb in my pocket, just in case.{RESET}", 0.05)