"""
Campbell's Soup Can #704
Produced: 2025-12-04 07:33:21
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_woody_allen_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print("\033[1;31;40m")  # Set text color to red
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.1)  # Delay between each character
    print("\033[0m")  # Reset text color

def main():
    print_woody_allen_quote()

if __name__ == "__main__":
    main()