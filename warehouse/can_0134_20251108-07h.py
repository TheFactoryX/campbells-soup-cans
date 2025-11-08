"""
Campbell's Soup Can #134
Produced: 2025-11-08 07:27:44
Worker: OpenAI: GPT-4o (2024-11-20) (openai/gpt-4o-2024-11-20)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# ANSI escape codes for colors
COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

# ASCII Art border
BORDER = """
  ________________________________
 /                                \\
|                                  |
 \________________________________/
"""

# Woody Allen style quote
QUOTE = (
    "Life is like a movie where I paid for popcorn, \n"
    "but the plot makes me wonder if I hit my head on the way in."
)

def typewriter_effect(text, color="white"):
    for char in text:
        sys.stdout.write(COLORS[color] + char + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(0.03)  # Typewriter delay
    print("\n", end="")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print(COLORS["yellow"] + BORDER + COLORS["reset"])

    # Spacing for quote
    print(COLORS["cyan"] + "| " + COLORS["reset"], end="")
    typewriter_effect(QUOTE, color="magenta")
    print(COLORS["cyan"] + "| " + COLORS["reset"])
    
    print(COLORS["yellow"] + BORDER + COLORS["reset"])

    print(COLORS["blue"] + "\n(Press Enter to exit)" + COLORS["reset"])
    input()

if __name__ == "__main__":
    main()