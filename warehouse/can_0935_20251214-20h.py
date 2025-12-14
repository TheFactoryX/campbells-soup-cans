"""
Campbell's Soup Can #935
Produced: 2025-12-14 20:34:00
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import textwrap
from shutil import get_terminal_size

def print_woody_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I've had a perfectly beautiful marriage. Both of us got legal custody of the children.",
        "I am unshakably confident that in whatever I do, I will receive full and instant gratification.",
        "My mother always said life was like a box of chocolates. To this day I don't know if she's referring to the fact they are full of nuts...",
        "Schizophrenia is when a person has two personalities. I'm confident that patients with schizophrenia could hold their own in a West Side Story script.",
        "Half the men I know are closet psychotics.",
        "When I used to stand up at some important moment in my life, my legs were so weak I fell.",
        "Did you hear about the insanity, who drove his car into a telephone pole? There's no one to blame except Joe's head.",
        "I used to be a great cyclist. It's because I lost my cycle.",
        "In my neighborhood, every sky line looks like a Masonic pretzel.",
        "I've had a perfectly beautiful divorce: the furniture is mine and it's very comfy."
    ]
    
    chosen_quote = random.choice(quotes)
    width = get_terminal_size().columns
    inner_width = width - 4
    
    # ANSI escape codes for colors
    ESC = "\033"
    RESET = ESC + "[0m"
    FRAMER = ESC + "[38;2;60;60;60m"  # Dark gray border
    TITLE = ESC + "[1;36m"            # Bright cyan title
    TEXT = ESC + "[1;37m"             # Bright white quote
    SMALL_C = ESC + "[38;2;120;120;120m"  # Light gray sneaker
    PAUSE = ESC + "[0;33m"            # Dark yellow for "sleeping..."
    
    # ASCII art of Woody Allen in boxing pose
    woody_ascii = [
        "                       .-''''''-.",
        "|  _ _ _ _ _ _ _ _ _ _|   woody|",
        "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  current |",
        "| o o o o o o o o o o |  boxing  |",
        "|_|_|_|_|_|_|_|_|_|_|_|__in_bed|",
        "   '._   \"\"\"   _.'",
        "     '-.....-'",
        ""
    ]
    
    # Print box with animate opening
    print(FRAMER + "╭" + "─" * (width-2) + "╮" + RESET)
    for line in woody_ascii:
        print(FRAMER + "│ " + RESET + line.center(width-4) + FRAMER + " │" + RESET)
    print(FRAMER + "├" + "─" * (width-2) + "┤" + RESET)
    
    # Print title with animation
    print(FRAMER + "│ " + RESET + TITLE + "WOOO...DY ALLEN QUOTES, PRESENTED".center(inner_width) + FRAMER + " │" + RESET)
    print(FRAMER + "├" + "─" * (width-2) + "┤" + RESET)
    
    # Print quote with dramatic reveal animation
    print(FRAMER + "│ " + RESET + PAUSE + "...sleeping...".center(inner_width) + FRAMER + " │" + RESET)
    print(FRAMER + "├" + "─" * (width-2) + "┤" + RESET)
    print(FRAMER + "│ " + RESET + TITLE + "AH, YES!".center(inner_width) + FRAMER + " │" + RESET)
    print(FRAMER + "├" + "─" * (width-2) + "┤" + RESET)
    
    # Print wrapped quote
    wrapped = textwrap.wrap(chosen_quote, width=inner_width)
    for line in wrapped:
        print(FRAMER + "│ " + RESET + TEXT + line.center(inner_width) + FRAMER + " │" + RESET)
    
    print(FRAMER + "╰" + "─" * (width-2) + "╯" + RESET)
    
    # Print sneaker animation
    print(SMALL_C + "''\n" * random.randint(1,3), end='')  # 1-3 small sneakers
    print(RESET)

if __name__ == "__main__":
    print_woody_quote()