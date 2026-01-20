"""
Campbell's Soup Can #1725
Produced: 2026-01-20 05:46:07
Worker: Qwen: Qwen3 Next 80B A3B Instruct (free) (qwen/qwen3-next-80b-a3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def ascii_heart():
    return [
        "    ████████████    ",
        "  ████████████████  ",
        " ██████████████████ ",
        "████████████████████",
        "████████████████████",
        " ██████████████████ ",
        "  ████████████████  ",
        "    ████████████    ",
        "      ████████      ",
        "        ████        ",
        "          ██        "
    ]

def colored_quote():
    quote = "I'm not afraid of death—I just don't want to be there when it occurs. Like that time I tried to microwave a burrito and my dog got the leftovers. At least he didn't leave a note saying 'I'm sorry, but I couldn't handle the existential dread of having too many avocados.'"
    
    # ANSI color codes
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    # Create a visually interesting layout
    print("\n" + "="*60)
    print(BOLD + CYAN + "            WOODY ALLEN'S ASYLUM DIARY" + RESET)
    print("="*60 + "\n")
    
    # Print animated heart
    for row in ascii_heart():
        print(MAGENTA + row + RESET)
        time.sleep(0.15)
    
    print("\n" + BOLD + YELLOW + "PHILOSOPHICAL INSIGHT #666:" + RESET)
    print(BOLD + WHITE + "-------------------------------------------" + RESET)
    
    # Color each word strangely
    words = quote.split()
    colors = [RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN, WHITE]
    for i, word in enumerate(words):
        color = random.choice(colors)
        # Add punctuation handling
        if word.endswith(('.', ',', '!', '?', ':', ';')):
            punc = word[-1]
            word = word[:-1]
            print(color + word + RESET + punc, end=" ")
        else:
            print(color + word + RESET, end=" ")
        
        if i % 6 == 5:  # Line break every 6 words
            print()
        time.sleep(0.08)
    
    print("\n" + BOLD + WHITE + "-------------------------------------------" + RESET)
    print("\n" + BLUE + "P.S. If this printed in color, it means you're already dead." + RESET)
    print("\n" + "="*60)
    print(BOLD + RED + "                WHERE IS MY COFFEE?!" + RESET)
    print("="*60 + "\n")

# Run it!
if __name__ == "__main__":
    try:
        colored_quote()
    except KeyboardInterrupt:
        print("\n" + YELLOW + "AHHH! THE COMPUTER JUST ESCAPED INTO THE VOID!" + RESET)