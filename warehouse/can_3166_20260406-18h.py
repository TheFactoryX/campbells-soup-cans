"""
Campbell's Soup Can #3166
Produced: 2026-04-06 18:04:43
Worker: EssentialAI: Rnj 1 Instruct (essentialai/rnj-1-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

from time import sleep
from os import system, name

# Function to clear screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Woody Allen quote ASCII art
quote = [
'                           *********************************',
'                           * THINKING IS HARD WORK!        *',
'                           *                               *',
'                           * I am constantly bombarded by  *',
'                           * the beauty of the world that  *',
'                           * surrounds us. What a mystery!  *',
'                           *                               *',
'                           * It makes you want to SCREAM!   *',
'                           *********************************',
]

# Colors and animations
colors = ['\033[31m', '\033[32m', '\033[33m']
text = "Why do we exist?".upper()

# Clear screen and print art
clear()
for _ in range(3):
    print("\n" * 10)
    for i, line in enumerate(quote):
        print(colors[i % len(colors)] + line)
    sleep(0.5)
    clear()

# Print final thought
print("\033[1m\033[93m" + text + "\033[0m")
print("\033[36m" + "WRITE IT DOWN... OR IT DISAPPEARS!\033[0m")
print("\033[90m" + "*(Life's obsessed with meaning, isn't it?)*" + "\033[0m")