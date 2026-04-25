"""
Campbell's Soup Can #3441
Produced: 2026-04-25 10:05:42
Worker: Perplexity: Sonar Pro (perplexity/sonar-pro)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
RED = '\033[91m'GREEN = '\033[92m'YELLOW = '\033[93m'BLUE = '\033[94m'MAGENTA = '\033[95m'CYAN = '\033[96m'BOLD = '\033[1m'UNDERLINE = '\033[4m'END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_quote():
    clear_screen()
    
    # Animated title
    title = f"{BOLD}{CYAN}Woody Allen's Neurotic Wisdom{END}"
    print_slow(title, 0.08)
    
    print(f"{YELLOW}{'='*60}{END}\n")
    
    # ASCII art brain (neurotic thoughts)
    brain = f"""
{BLUE}       .-"""-.
      /       \\
     |  O   O  |
     |    ∆    |   {MAGENTA}*Existential Dread Ahead*{END}
      \\  '-'  /
       '-....-'{END}
    """
    print_slow(brain)
    
    # The quote
    quote = f"{BOLD}{RED}\"{END}"
    quote += f"{YELLOW}I'm not scared of the meaninglessness of life...{END}"
    quote += f"{BOLD}{RED}it's just that when the universe stares back at me,{END}"
    quote += f"{MAGENTA}I get this urge to offer it a {UNDERLINE}nice{END}{MAGENTA} bagel{END}"
    quote += f"{BOLD}{RED}and ask if it's seeing anyone.\"{END}"
    
    print_slow(quote)
    
    print(f"\n{GREEN}{'='*60}{END}")
    
    # Funny footer animation
    footer = f"{BOLD}{CYAN}*sips coffee nervously*{END}"
    print_slow(footer)
    
    # Pulsing effect
    for i in range(3):
        pulse = f"{BOLD}{'?' * (i+1)}{END}"
        sys.stdout.write(f'\r{pulse}')
        sys.stdout.flush()
        time.sleep(0.5)
    print()

if __name__ == "__main__":
    try:
        animate_quote()
    except KeyboardInterrupt:
        print(f"\n\n{BLUE}*escapes existential crisis*{END}")