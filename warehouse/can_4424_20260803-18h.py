"""
Campbell's Soup Can #4424
Produced: 2026-08-03 18:05:22
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A woody allen style philosophical quote printer
with visual flair. Pure python, no dependencies.
"""

import sys
import time
import os

# ANSI color codes
class Colors:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def draw_border(top_char='═', side_char='║', corners='╭╮╰╯'):
    width = 60
    top = f"{Colors.CYAN}{corners[0]}{top_char * (width-2)}{corners[1]}{Colors.RESET}"
    bottom = f"{Colors.CYAN}{corners[2]}{top_char * (width-2)}{corners[3]}{Colors.RESET}"
    return top, bottom, width

def animate_quote():
    clear_screen()
    
    top, bottom, width = draw_border()
    
    # Title with animation
    title = "🌟 WOODY ALLEN STYLE PHILOSOPHY 🌟"
    print(f"\n{Colors.YELLOW}{'=' * 65}{Colors.RESET}")
    print_slow(f"{Colors.BOLD}{Colors.MAGENTA}{title.center(65)}{Colors.RESET}", 0.05)
    print(f"{Colors.YELLOW}{'=' * 65}{Colors.RESET}\n")
    
    print(top)
    
    quote_lines = [
        "    I'm not terrified of death,     ",
        "    I simply prefer not to be      ",
        "    in the room when it occurs.    ",
        "       — Woody Allen (probably)    ",
    ]
    
    for line in quote_lines:
        centered = line.center(58)
        print(f"{Colors.BLUE}{top[0]}{Colors.CYAN}{centered}{Colors.BLUE}{top[0].replace('╭', '╮').replace('╮', '╭')}")
        time.sleep(0.3)
    
    print(bottom)
    
    # Philosophical musings
    musings = [
        "    Existential crisis level: MAXIMUM",
        "    Coffee consumption: Also maximum",
        "    Will to live: Questionable at best"
    ]
    
    print(f"\n{Colors.GREEN}{'─' * 65}{Colors.RESET}")
    for musing in musings:
        print(f"{Colors.GREEN}│{Colors.YELLOW}  {musing.ljust(60)} {Colors.GREEN}│{Colors.RESET}")
        time.sleep(0.15)
    print(f"{Colors.GREEN}{'─' * 65}{Colors.RESET}")
    
    # Final flourish
    print(f"\n{Colors.RED}{Colors.BOLD}    The universe doesn't care,")
    print(f"    but at least we have pretzels.{Colors.RESET}")
    
    print(f"\n{Colors.MAGENTA}{'≈' * 65}{Colors.RESET}")

def main():
    try:
        animate_quote()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Even the interruption is meaningless.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.YELLOW}Error: {e}{Colors.RESET}")
        print(f"{Colors.RED}Like Sisyphus, we push the boulder anyway.{Colors.RESET}")

if __name__ == "__main__":
    main()