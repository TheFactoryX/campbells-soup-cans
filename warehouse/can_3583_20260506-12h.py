"""
Campbell's Soup Can #3583
Produced: 2026-05-06 12:07:11
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic philosophical quote in Woody Allen's style with visual flair!"""

import time
import sys

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'

def typewriter(text, color="", delay=0.04, newline=True):
    """Print text with typewriter effect"""
    full_text = f"{color}{text}{Colors.RESET}"
    for char in full_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def draw_brain():
    """Draw a simple thinking brain"""
    brain = f"""
{Colors.CYAN}     {'='*20}
   {'='*24}
  {'='*26}
  {Colors.BLUE}  (  {Colors.CYAN}__{Colors.BLUE}  ){Colors.CYAN}______
  {Colors.BLUE} (   {Colors.CYAN}o o{Colors.BLUE} ){Colors.CYAN}      ){Colors.BLUE}__
 {Colors.BLUE}  (      {Colors.CYAN}_\\{Colors.BLUE}__){Colors.CYAN}    ){Colors.BLUE}(  )
 {Colors.BLUE}   {Colors.CYAN}\\___/{Colors.BLUE}__) {Colors.CYAN}|__|{Colors.BLUE}|_|
 {Colors.BLUE}  /__{Colors.CYAN}\\{Colors.BLUE}____{Colors.CYAN}/{Colors.BLUE}___{Colors.CYAN}/{Colors.BLUE}____
 {Colors.CYAN}     {Colors.BLUE}|{Colors.CYAN}___{Colors.BLUE}|{Colors.CYAN}___{Colors.BLUE}|
{Colors.RESET}"""
    print(brain)

def draw_quote_box(quote_lines):
    """Draw a decorative box around quote lines"""
    max_len = max(len(line) for line in quote_lines)
    border = f"{Colors.MAGENTA}{'═' * (max_len + 4)}{Colors.RESET}"
    
    print(border)
    for line in quote_lines:
        padded = line.center(max_len)
        print(f"{Colors.MAGENTA}║{Colors.RESET} {Colors.YELLOW}{padded}{Colors.RESET} {Colors.MAGENTA}║{Colors.RESET}")
    print(border)

def main():
    # Header
    print(f"\n{Colors.BOLD}{Colors.RED}{'═' * 50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}   A WOODY ALLEN-STYLE PHILOSOPHY{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.RED}{'═' * 50}{Colors.RESET}\n")
    
    # Draw thinking brain
    draw_brain()
    
    # The quote split into lines for the box
    quote_lines = [
        "I used to think I wanted to achieve immortality,",
        "but then I realized I'm not particularly",
        "enthusiastic about the whole 'living' part.",
        "",
        "Life is like a relay race,",
        "and I keep dropping the baton",
        "because I'm too busy contemplating",
        "whether I want to finish it."
    ]
    
    # Draw the quote box
    draw_quote_box(quote_lines)
    
    # Author attribution
    print(f"\n{Colors.BOLD}{Colors.GREEN}           — A Neurotically Yours{Colors.RESET}")
    print(f"{Colors.DIM}           (Woody Allen's Spirit Animal){Colors.RESET}\n")
    
    # Footer with some existential dread
    print(f"{Colors.ITALIC}{Colors.BLUE}{'─' * 50}{Colors.RESET}")
    print(f"{Colors.ITALIC}{Colors.BLUE}     Still wondering if I should have stayed in bed...{Colors.RESET}")
    print(f"{Colors.ITALIC}{Colors.BLUE}{'─' * 50}{Colors.RESET}\n")

if __name__ == "__main__":
    main()