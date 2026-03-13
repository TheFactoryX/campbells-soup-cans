"""
Campbell's Soup Can #2750
Produced: 2026-03-13 21:48:29
Worker: Sao10K: Llama 3.3 Euryale 70B (sao10k/l3.3-euryale-70b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Woody Allen Quote Printer

# Import required modules
import sys
import time
import os

# Define ANSI escape codes for colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Define a function to print a quote in a colorful way
def print_quote(quote):
    """Print a quote with colorful formatting"""
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the quote in a box with colors
    print(f"{bcolors.HEADER}***************************************{bcolors.ENDC}")
    print(f"{bcolors.HEADER}*                                     *{bcolors.ENDC}")
    print(f"{bcolors.HEADER}*  {bcolors.OKGREEN}{quote}{bcolors.ENDC}  {bcolors.HEADER}*{bcolors.ENDC}")
    print(f"{bcolors.HEADER}*                                     *{bcolors.ENDC}")
    print(f"{bcolors.HEADER}***************************************{bcolors.ENDC}")

    # Print author information with animation
    animation = " Woody Allen "
    for i in range(10):
        sys.stdout.write("\r" + f"{bcolors.OKBLUE}Quote by{bcolors.ENDC}: {bcolors.HEADER}-{bcolors.ENDC}" + animation)
        sys.stdout.flush()
        time.sleep(0.5)
        animation = "  " * (len(animation) * -1)

    print("\n")

# Example usage
if __name__ == "__main__":
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print_quote(quote)