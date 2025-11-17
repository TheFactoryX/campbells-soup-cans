"""
Campbell's Soup Can #343
Produced: 2025-11-17 18:44:05
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
RED = '\033[31m'
RESET = '\033[0m'

# Woody Allen quotes
quotes = [
    f"{RED}Life is full of misery, loneliness, and suffering.{RESET} And it's all over much too soon.",
    f"{RED}I'm not afraid of death;{RESET} I just don't want to be there when it happens.",
    f"{RED}I don't want to achieve immortality through my work;{RESET} I want to achieve it through not dying."
]

# ASCII art
art = """
 ______   ______     __    __       __     ______     ______
/\  ___\ /\  ___\   /\ \  /\ \     /\ \   /\  ___\   /\  ___\
\ \ \____\ \ \____  \ \ \ \ \ \    \ \ \  \ \ \____  \ \ \____
 \ \_____\\ \_____\  \ \ \ \ \ \    \ \ \  \ \_____\  \ \_____\
  \/_____/ \/_____/   \ \_\ \_\ \____\ \_\  \/_____/   \/_____/
"""

# Print ASCII art and select a random quote
print(art)
time.sleep(1)
print(random.choice(quotes))