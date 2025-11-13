"""
Campbell's Soup Can #255
Produced: 2025-11-13 18:44:26
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import random

# ANSI color codes
class Style:
    RESET = "\033[0m"
    PINK = "\033[95m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    BG_RED = "\033[41m"

# Quote data
QUOTE = Style.PINK + "I'm not afraid of death; I just don't want to be there when it happens." + Style.RESET
AUTHOR = Style.CYAN + "- Woody Allen" + Style.RESET

# Create ASCII art of a thinking skull head
SKULL = f"""
{Style.YELLOW}      __---__
   _-`oOOoOoOo`-_
  (    OOOOOOO    )
   `-__-oOo-__-'
      / (   ) \\
     /   \ /   \\
    (<     >)_)
     \\     //   {Style.PINK}Life{/Style.YELLOW}
      )   (
     /     \\   {Style.PINK}LOL{/Style.YELLOW}
    (       ) \n{Style.RESET}"""

# Make terminal full screen on Windows
if os.name == 'nt':
    os.system('mode con: cols=120 lines=30')

# Get terminal dimensions
try:
    columns, rows = os.get_terminal_size()
except OSError:
    columns = 80
    rows = 24

# Center text function
def center_text(text):
    padding = (columns - len(text)) // 2
    return Style.YELLOW + " " * max(0, padding) + text + Style.RESET

# Print animated border
def print_border():
    print(Style.YELLOW + "=" * columns + Style.RESET)

# Typing effect
def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Print groovy quote card
def print_quote_card():
    card_width = min(columns - 10, 100)
    card_height = rows // 2
    
    # Card design
    border = Style.YELLOW + "╌" * card_width + Style.RESET
    mid = Style.YELLOW + "│" + " " * (card_width - 2) + "│" + Style.RESET
    
    print()
    print_centered = lambda x: sys.stdout.write(center_text(x) + "\n")
    
    # Top decoration
    print_centered(SPARKLE图案)
    
    # Top border
    print_centered(SPARKLE图案)
    
    # Title
    title = Style.PINK + "WOODY ALLEN QUOTE OF THE DAY" + Style.RESET
    print_centered(title)
    
    # Quote rest section
    print_centered(border)
    print_centered(mid)
    print_centered(mid)
    
    # Animated quote
    print_centered(" " * ((card_width - len(QUOTE)) // 2) + QUOTE)
    
    print_centered(mid)
    print_centered(mid)
    
    # Author section
    quote_rest = " " * ((card_width - len(AUTHOR)) // 2) + AUTHOR
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    
    # Print author in subtle glow
    glow = random.randint(2, 4)
    glow_chars = Style.YELLOW + SPARKLE图案 + (SPARKLE图案 * glow) + Style.RESET
    print_centered(" " * ((card_width - len(glow_chars)) // 2) + glow_chars)
    
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    
    # Rest of quote letters
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    print_centered(SPARKLE图案)
    
    # Bottom
    print_centered(border)

# Sparkle pattern
SPARKLE图案 = random.choice("✧✨★✹✿✿✺✹✬❦☙❧")

# Main animation
if __name__ == "__main__":
    # Clear screen
    print(Style.RESET + "\033c")
    
    # Print title with bouncy effect
    title = Style.CYAN + "Roast Your Reality With Woody's Wisdom!" + Style.RESET
    for _ in range(3):
        for i in range(1,4):
            sys.stdout.write("\033[?25l")
            print("\033[{};{}H".format(5 + i, (columns - len(title)) // 2) + title)
            time.sleep(0.1)
            sys.stdout.write("\033[{};{}H".format(5 + i - 1, (columns - len(title)) // 2) + " " * len(title))
            time.sleep(0.1)
        time.sleep(0.3)
    
    # Print skull with descent effect
    skull_lines = SKULL.split('\n')
    for i, line in enumerate(skull_lines):
        sys.stdout.write("\033[{};H".format(10 + i) + line)
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Print quote card animation
    print_quote_card()
    
    # Fadeout effect
    for i in range(10, 0, -1):
        sys.stdout.write("\033[{};{}H".format(10, (columns - len(SPARKLE图案)) // 2) + SPARKLE图案 * i)
        sys.stdout.flush()
        time.sleep(0.1)