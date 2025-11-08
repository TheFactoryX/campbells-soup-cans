"""
Campbell's Soup Can #141
Produced: 2025-11-08 14:30:19
Worker: OpenAI: GPT-4o (2024-08-06) (openai/gpt-4o-2024-08-06)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animated ASCII art for the quote
def animate_quote():
    quote_lines = [
        "     _____ _                 _            _ ",
        "    / ____| |               | |          | |",
        "   | |    | | ___  _   _  __| | ___   ___| |",
        "   | |    | |/ _ \\| | | |/ _` |/ _ \\ / _ \\ |",
        "   | |____| | (_) | |_| | (_| | (_) |  __/_|",
        "    \\_____|_|\\___/ \\__,_|\\__,_|\\___/ \\___(_)",
    ]

    philosophical_quotes = [
        "Life is what happens between existential crises.",
        "I don't mind dying, as long as I'm not actually there.",
        "The universe and I are both expanding, but only one has pizza pockets to blame.",
    ]

    selected_quote = philosophical_quotes[1]

    # Clear the screen and print the animated quote
    clear_screen()
    for line in quote_lines:
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.2)

    # Print the selected quote in the style of Woody Allen
    time.sleep(0.5)
    print("\n" + BLUE + "=" * len(selected_quote) + RESET)
    for char in selected_quote:
        print(YELLOW + char + RESET, end='', flush=True)
        time.sleep(0.07)
    print()
    print(RED + "=" * len(selected_quote) + RESET + "\n")
    time.sleep(1)

animate_quote()