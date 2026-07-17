"""
Campbell's Soup Can #4228
Produced: 2026-07-17 11:40:48
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A Woody Allen-style philosophical quote with visual flair"""

import sys
import time

# ANSI color codes
class Colors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def type_writer(text, delay=0.03):
    """Animate text like a typewriter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_box(text, width=60):
    """Create a decorative box around text"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    max_len = min(max_len, width - 4)
    
    # Top border
    box_top = f"{Colors.MAGENTA}╔{'═' * (max_len + 2)}╗{Colors.RESET}"
    
    # Middle lines
    middle_lines = []
    for line in lines:
        padded = line[:max_len].ljust(max_len)
        middle_lines.append(f"{Colors.MAGENTA}║{Colors.RESET} {Colors.CYAN}{padded}{Colors.RESET} {Colors.MAGENTA}║{Colors.RESET}")
    
    # Bottom border
    box_bottom = f"{Colors.MAGENTA}╚{'═' * (max_len + 2)}╝{Colors.RESET}"
    
    return '\n'.join([box_top] + middle_lines + [box_bottom])

def main():
    # Woody Allen-style quote
    quote = """"Sometimes I wonder if the world is an enormous 
malfunctioning computer program that's 
been running since the Big Bang, and we're 
all just characters in a cosmic debugging session 
that God forgot to close. And the worst part? 
I'm pretty sure I'm the bug.""""

    # Animation sequence
    print(f"\n{Colors.YELLOW}" + "╔" + "═" * 58 + "╗" + Colors.RESET)
    print(f"{Colors.YELLOW}║{Colors.RESET}" + " " * 58 + f"{Colors.YELLOW}║{Colors.RESET}")
    print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.BOLD}{Colors.WHITE}WOODY ALLEN'S ANXIETY-INDUCED PHILOSOPHY{Colors.RESET}" + " " * 17 + f"{Colors.YELLOW}║{Colors.RESET}")
    print(f"{Colors.YELLOW}║{Colors.RESET}" + " " * 58 + f"{Colors.YELLOW}║{Colors.RESET}")
    print(f"{Colors.YELLOW}╚" + "═" * 58 + "╝{Colors.RESET}\n")

    # Typing animation
    type_writer(quote, 0.02)
    
    # Add attribution with color
    time.sleep(0.5)
    author = f"\n{Colors.BLUE}{'─' * 60}{Colors.RESET}"
    author += f"\n{Colors.RED}— Woody Allen (probably worried about this very program){Colors.RESET}"
    author += f"\n{Colors.BLUE}{'─' * 60}{Colors.RESET}\n"
    
    # Fade in the attribution
    for char in author:
        if char == '\n':
            print()
            time.sleep(0.01)
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.005)
    
    print(f"\n{Colors.GREEN}{'*' * 60}{Colors.RESET}")
    print(f"{Colors.GREEN}*{' ' * 58}{Colors.GREEN}*")
    print(f"{Colors.GREEN}*  {Colors.YELLOW}Analysis: 97.3% anxiety, 2.7% existential crisis{Colors.GREEN}")
    print(f"{Colors.GREEN}*  {Colors.YELLOW}Confidence level: Extremely uncertain{Colors.GREEN}")
    print(f"{Colors.GREEN}*{' ' * 58}{Colors.GREEN}*")
    print(f"{Colors.GREEN}{'*' * 60}{Colors.RESET}\n")

if __name__ == "__main__":
    main()