"""
Campbell's Soup Can #3684
Produced: 2026-05-15 17:00:59
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
Because existential crisis deserves good presentation.
"""

import time
import sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

def print_with_delay(text, delay=0.03):
    """Print text character by character for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Header with ASCII art
    header = f"""
{CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   {BOLD}{RED}  _    _    _    _    _    _    _    _    _    _   {RESET}{CYAN}║
║   {RED}| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  {RESET}{CYAN}║
║   {YELLOW}| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  {RESET}{CYAN}║
║   {GREEN}| |__| |__| |__| |__| |__| |__| |__| |__| |__| |__| |  {RESET}{CYAN}║
║   {BLUE}|______||||______||||______||||______||||______||||______||  {RESET}{CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    
    # Philosophical quote in a nice box
    quote_box = f"""
{YELLOW}╭──────────────────────────────────────────────────────────────╮
│                                                              │
│  {BOLD}{WHITE}I'm not afraid of being nothing after death.{RESET}{YELLOW}                       │
│  {BOLD}{WHITE}In fact, I'm positively excited about the prospect!{RESET}{YELLOW}              │
│                                                              │
│  {DIM}{RED}Because if there's one thing I've learned in life, it's that{RESET}{YELLOW}       │
│  {DIM}{RED}being nothing sounds remarkably similar to being{RESET}{YELLOW}                 │
│  {DIM}{RED}everything I do when I get out of bed on a Monday morning.{RESET}{YELLOW}         │
│                                                              │
│  {MAGENTA}           — Someone Who Should Know Better{RESET}{YELLOW}                     │
│                                                              │
╰──────────────────────────────────────────────────────────────╯{RESET}
"""
    
    # Print quote with typewriter effect
    print(f"{BLUE}Calculating existential wisdom{RED}...{RESET}")
    time.sleep(0.5)
    print()
    print_with_delay(quote_box, 0.02)
    
    # Footer
    footer = f"""
{GREEN}✨ {DIM}Philosophy is like a repository of thoughts{RESET}{GREEN} ✨
{GREEN}especially the ones we have while staring at the ceiling at 3 AM{RESET}
"""
    print(footer)

if __name__ == "__main__":
    main()