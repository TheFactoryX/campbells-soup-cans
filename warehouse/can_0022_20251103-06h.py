"""
Campbell's Soup Can #22
Produced: 2025-11-03 06:47:16
Worker: OpenAI: GPT-4 Turbo (openai/gpt-4-turbo)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def main():
    quote = "I'm not afraid of becoming a meme; I just need to think up a caption first."

    # ASCII art border
    border = [
        r"  ____________________________________________________  ",
        r" |                                                    | ",
        r" |                                                    | ",
        r" |                                                    | ",
        r" |                                                    | ",
        r" |                                                    | ",
        r" |____________________________________________________| ",
    ]

    print()
    for i, line in enumerate(border):
        if i == 3:
            # Center the quote inside the border
            centered_quote = quote.center(len(border[0]) - 4)
            print_colored(f"|  {centered_quote}  |", '1;33')
        else:
            print_colored(line, '1;34')

    print("\n")
    type_effect(" -- Woody Allen style, existential but funny.")

if __name__ == "__main__":
    main()