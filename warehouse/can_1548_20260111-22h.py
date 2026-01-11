"""
Campbell's Soup Can #1548
Produced: 2026-01-11 22:34:54
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
import random
import sys

def woody_allen_quote_printer():
    # The one philosophical quote
    quote = '"The universe is expanding, and my waistline is too. It makes you wonder which one will swallow us whole first."'
    
    # ASCII Art representation of Woody Allen-esque anxiety
    # A simple theater mask with a worried expression
    art = r"""
      .---.
     /     \
    |  o o  |
    |   ^   |
     \  -  /
      '---'
    """
    
    # Colors (ANSI escape codes)
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    MAGENTA = '\033[95m'
    
    # Title text
    title = "WOODY'S EXISTENTIAL WAFFLE"
    
    # Animation utility
    def typewriter(text, color, speed=0.03):
        for char in text:
            sys.stdout.write(f"{color}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def print_centered(text, width=60, color=WHITE):
        padding = (width - len(text)) // 2
        print(f"{color}{' ' * padding}{text}{RESET}")

    def slide_in(text, color):
        width = 60
        text_len = len(text)
        # Clear previous line logic can be tricky in simple scripts, 
        # so we will just do a nice rapid print
        for i in range(5):
            prefix = " " * (i * 3)
            sys.stdout.write(f"\r{prefix}{color}{text[:width - i*3]}{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
        print() # newline

    # --- SEQUENCE START ---
    
    # 1. Clear screen (optional, but nice for the effect)
    # Note: Some terminals might not support this, but it's standard ANSI
    print("\033[2J\033[H") 

    # 2. Draw the Title with a border
    border = f"{MAGENTA}*" * (len(title) + 4)
    print(f"\n{border}")
    print_centered(f"{BOLD}{YELLOW}{title}{RESET}", len(border))
    print(f"{border}\n")

    # 3. Print the ASCII Art with a blink effect
    for _ in range(3):
        sys.stdout.write(f"\r{RED}{art}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{' ' * 30}") # Clear it
        sys.stdout.flush()
        time.sleep(0.1)
    # Leave it visible
    print(f"\r{RED}{art}{RESET}")

    # 4. The Build Up (Neurotic intro)
    print()
    typewriter("...Calculating the meaning of life...", CYAN, 0.05)
    time.sleep(0.2)
    typewriter("...Synchronizing anxiety levels...", BLUE, 0.04)
    time.sleep(0.2)
    
    # 5. The Quote Reveal (Slide in effect)
    print()
    print_centered("AND SO, HE MUSES:", 60, YELLOW)
    time.sleep(0.5)
    
    # We break the quote into two parts for dramatic pause
    part1 = quote.split(";")[0] + ";"
    part2 = quote.split(";")[1]
    
    # Typewriter Part 1
    print() # spacing
    typewriter(part1, WHITE, 0.06)
    time.sleep(0.4) # The dramatic pause
    
    # Typewriter Part 2 (with color shift)
    typewriter(part2, RED, 0.06)
    
    # 6. Final Thought (scrolling footer)
    time.sleep(0.5)
    print()
    footer = " -- I am big, the universe is expanding, it's the pictures that got small. -- "
    # Slide footer in from right to left visually using carriage return
    width = 60
    for i in range(len(footer), 0, -1):
        sys.stdout.write(f"\r{CYAN}{footer[:i].center(width)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

if __name__ == "__main__":
    try:
        woody_allen_quote_printer()
    except KeyboardInterrupt:
        # Allow user to exit gracefully if they spam Ctrl+C
        print("\n\n[Narrator: He left the theater early, but his existential dread remained.]")
        sys.exit(0)