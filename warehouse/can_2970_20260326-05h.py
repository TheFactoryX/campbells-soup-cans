"""
Campbell's Soup Can #2970
Produced: 2026-03-26 05:49:45
Worker: OpenAI: GPT-4 (older v0314) (openai/gpt-4-0314)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys
from functools import partial
from itertools import cycle

def blink(speed, interval, text):
    """Function to blink text."""
    time.sleep(interval)
    for state in cycle(["\033[5m", "\033[0m"]):
        sys.stdout.write(f"{state}{text}\r")
        sys.stdout.flush()
        time.sleep(speed)

def colored(text, color_code):
    """Function to output text with colored background."""
    return f"\033[{color_code}m{text}\033[0m"

color_codes = [
    41,  # red
    42,  # green
    43,  # yellow
    44,  # blue
    45,  # magenta
    46,  # cyan
    47,  # white
]

# Creating quote lines with formatted ASCII art and colors
quote_lines = [
    " _____ _           _                    _     ",
    "|  __ \\ |         | |                  | |    ",
    "| |  \\/ |__   __ _| |_ ___   _ _ __ ___| |_   ",
    "| | __| '_ \\ / _` | __/ _ \\_| | '__/ _ \\ __|  ",
    "| |_\\ \\ | | | (_| | ||  __/_  | | |  __/ |_   ",
    " \\____/_| |_|\\__,_|\\__\\___( )_|_|  \\___|\\__|  ",
    "                          |/                  ",
]

colored_quotes = []

for text in quote_lines:
    colored_line = [colored(char, random.choice(color_codes)) for char in text]
    colored_quotes.append("".join(colored_line))

# Print colored quote
print("\n")
for line in colored_quotes:
    print(line)
    time.sleep(0.2)
print("\n")

# Blink wrap up text
wrap_up_text = "Enjoy and Contemplate! - Woody Allen"
blink_interval = partial(blink, 1, 0.5)
blink_thread = Thread(target=blink_interval, args=(wrap_up_text,))

try:
    # Start blink_thread with daemon=True
    blink_thread.start()
    time.sleep(6)
except KeyboardInterrupt:
    print(f"{' ' * len(wrap_up_text)}\r")