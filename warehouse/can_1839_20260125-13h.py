"""
Campbell's Soup Can #1839
Produced: 2026-01-25 13:44:59
Worker: Cohere: Command R+ (08-2024) (cohere/command-r-plus-08-2024)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for text colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[93m"

# Woody Allen-esque quotes
woody_quotes = [
    f"{CYAN}You'd be surprised how many people live their lives based on what they think looks cool, which is only slightly better than living your life according to what your parents think.{RESET}",
    f"{CYAN}I'm not afraid of death. I just don't want to be there when it happens.{RESET}",
    f"{CYAN}Life is full of misery, loneliness, and suffering, and it wouldn't be complete without a small dose of dandruff.{YELLOW} It's a package deal.{RESET}",
    f"{CYAN}My one regret in life is that I'm not someone else.{RESET}",
    f"{CYAN}There are worse things in life than death. Have you ever spent an evening with an insurance salesman?{RESET}",
    f"{CYAN}I don't want to achieve immortality through my work; I want to achieve it by not dying.{YELLOW} Seems simpler.{RESET}",
]

# ASCII art header
woody_art = f"""
{BOLD}     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{CYAN} ▄▄▄▄▄ {YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▄▄▄{CYAN}       ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ {YELLOW}▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄{CYAN}▄▄▄▄▄▄ {YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{CYAN} ▄▄▄▄▄▄▄▄▄▄▄▄▄{YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▄▄▄▄▄▄▄▄▄▄▄▄{CYAN} ▄▄▄▄▄▄▄ {YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{CYAN}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{YELLOW}▄▄▄▄▄▄▄▄▄▄
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{CYAN}▄▄▄▄▄▄ {YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▄▄▄▄▄▄▄▄▄{CYAN} ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ {YELLOW}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 {BOLD}         A {CYAN}WOODY{YELLOW} ALLEN{BOLD} MOMENT:{RESET}
"""

# Function to animate text
def animated_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

# Main program
if __name__ == "__main__":
    # Print Woody Allen ASCII art header
    animated_print(woody_art)

    # Randomly select and print a quote
    quote = random.choice(woody_quotes)
    print("\n" + quote)