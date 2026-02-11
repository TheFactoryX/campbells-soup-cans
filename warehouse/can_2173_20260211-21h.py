"""
Campbell's Soup Can #2173
Produced: 2026-02-11 21:50:05
Worker: WizardLM-2 8x22B (microsoft/wizardlm-2-8x22b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def main():
    quote = (
        "I'm not afraid of death; "
        "I just don't want to be there when it happens."
    )

    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    END = "\033[0m"

    # ASCII art box
    top_bottom_border = f"{RED}+{YELLOW}-" + "-" * (len(quote) + 2) + f"-{RED}+{END}"
    empty_line = f"{RED}|{YELLOW} {END}" + " " * (len(quote) + 2) + f" {RED}|{END}"

    print(top_bottom_border)
    for i, word in enumerate(quote.split()):
        if i % 2 == 0:
            colored_word = f"{GREEN}{word}{END}"
        else:
            colored_word = f"{RED}{word}{END}"
        formatted_line = f"{RED}|{YELLOW} {colored_word}"
        # Adjust spacing for the last word
        if i != len(quote.split()) - 1:
            formatted_line += " " * (len(quote) - len(formatted_line) + 3)
        else:
            formatted_line += " " * (len(quote) - len(formatted_line) + 1)
        print(formatted_line)
    print(empty_line * (len(quote.split()) // 2))
    print(top_bottom_border)

    # Print the quote slowly for dramatic effect
    print_slow(f"{YELLOW}Woody Allen once said...{END}")
    time.sleep(1)
    print_slow(quote)

if __name__ == "__main__":
    main()