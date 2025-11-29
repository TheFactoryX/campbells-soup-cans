"""
Campbell's Soup Can #600
Produced: 2025-11-29 12:56:41
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import time
from random import choice

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ANSI color codes
CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
SKYBLUE = "\033[0;34m"
RESET = "\033[0m"

# Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Comedy is when you pull the rug out from under the audience.",
    "I never forget a face, but in your case I'll be glad to make an exception.",
    "A little bit of blackmail is good for the soul.",
    "I used to think I was indecisive, but now I'm not so sure.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "Live like you're going to die young; in fact, die young as often as possible.",
    "The trouble with marriage is getting divorced.",
    "I'm on a drug saying program; can I have a list of the drugs please?",
    "He never said a word that didn't sound utterly ridiculous.",
    "Life is full of misery, loneliness, and suffering — and it's all over much too soon."
]

woody_quote = choice(quotes)

# ASCII art design
brain = [
    f"{GREEN}        .-""-.",
    f"{GREEN}      .'      '.",
    f"{GREEN}     /          \\",
    f"{GREEN}|   \\          /   |",
    f"{GREEN}|    \\    /    |",
    f"{GREEN} \\   |  \/  |   /",
    f"{GREEN}  '-._     _ .-",
    f"{GREEN}      `-..-`"
]

signature = [
    f"{RED}              ___",
    f"{RED}             /   \\",
    f"{RED}            /     \\",
    f"{RED}           / Woody \\",
    f"{RED}          /__ Allen__\\",
    f"{RED}         |           |",
    f"{RED}          \\     |     /",
    f"{RED}           \\    |    /",
    f"{RED}            \\   |   /",
    f"{RED}             \\  |  /",
    f"{RED}              \\ | /",
    f"{RED}               \\|/  ",
    f"{CYAN}               /|\\  ",
    f"{CYAN}              / | \\ ",
    f"{CYAN}             /  |  \\ ",
    f"{CYAN}            /   |   \\ ",
    f"{CYAN}           /____|____\\"
]

# Format the quote into a golden box
def get_gilded_box(text, gold="\033[1;33m", reset="\033[0m"):
    lines = text.split('\n')
    max_width = max(len(line) for line in lines) + 4
    top_bottom = gold + "╔" + "═" * max_width + "╗" + reset
    box_lines = [gold + "║ " + line.center(max_width-2) + " ║" + reset for line in lines]
    bottom = gold + "╚" + "═" * max_width + "╝" + reset
    return top_bottom + "\n" + "\n".join(box_lines) + "\n" + bottom

# Create the quote box
quote_box = get_gilded_box(woody_quote)

# Print everything with flair
slow_print(f"{SKYBLUE}      /\    /\    /\      {RESET}")
for line in brain:
    slow_print(line, delay=0.05)
slow_print(f"\n{YELLOW} ┌───────────────────────────────────────┐" + RESET)
slow_print(quote_box)
slow_print(f"{YELLOW} └───────────────────────────────────────┘" + RESET)

# Print signature
for line in signature:
    slow_print(line)

slow_print(f"\n{CYAN}         Watched: 5 Grams")
print(f"{RESET}")