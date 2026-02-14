"""
Campbell's Soup Can #2218
Produced: 2026-02-14 10:46:47
Worker: OpenAI: GPT-4o (2024-05-13) (openai/gpt-4o-2024-05-13)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Colors using ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

quote = "I’m not saying I don’t believe in a higher power; I’m just saying I’d be more comfortable if it were a little clearer about the rental agreement."

# function to print each character with a delay for animation effect
def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII Art Woody Allen Style Text
art = [
    RED + "  __          __  _                            _          _   _ ",
    YELLOW + "  \\ \\        / / | |                          | |        | | | |",
    GREEN + "   \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |",
    CYAN + "    \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\  |  _  |",
    BLUE + "     \\  /\\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | |",
    MAGENTA + "      \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  \\_| |_/",
    RESET
]

# Print the art
for line in art:
    animated_print(line, 0.05)

# Print the quote with some flair
animated_print(CYAN + "\n" + ("*"*len(quote)) + "\n" + quote + "\n" + ("*"*len(quote)) + RESET, 0.05)