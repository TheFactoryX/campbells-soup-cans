"""
Campbell's Soup Can #93
Produced: 2025-11-06 11:28:44
Worker: Qwen2.5 Coder 32B Instruct (free) (qwen/qwen-2.5-coder-32b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Frame delay for animation
DELAY = 0.1

# Function to print a line with a delay
def print_with_delay(text, color=RESET):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(DELAY)
    print()

# Function to clear the screen
def clear_screen():
    print("\033c", end="")

# Function to print the top and bottom borders of the quote box
def print_border():
    border = " " + "=" * 78 + " "
    print_with_delay(border, BLUE)

# Function to print the actual quote in a centered format with color
def print_quote():
    quote = "In my younger and more vulnerable years, my father gave me some advice that I’ve been turning over in my mind ever since." \
            "\n'We may have all come on different ships,' he said, 'but we're in the same boat.'"
    lines = quote.split('\n')
    for line in lines:
        padded_line = f"| {line:<76} |"
        print_with_delay(padded_line, GREEN)

# Main function to animate the display of the quote
def display_quote():
    clear_screen()
    print_border()
    time.sleep(DELAY * 2)
    print_quote()
    time.sleep(DELAY * 2)
    print_border()

# Function to add a playful Woody Allen themed outro
def outro():
    clear_screen()
    outro_text = "  ... but who really knows if we're even in the same ocean? "
    print_with_delay(outro_text, YELLOW)

# Main sequence
display_quote()
time.sleep(DELAY * 3)
outro()