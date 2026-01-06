"""
Campbell's Soup Can #1430
Produced: 2026-01-06 13:49:42
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time
import sys
import random
import os

# --- Configuration ---
# ANSI Color codes
class Color:
    HEADER    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Woody Allen Style Quotes ---
# A collection of self-deprecating, neurotic, existential quips.
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "My brain is my second favorite organ.",
    "I took a speed reading course and read War and Peace in twenty minutes. It involves Russia.",
    "If it turns out I'm right, I'll be very surprised.",
    "I'm astounded by people who want to 'know' the universe when it's hard enough finding your way around Chinatown.",
    "The odds of being picked at random are astronomical. Try it sometime. It won't work.",
    "Basically I'm a happy person, except I'm depressed."
]

# --- ASCII Art Components ---
# A wire-frame model of a brain, or perhaps a blob. It's existential.
ART_LINES = [
    f"{Color.CYAN}      .-----.",
    f"{Color.CYAN}    /{Color.FAIL}#########{Color.CYAN}\\",
    f"{Color.CYAN}   /{Color.FAIL}###{Color.WARNING}{{?}}{Color.FAIL}###{Color.CYAN}\\",
    f"{Color.CYAN}  |{Color.FAIL}###{Color.WARNING}| {Color.WARNING}II {Color.FAIL}| #{Color.CYAN}|",
    f"{Color.CYAN}  |{Color.FAIL}###{Color.WARNING}{{'\"'}}{Color.FAIL}###{Color.CYAN}|",
    f"{Color.CYAN}   \\{Color.FAIL}#########/{Color.CYAN}",
    f"{Color.CYAN}    \\{Color.FAIL}#/{Color.CYAN}   \\{Color.FAIL}#/{Color.CYAN}",
    f"{Color.CYAN}      '---'",
    f"{Color.ENDC}"
]

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.04):
    """
    Prints text with a typewriter effect.
    Handles ANSI codes by not pausing on them.
    """
    i = 0
    while i < len(text):
        char = text[i]
        # Check for start of ANSI escape sequence
        if char == '\033':
            # Find the end of the sequence
            end = text.find('m', i)
            if end != -1:
                # Print the whole sequence at once
                sys.stdout.write(text[i:end+1])
                i = end
            else:
                sys.stdout.write(char)
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            # Randomize speed slightly for human feel
            time.sleep(speed * (0.5 + random.random()))
        i += 1
    print()  # Newline at the end

def print_boxed_quote(quote):
    """Prints the quote inside a decorative box with animation."""
    
    # Determine box width based on quote length
    quote_len = len(quote)
    width = quote_len + 4
    top_border = f"{Color.WARNING}╔{'═' * width}╗{Color.ENDC}"
    bottom_border = f"{Color.WARNING}╚{'═' * width}╝{Color.ENDC}"
    side = f"{Color.WARNING}║{Color.ENDC}"
    
    # Padding for readability
    padded_quote = f"  {quote}  "
    
    # Print top border with a flicker effect
    print(f"\n{top_border}")
    time.sleep(0.1)
    
    # Print the quote line by line (it's one line mostly, but robust)
    lines = padded_quote.split('\n')
    for line in lines:
        # Ensure the line is the right length for the box (padding)
        content = line
        # This is a simple centering if we wanted, but let's keep it left aligned
        # inside the box for that 'messy' thought look.
        # We just need to fill the remaining space with spaces.
        remaining = width - len(line) 
        if remaining > 0:
            content = line + " " * remaining
        
        # Construct the full line
        full_line = f"{side}{Color.WARNING}{content}{Color.ENDC}{side}"
        
        # Simulate a thinking pause
        print(full_line)
        time.sleep(0.15)

    print(bottom_border)

def print_neurotic_cursor():
    """Prints a blinking cursor and waits for user to 'face the music'."""
    cursor = f"{Color.BOLD}_{Color.ENDC}"
    for _ in range(6):
        sys.stdout.write(f"\r{Color.FAIL}Press Enter to accept your fate... {cursor}{Color.ENDC}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{Color.FAIL}Press Enter to accept your fate...  {Color.ENDC}")
        sys.stdout.flush()
        time.sleep(0.4)
    
    # Just wait for input silently now
    sys.stdout.write(f"\r{Color.WARNING}Waiting for existential validation...    {Color.ENDC}\n")
    input()

def main():
    clear_screen()
    
    # 1. The Disclaimer / Title
    print(f"{Color.HEADER}{Color.BOLD}")
    print("/// WOODY ALLEN'S POCKET PHILOSOPHER ///")
    print(f"{Color.ENDC}")
    
    # 2. The Art (Type it out)
    for line in ART_LINES:
        print(line)
        time.sleep(0.1)
        
    print("\n")
    
    # 3. Select a random quote
    quote_text = random.choice(QUOTES)
    
    # 4. Print the boxed quote
    print_boxed_quote(quote_text)
    
    # 5. The dramatic pause and cursor
    print("\n")
    print_neurotic_cursor()
    
    # 6. The Post-script (The kicker)
    time.sleep(0.5)
    print(f"\n{Color.CYAN}... And now I have to go lie down.{Color.ENDC}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.FAIL}Interrupted. Typical.{Color.ENDC}")
        sys.exit(0)