"""
Campbell's Soup Can #3791
Produced: 2026-05-26 16:52:08
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Woody Allen-style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # ANSI color codes
    RESET = "\033[0m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # ASCII art border
    border_top = f"{CYAN}╔{'═' * 60}╗{RESET}"
    border_mid = f"{CYAN}║{RESET}"
    border_bottom = f"{CYAN}╚{'═' * 60}╝{RESET}"
    
    # Print border top
    print(border_top)
    
    # Print quote with formatting
    print(f"{DIM}{border_mid}{RESET}  {YELLOW}{BOLD}★ Woody Allen Philosophy ★{RESET}{DIM}{border_mid}{RESET}")
    print()
    print(f"{CYAN}{border_mid}{RESET}  {GREEN}{quote}{RESET}{DIM}{border_mid}{RESET}")
    print()
    print(f"{DIM}{border_mid}{RESET}  {YELLOW}— A neurotic thought on existence{RESET}{DIM}{border_mid}{RESET}")
    
    # Print border bottom
    print(border_bottom)
    
    # Animated thought bubble
    print(f"\n{DIM}Thinking...{RESET}")
    for i in range(3):
        sys.stdout.write(f"\r{CYAN}{'*' * (i + 1)}{' ' * (2 - i)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\r{CYAN}{'*' * 3}{RESET}")
    
    # Final message
    print(f"\n{BOLD}{YELLOW}Don't forget to live while you're dying!{RESET}{DIM}")

if __name__ == "__main__":
    main()