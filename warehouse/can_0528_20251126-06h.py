"""
Campbell's Soup Can #528
Produced: 2025-11-26 06:47:23
Worker: Cohere: Command R (08-2024) (cohere/command-r-08-2024)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_animated_quote(quote):
    words = quote.split()
    for word in words:
        print('\033[1;' + str(random.randint(30, 37)) + 'm' + word + '\033[0m', end=" ")
        time.sleep(0.1)  # adjust speed here
    print()

# Some "Woody Allen" Style Quotes (you can add more!)
quotes = [
    "I'm terrified of dying and being forgotten. But I'm more terrified of being forgotten while still alive.",
    "Money is better than poverty, if only for financial reasons.",
    "My one regret in life is that I am not someone else.",
    "I'd rather be dead than read,"
]

# Choose a random quote and print it animatedly
quote_to_print = random.choice(quotes)
print('\033[1m' + '-'*60 + '\033[0m')
print('\033[1;' + str(random.randint(32, 37)) + 'm' + 'In the words of Woody Allen:' + '\033[0m')
print_animated_quote(quote_to_print)
print('\033[1m' + '-'*60 + '\033[0m')