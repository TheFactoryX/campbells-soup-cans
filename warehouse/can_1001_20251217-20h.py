"""
Campbell's Soup Can #1001
Produced: 2025-12-17 20:38:23
Worker: Venice: Uncensored (free) (cognitivecomputations/dolphin-mistral-24b-venice-edition:free)
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
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Woody Allen style quote
quote = "If you want to make God laugh, tell him about your plans."

# Function to print colored text
def print_colored_text(text, color):
    print(f"{color}{text}{RESET}")

# ASII art frame
frame = """
+---------------------------+
|                           |
|                           |
|                           |
|                           |
|                           |
|                           |
+---------------------------+
"""

# Clear the screen
def clear_screen():
    sys.stdout.write("\033[2J\033[1;1H")

# Animation function
def animate_quote():
    clear_screen()
    print(frame)
    print_colored_text("         ", YELLOW)
    print_colored_text("         ", YELLOW)
    print_colored_text("         ", YELLOW)
    print_colored_text("         ", YELLOW)
    print_colored_text("         ", YELLOW)
    print(colored_middle_section(quote, 3))
    time.sleep(1)
    for i in range(1, 6):
        print_colored_text("         ", YELLOW)
        print(colored_middle_section(quote, i))
        time.sleep(0.5)

def colored_middle_section(text, color_choice):
    color_options = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    color = color_options[color_choice % len(color_options)]
    return f"{color}|          {text}          |{RESET}"

# Main function to display the quote
def main():
    animate_quote()

if __name__ == "__main__":
    main()