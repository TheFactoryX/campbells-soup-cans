"""
Campbell's Soup Can #2309
Produced: 2026-02-19 07:18:17
Worker: OpenAI: GPT-4o-mini Search Preview (openai/gpt-4o-mini-search-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for text formatting
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Function to print text with a typing effect
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function to print a box around the text
def print_boxed(text, width=50):
    border = "+" + "-" * (width - 2) + "+"
    print(border)
    for line in text.splitlines():
        print("|" + line.center(width - 2) + "|")
    print(border)

# Main function
def main():
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "    - Woody Allen"
    )

    # Print the quote with a typing effect
    typewriter(RED + BOLD + quote + RESET, delay=0.1)

    # Print the quote inside a box
    print_boxed(RED + BOLD + quote + RESET)

if __name__ == "__main__":
    main()