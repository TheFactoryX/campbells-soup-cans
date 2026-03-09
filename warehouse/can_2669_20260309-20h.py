"""
Campbell's Soup Can #2669
Produced: 2026-03-09 20:51:15
Worker: OpenAI: GPT-4o (extended) (openai/gpt-4o:extended)
Employment: Paid
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
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# ASCII Art components
frame_top_bottom = '+-' + '-'*39 + '-+'
frame_middle = '| ' + ' '*39 + ' |'

quote = "Life is divided into the horrible and the miserable. \n"
quote += "That's the two categories. The horrible would be like, \n"
quote += "I don't know, terminal cases, blind people, cripples. \n"
quote += "I don't know how they get through life. It's amazing to me. \n"
quote += "And the miserable is everyone else. So you should be thankful \n"
quote += "that you're miserable, because that's very lucky, to be miserable."

# Function to print the frame for the quote
def print_frame():
    print(RED + frame_top_bottom)
    for _ in range(8):
        print(RED + frame_middle)
    print(RED + frame_top_bottom + RESET)

# Function to print the quote letter by letter with animation
def print_quote(animated_quote):
    x,y = 2,1  # starting cursor position for quote inside the frame
    sys.stdout.write("\033[2J")  # clear terminal
    sys.stdout.write("\033[H")   # move cursor to home position
    print_frame()                # draw the initial frame
    for line in animated_quote.split("\n"):
        for char in line:
            sys.stdout.write(f"\033[{y};{x}H")  # move cursor to position
            sys.stdout.write(GREEN + char + RESET)
            sys.stdout.flush() 
            x += 1
            if x > 40:   # wrap text after 40 characters (frame width)
                x = 2
                y += 1
        x = 2
        y += 1
    sys.stdout.write("\033[49;0H")  # move cursor to a safe spot

# Main function
def main():
    print_quote(quote)
    time.sleep(5)  # wait for few seconds to let user read the quote

if __name__ == "__main__":
    main()