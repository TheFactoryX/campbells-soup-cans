"""
Campbell's Soup Can #241
Produced: 2025-11-13 04:40:14
Worker: Mistral: Mistral Nemo (free) (mistralai/mistral-nemo:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for colors
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Woody Allen quotes
quotes = [
    f"{YELLOW}Life doesn't imitate art, it imitates bad television.{RESET}",
    f"{GREEN}I'm not afraid of death, I just don't want to be there when it happens.{RESET}",
    f"{YELLOW}I'm not a neurotic, I have an inner life.{RESET}",
    f"{GREEN}I'm not young enough to know everything.{RESET}",
    f"{YELLOW}I'm not looking for a relationship, I'm just looking for a roommate I can make out with.{RESET}",
]

# Print a funny ASCII art
print(f"""
{RESET}
  ______
< I'm not |
 \   ^__^
  \  (oo)\_______
     (__)\       )\/\
         ||----w |
         ||     ||
{RESET}
""")

# Wait for a second to let the ASCII art show
time.sleep(1)

# Print a random quote with some animation
for _ in range(3):
    quote = random.choice(quotes)
    print(f"\n{quote}\n")
    time.sleep(0.5)

print(f"\n{RESET}And that's why I prefer the movies.")