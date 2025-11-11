"""
Campbell's Soup Can #215
Produced: 2025-11-11 22:33:04
Worker: Qwen: Qwen2.5 VL 32B Instruct (free) (qwen/qwen2.5-vl-32b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
from termcolor import colored
import os

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Define ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Create a border for the quote
def print_borders():
    width = 70
    border_top = f"{YELLOW}{'*' * width}{RESET}"
    border_middle = f"{YELLOW}*{' ' * (width - 2)}*{RESET}"
    border_bottom = f"{YELLOW}{'*' * width}{RESET}"
    print(border_top)
    print(border_middle)
    print(border_middle)
    print(border_middle)
    print(border_middle)
    print(border_bottom)

# Create an animation effect for the quote
def print_quote():
    quote = [
        "Life is like a bowl of soup—",
        "You're always chasing the last spoonful,",
        "And by the time you get there,",
        "It's just you and the noodles.",
        "",
        "Existential crisis, anyone?"
    ]
    for line in quote:
        print(line.center(70))
        time.sleep(0.5)

# Main function
def main():
    # Print initial title with colored ASCII art
    title = f"""
  {BLUE}**********   {MAGENTA}**********   {GREEN}******   {RED}*********  
  {BLUE}***  {RESET}*  *{BLUE}  ***   {RESET}*  *{BLUE}  ***    {RESET}*  *{BLUE}******   {RED}**********   {RESET}
  {BLUE}*********   {RESET}**{BLUE}     *   {RESET}**{BLUE}    *    {RESET}**{BLUE}******     {RESET}**{BLUE}****   {RESET}
  {BLUE}********** {RESET}     {BLUE}**********{RESET}       {BLUE}**********     {RESET}
  
{CYAN}Welcome to Woody Allen's Quote Machine!{RESET}
    """
    print(title)
    time.sleep(2)

    # Clear the screen and show the borders
    os.system('cls' if os.name == 'nt' else 'clear')
    print_borders()

    # Print the Woody Allen quote in a funny, self-deprecating way
    print_quote()

    # Close the borders
    print_borders()

# Run the program
if __name__ == "__main__":
    main()