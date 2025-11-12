"""
Campbell's Soup Can #232
Produced: 2025-11-12 17:33:48
Worker: Meta: Llama 4 Scout (free) (meta-llama/llama-4-scout:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
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

def print_boxed_quote(quote, author, color):
    print(f"{color}╔═══════════════════════════════════╗{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC} {quote} {bcolors.ENDC}║")
    print(f"{color}║{bcolors.ENDC}  - {author} {bcolors.ENDC}║")
    print(f"{color}╚═══════════════════════════════════╝{bcolors.ENDC}")

def main():
    quote = "I'm not afraid of death; I just don't want to be there when my therapist is."
    author = "Woody Allen (maybe?)"

    print("\n")
    time.sleep(0.5)
    print(f"{bcolors.OKCYAN}Loading existential dread...{bcolors.ENDC}")
    time.sleep(0.5)

    print("\n")
    print_boxed_quote(quote, author, bcolors.OKBLUE)

    print("\n")
    time.sleep(0.5)
    print(f"{bcolors.FAIL}Press Ctrl+C to escape the meaninglessness of life.{bcolors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{bcolors.WARNING}You've managed to temporarily escape. Until next time.{bcolors.ENDC}")