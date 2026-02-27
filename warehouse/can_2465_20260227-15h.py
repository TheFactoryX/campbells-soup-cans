"""
Campbell's Soup Can #2465
Produced: 2026-02-27 15:52:47
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
BOLD = "\033[1m"

def print_woody_art():
    art = [
        f"{BOLD}{WHITE}      ,_   _      {RESET}",
        f"{BOLD}{WHITE}     (•_•)       {RESET}",
        f"{BOLD}{WHITE}    ( •_•)      {RESET}",
        f"{BOLD}{WHITE}     (•_•)       {RESET}",
        f"{BOLD}{WHITE}      \\ /        {RESET}",
        f"{BOLD}{WHITE}       v         {RESET}",
        f"{BOLD}{WHITE}     (___)       {RESET}",
        f"{BOLD}{WHITE}      / \\        {RESET}",
        f"{BOLD}{WHITE}     /   \\       {RESET}",
        f"{BOLD}{WHITE}    /     \\      {RESET}",
        f"{BOLD}{WHITE}   /       \\     {RESET}",
        f"{BOLD}{WHITE}  /         \\    {RESET}",
        f"{BOLD}{WHITE} /           \\   {RESET}",
    ]
    for line in art:
        print(line)
        time.sleep(0.05)

def print_quote_box(quote, show_quote):
    box_width = 45
    top = f"{BLUE}┌{'─' * (box_width-2)}┐{RESET}"
    empty_line = f"{BLUE}│{' ' * (box_width-2)}│{RESET}"
    
    if show_quote:
        inner_width = box_width - 4
        # Center the quote with padding
        padded_quote = quote.center(inner_width)
        quote_line = f"{BLUE}│ {YELLOW}{padded_quote}{RESET}{BLUE} │{RESET}"
    else:
        quote_line = empty_line
    
    print(top)
    print(empty_line)
    print(quote_line)
    print(empty_line)
    print(f"{BLUE}└{'─' * (box_width-2)}┘{RESET}")

def main():
    # Clear screen with ANSI
    print("\033[H\033[J", end='')
    
    # Print Woody Allen ASCII art with animation
    print_woody_art()
    
    # Print title
    print(f"\n{BOLD}{RED}Woody Allen's Existential Dilemma{RESET}\n")
    
    # The quote (original creation)
    quote = "I don't believe in the afterlife, but I've packed a suitcase just in case. It's mostly socks and existential dread."
    
    # Blinking animation (3 cycles)
    for i in range(5):
        show_quote = (i % 2 == 0)
        print_quote_box(quote, show_quote)
        
        # Print footer with neurotic disclaimer
        print(f"\n{YELLOW}{' ' * 10}This quote may cause minor panic attacks{RESET}")
        print(f"{YELLOW}{' ' * 10}and an irrational fear of elevator music{RESET}")
        
        # Pulse effect for the disclaimer
        for _ in range(3):
            sys.stdout.write(f"\r{RED}{' ' * 10}WARNING: Contains 97% neurosis!{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write(f"\r{YELLOW}{' ' * 10}WARNING: Contains 97% neurosis!{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Move cursor up to overwrite the box
        if i < 4:
            print("\033[7A", end='')  # Move up 7 lines (box height + footer)
            time.sleep(0.6)

if __name__ == "__main__":
    main()