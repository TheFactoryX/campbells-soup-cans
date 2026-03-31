"""
Campbell's Soup Can #3061
Produced: 2026-03-31 17:13:53
Worker: Mistral: Codestral 2508 (mistralai/codestral-2508)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_quote():
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    # ASCII art
    woody_art = f"""
    {RED}  _____ _____ _____ _____ _____ _____ _____
    |     |   __| __  |     |   __| __  |     |
    | | | |__   |    -| | | |   __|    -| | | |
    |_|_|_|_____|__|__|_|_|_|_____|__|__|_|_|_|{RESET}
    """

    # Quote
    quote = f"""
    {GREEN}Life is a {RED}box of chocolates{RESET}{GREEN}, you never know what you're gonna get.
    But at least you can always {BLUE}complain{RESET}{GREEN} about it.
    It's like a {YELLOW}Russian roulette{RESET}{GREEN} with existential dread.
    And don't even get me started on the {MAGENTA}meaning of it all{RESET}{GREEN}.
    It's all just a {CYAN}cosmic joke{RESET}{GREEN} that we're all in on.{RESET}
    """

    # Print the ASCII art
    print(woody_art)

    # Print the quote with typewriter effect
    typewriter(quote)

if __name__ == "__main__":
    print_woody_quote()