"""
Campbell's Soup Can #630
Produced: 2025-11-30 20:33:26
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors and styles
class Style:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Woody Allen-style quote
quote = [
    "Life is absurd, but what's really ridiculous is that",
    "we keep expecting it to make sense. I mean, here we",
    "are, hurtling through space on a rock with limited",
    "snack options, trying to remember people's names at",
    "parties while the universe expands endlessly.",
    "It's like an existential clown car.",
]

def print_centered(text, width=60):
    padding = (width - len(text)) // 2
    print(f'{Style.YELLOW}{" " * padding}{text}{Style.END}')

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(f'{Style.YELLOW}{char}{Style.END}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Box top
    print(f'\n{Style.RED}{"┌"}{"─"*62}{"┐"}{Style.END}')
    
    # Quote lines with typing effect
    for line in quote:
        print(f'{Style.RED}{"│"}{Style.END} ', end='')
        typewriter(line, delay=0.03)
    
    # Author attribution
    print(f'{Style.RED}{"│"}{Style.END}')
    print(f'{Style.RED}{"│"}{Style.END}{" " * 40}', end='')
    typewriter(f'{Style.BOLD}― Woody Allen (probably){Style.END}', delay=0.05)
    
    # Box bottom
    print(f'{Style.RED}{"└"}{"─"*62}{"┘"}{Style.END}\n')

if __name__ == "__main__":
    main()