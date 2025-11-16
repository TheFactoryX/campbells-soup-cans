"""
Campbell's Soup Can #308
Produced: 2025-11-16 05:32:45
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
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
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'

# ASCII art - Woody Allen in a beret
woody_ascii = [
    "            _/",
    "    /\      /",
    "   /  \    /_/_      _______    /\\",
    "  | 0  |  /     \\__  /   -   \\  /  \\",
    "  | o  | /   __   \\_\\/-()()()-\\/__/", 
    "   \\__/  \\__|  |____)        \\____)",
    "    |        |_______)        (____)",
    "    |_        |      \\        /    \\",
    "  __(_)_5-----|       \\______(     \\",
    " (___________/                                "
]

# Animated eyes for Woody
class Woody:
    def __init__(self):
        self.eyes = [')', '0']
        self.eye_index = 0

    def blink(self):
        # Clear screen and print animated Woody
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(RED)
        for line in woody_ascii:
            if '0' in line or ')' in line:
                # Replace eyes in the ASCII art
                current_eye = self.eyes[self.eye_index]
                print(line.replace('0', current_eye).replace(')', current_eye))
            else:
                print(line)
        print(RESET)
        # Cycle eyes
        self.eye_index = (self.eye_index + 1) % len(self.eyes)

# Philosophical quotes in Woody Allen's style
quotes = [
    "\"I have the greatest talent for optimism. I always expect the worst, and it always happens.",
    "\"I think, therefore I am neurotic.\"",
    "\"My philosophy is: don't take life too seriously. No one gets out alive anyway.",
    "\"Life is a disaster that's briefly interrupted by happiness.\"",
    "\"The worst part of getting old is not having another Woody Allen movie to look forward to.\""
]

# Select a random quote
quote = random.choice(quotes)

# Display animated Woody
def display_woody_animation():
    woody = Woody()
    for _ in range(15):  # 15 frames
        woody.blink()
        time.sleep(0.3)

# Print the box with the quote
def print_quote_box():
    border = GREEN + '=' * (len(quote) + 4) + RESET
    space = len(quote) * ' '
    print(GREEN)
    print(border)
    print(f'{GREEN}={RESET}{space} {GREEN}={RESET}')
    print(f'{GREEN}={RESET} {BLUE}{quote}{RESET} {GREEN}={RESET}')
    print(f'{GREEN}={RESET}{space} {GREEN}={RESET}')
    print(border)
    print(YELLOW)
    print("W O O D Y   A L L E N - Style")
    print(RESET)

# Main animation
def main():
    display_woody_animation()
    print_quote_box()

if __name__ == "__main__":
    main()