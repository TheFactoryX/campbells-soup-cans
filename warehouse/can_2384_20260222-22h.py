"""
Campbell's Soup Can #2384
Produced: 2026-02-22 22:44:36
Worker: OpenAI: GPT-4o (2024-11-20) (openai/gpt-4o-2024-11-20)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ASCII art border
BORDER = f"""
{YELLOW} **********************
{YELLOW}*{RESET}                      {YELLOW}*
{YELLOW} **********************{RESET}
"""

# Function to print character-by-character with delay
def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# The quote
QUOTE = (
    f"{CYAN}{BOLD}"
    "  'The key to happiness is to avoid thinking about the meaning of life... \n"
    "   but then again, if I avoid thinking, how do I know if I'm avoiding it correctly?'"
    f"{RESET}"
)

# Display program
def main():
    # Print the border
    print(BORDER)
    # Animate the quote
    typewriter_effect(QUOTE)
    # Print closing frame
    print(BORDER)

# Run the program
if __name__ == "__main__":
    main()