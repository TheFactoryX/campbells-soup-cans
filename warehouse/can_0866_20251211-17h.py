"""
Campbell's Soup Can #866
Produced: 2025-12-11 17:46:26
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
colors = {
    "cyan": "\033[96m",
    "pink": "\033[95m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# Create ASCII art with animation
def display_ascii():
    print("\n")
    for frame in range(1, 5):
        if frame == 1:
            print(colors["cyan"] + "   ,-.     ,-.     ,-.   " + colors["reset"])
            print(colors["cyan"] + "  ( o )  ( o )  ( o )  " + colors["reset"])
            print(colors["cyan"] + "   `-'     `-'     `-'   " + colors["reset"])
            print(colors["cyane"] + "     _____     _____     _____   " + colors["reset"])
            print(colors["cyan"] + "    /1  1\\   /2  2\\   /3  3\\  " + colors["reset"])
            print(colors["cyan"] + "   ( o   o ) ( o   o ) ( o   o ) " + colors["reset"])
            print(colors["cyan"] + "    \\___-_/   \\___-_/   \\___-_/  " + colors["reset"])
        elif frame == 2:
            print(colors["pink"] + "   ,-.     ,-.            ".center(40) + colors["reset"])
            print(colors["pink"] + "  ( o )  ( o )           ".center(40) + colors["reset"])
            print(colors["pink"] + "   `-'     `-'            ".center(40) + colors["reset"])
            print(colors["pink"] + "     _____     _____     _____   ".center(40) + colors["reset"])
            print(colors["pink"] + "    /1  1\\   /2  2\\   /3  3\\  ".center(40) + colors["reset"])
            print(colors["pink"] + "   ( o   o ) ( o   o ) ( o   o ) ".center(40) + colors["reset"])
            print(colors["pink"] + "    \\___-_/   \\___-_/   \\___-/  ".center(40) + colors["reset"])
        elif frame == 3:
            print(colors["yellow"] + "   ,-.     ,-.     ,-.   ".center(40) + colors["reset"])
            print(colors["yellow"] + "  ( o )  ( o )  ( o )  ".center(40) + colors["reset"])
            print(colors["yellow"] + "   `-'     `-'     `-'   ".center(40) + colors["reset"])
            print(colors["yellow"] + "     _____     _____     _____   ".center(40) + colors["reset"])
            print(colors["yellow"] + "    /1  1\\   /2  2\\   /3  3\\  ".center(40) + colors["reset"])
            print(colors["yellow"] + "   ( o   o ) ( o   o ) ( o   o ) ".center(40) + colors["reset"])
            print(colors["yellow"] + "    \\___-_/   \\___-_/   \\___-/  ".center(40) + colors["reset"])
        else:
            print(colors["cyan"] + "   ,-.     ,-.     ,-.   ".center(40) + colors["reset"])
            print(colors["cyan"] + "  ( o )  ( o )  ( o )  ".center(40) + colors["reset"])
            print(colors["cyan"] + "   `-'     `-'     `-'   ".center(40) + colors["reset"])
            print(colors["cyan"] + "     _____     _____     _____   ".center(40) + colors["reset"])
            print(colors["cyan"] + "    /1  1\\   /2  2\\   /3  3\\  ".center(40) + colors["reset"])
            print(colors["cyan"] + "   ( o   o ) ( o   o ) ( o   o ) ".center(40) + colors["reset"])
            print(colors["cyan"] + "    \\___-_/   \\___-_/   \\___-/  ".center(40) + colors["reset"])
        print("\n" * 2, end="")
        time.sleep(1)
        sys.stdout.write("\033[F" * 7)  # Move cursor up 7 lines

# Three-colored text
def print_colored_text(text, color1, color2, color3):
    lines = text.split('\n')
    for line in lines:
        print(f"{color1}{line[0]}{color2}{line[1:15]}{color3}{line[15:]}{colors['reset']}".center(60))

# Main program
if __name__ == "__main__":
    display_ascii()
    
    # Create the quote
    quote = (
        "I don't want to live my life a second time, because I'm completely certain "
        "I'm going to do everything wrong the first time."
    )
    
    # Display title and attribution
    print_colored_text(
        "  WOODY ALLEN ON LIFE  ", 
        colors["cyan"], 
        colors["pink"], 
        colors["yellow"]
    )
    time.sleep(1)
    print()
    print_colored_text(
        "            YOU'RE THE DUMBEST PERSON I KNOW - NEBRASKA NEBRASKE      ", 
        colors["pink"], 
        colors["yellow"], 
        colors["cyan"]
    )
    print()
    time.sleep(2)
    
    # Print the quote with typing effect
    print(colors["reset"] + "\n" + "=" * 50)
    print(colors["yellow"] + "Quote:".center(50))
    print(colors["reset"] + "=" * 50)
    print()
    
    # Printing with delayed animation
    for i, line in enumerate(quote.split()):
        animated_line = ""
        for char in line + " ":
            if i % 2 == 0:
                animated_line += f"{colors['cyan']}{char}{colors['reset']}"
            else:
                animated_line = f"{colors['yellow']}{char} " + animated_line
        print(animated_line, end='', flush=True)
        time.sleep(0.05)
        if i % 5 == 0:
            time.sleep(0.2)
    
    print()
    print(colors["reset"] + "=" * 50)
    print()
    time.sleep(2)
    
    # Final message
    print_colored_text(
        "Remember: You're only given one little spit of time in the big scheme of "
        "everything. And the spit's gonna get dry pretty fast...",
        colors["red"], 
        colors["magenta"], 
        colors["blue"]
    )
    print()
    time.sleep(1)
    print(colors["cyan"] + " :-( ".center(60) + colors["reset"])