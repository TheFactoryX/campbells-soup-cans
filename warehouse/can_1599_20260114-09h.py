"""
Campbell's Soup Can #1599
Produced: 2026-01-14 09:43:55
Worker: Mistral: Mistral 7B Instruct v0.3 (mistralai/mistral-7b-instruct-v0.3)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import textwrap

# Define the quote
quote = textwrap.dedent("""
\033[93m
         _____
        /     \
       /  *   \
      /    *   \
     /      *   \
    /___________\
   \             /
    \           /
     \         /
      \       /
       \     /
        \   /
         \ /
          /

       "I'm not afraid of death; I just don't want to be there when it happens."

       - Woody Allen
""")

# Define the animation function
def print_quote(quote):
    for line in quote.splitlines():
        print(line)
        time.sleep(0.05)

# Run the animation
print_quote(quote)