"""
Campbell's Soup Can #4505
Produced: 2026-08-09 19:00:48
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import os
import time
import random
from io import StringIO

# ANSI color codes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
INVERT = '\033[7m'
REVERSE = '\033[5m'

# Decorative characters
stars = ['*', '✪', '★', '☀️', '☻', '☸']

# Animated cursor (moves randomly)
cursor = (3, 3)  # Starting position

def generate_quote():
    prefixes = [
        "I'm sitting here thinking about",
        "Someone asked me the other day",
        "This might sound strange",
        "Between the misery and clarity of a midlife crisis",
        "When you stare into the abyss long enough",
        "In the singularity of late-night existential dread",
        "After that third glass of absinthe",
        "When you realize most people are",
    ]
    
    main_parts = [
        "death's existential coupon system",
        "life just being... aggressively mediocre",
        "how coffee became a personality",
        "the universe's billion-year midlife crisis",
        "being trapped in a simulation of sentience",
        "the cost of pretending to care",
        "how NFTs are actually just thoughts",
        "that anxiety is just evolved thought patterns",
        "the heat death of humor",
        "how boomers missed everything",
        "if we're actually just quotes in a book",
        "what CAPTCHA means",
        "the dread of someone finally reading this",
        "the void beneath my Chekhov shorts",
        "how we're all just background noise",
    ]
    
    suffixes = [
        "should each wear irony like it's a religion",
        "has been uninstalled from my emotional browser.",
        "and I'm here like... questioning everything",
        "but I'll have to stop. The antipsychotics are waiting.",
        "and I'm just here bored, like always",
        "and I'd bill this",
        "but who's trolling the universe about this?",
        "because that's just stupid neuroticism",
        "but I'll have comedy gold before midnight",
        "it's just my Tuesday existential crisis",
        "I'm basically not real anyway",
        "because life is just contextual comedy",
        "but I'll save that for the therapist",
        "and I'm not talking to you specifically",
        "so help me God I'm canceled",
        "and that's Twitter-level absurd",
    ]
    
    return random.choice(prefixes) + " " + random.choice(main_parts) + " " + random.choice(suffixes)

def animated_cursor():
    symbols = [' ', '//', '~~', '□', '□']
    while True:
        symbol = random.choice(symbols)
        sys.stdout.write(f'\033[{cursor[0]};{cursor[1]}H{ITALIC}{symbol}{RESET}')
        sys.stdout.flush()
        time.sleep(0.15)
        cursor = ((cursor[0] + 1) % 25, (cursor[1] + 1) % 80)

def create_decorative_quote(quote):
    width = len(quote) + 6
    
    top_border = (stars[random.randrange(0, len(stars))] * width).ljust(80, ' ')
    middle_border = (' ' + '|' + ' '*(width-2) + '|').ljust(80, ' ')
    bottom_border = (stars[random.randrange(0, len(stars))] * width).rjust(80, ' ')
    
    header = f"{WHITE}{BOLD}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{RESET}"
    
    lines = [top_border, middle_border, header, middle_border]
    for i, line in enumerate(quote.split('\n')):
        line = line.rstrip()
        formatted = f"{BLACK}|  {line} {' '*(width - len(line) - 4) if len(line) < width - 4 else ''}  |".ljust(80, ' ')
        if i == 0 or i == len(quote.split('\n')) - 1:
            formatted = f"{BLUE}{formatted}{RESET}"
        elif i % 2 == 1:
            formatted = f"{YELLOW}{formatted}{RESET}"
        lines.append(formatted)
    
    footer = f"{WHITE}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{RESET}"
    lines.append(middle_border)
    lines.append(bottom_border)
    lines.append(footer)
    
    animated_cursor_handle = None
    cursor_thread = None
    
    try:
        cursor_thread = threading.Thread(target=animated_cursor, daemon=True)
        cursor_thread.start()
        
        for line in lines:
            sys.stdout.write(line + '\n')
            sys.stdout.flush()
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        pass
    finally:
        if cursor_thread and cursor_thread.is_alive():
            cursor_thread.join(timeout=0.1)
        sys.stdout.write(f'\033[{cursor[0]};{cursor[1]}H{RESET}')
        sys.stdout.flush()

def main():
    quote = generate_quote()
    create_decorative_quote(quote)

if __name__ == "__main__":
    main()