"""
Campbell's Soup Can #1369
Produced: 2026-01-03 16:40:07
Worker: Venice: Uncensored (free) (cognitivecomputations/dolphin-mistral-24b-venice-edition:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# Function to clear the console screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

# ASCII art frame
frame = f"""{GREEN}
+-----------------------------------+
|                           {YELLOW}Woody Allen's Wisdom{ENDC}{GREEN}          |
+-----------------------------------+{ENDC}
"""

# Function to print the frame
def print_frame():
    print(frame)

# The philosophical quote
quote = f"""{RED}
"I'm not afraid of darkness, it just reminds me I'm not alone in being lost!"
{ENDC}
"""

# Main program
def main():
    clear_console()
    print_frame()

    # Print the quote character by character with a slight delay
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.05)

# Run the main function
if __name__ == "__main__":
    main()