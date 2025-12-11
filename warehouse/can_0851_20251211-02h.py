"""
Campbell's Soup Can #851
Produced: 2025-12-11 02:24:05
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
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
import os

# ANSI escape codes
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
CLEAR = "\033[2J\033[H"

def clear_screen():
    sys.stdout.write(CLEAR)
    sys.stdout.flush()

def woody_print(text, color=YELLOW, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # Title with 'neurotic' animation
    title = [
        "╔════════════════════════════════════════╗",
        "║                                        ║",
        f"║   {BOLD}░W░O░O░D░Y░ ░A░L░L░E░N░{RESET}   {RED}▓{RESET}    ║",
        "║                                        ║",
        "╚════════════════════════════════════════╝"
    ]

    for line in title:
        print(f"{BLUE}{line}{RESET}")
        time.sleep(0.3)
    
    time.sleep(0.5)
    
    # Create the quote box
    quote = "I'm terrified of eternity - not because it's forever, but because I forgot to bring a book."
    
    max_len = max(len(line) for line in quote.split("\n"))
    
    print(f"\n{RED}╔{'═' * (max_len + 4)}╗{RESET}")
    print(f"{RED}║{RESET}  ", end="")
    
    # Animated typing inside box
    woody_print(f"{ITALIC}{quote}{RESET}", YELLOW, 0.03)
    
    print(f"{RED}╚{'═' * (max_len + 4)}╝{RESET}\n")
    
    # Flashing signature
    time.sleep(1)
    for _ in range(3):
        print(f"{BOLD}{RED}-> Woody Allen <-\r{RESET}", end="")
        time.sleep(0.3)
        print(f"{BOLD}{BLUE}-> Woody Allen <-\r{RESET}", end="")
        time.sleep(0.3)
    print(f"{BOLD}{YELLOW}-> Woody Allen <-\n{RESET}")

if __name__ == "__main__":
    main()