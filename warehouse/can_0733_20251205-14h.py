"""
Campbell's Soup Can #733
Produced: 2025-12-05 14:37:07
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import time
import os
import sys
import ctypes

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

# Drop shadow effect
def print_with_shadow(text, style):
    shadow = text.replace(" ", "  ").upper()  # Create shadow effect
    print(f"{BLUE}{shadow}{RESET}")
    print(style + text + RESET)

# Animated border with loading effect
def animated_border():
    border = "╒════════════════════════════╕"
    print(border)
    for i in range(3):
        sys.stdout.write(f"\033[{i + 1}B\033[")
        if i % 2 == 0:
            print(f"║{RED}\x1b[5m{\x1b[0m{\x1b[5m"
                  f"{RESET}{MAGENTA}]▌▌]▌"
                  f"{RESET}{RED][{BOLD}]}
        else:
            print(f"║{GREEN}\x1b[5m█êêêê\x1b[0m"
                  f"{RESET}{MAGENTA}]⌐⌐{RESET}{BLUE}]⌐⌐⌐")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"║{RESET}{cursor_up(i + 1)}")

# Little Prince character
PRINCE = f"""
{BLUE}                 (__,
                (oo)
        _,---.   (..
      .-'-------'`.//\\
     //         \\└┴─┐
    ||           |
     \\({});
     `'-..___.-\\{RESET}{cursor_up(9)}"""

# Quote in animated form
QUOTE = f"""
{YELLOW}      __           __         __                  __
     /\\ \\         / /        / /                 / /                
    /\\  \\ \\____   / / /\\      \\ \\      ___     / / ______   _____ 
    \\ \\_\\ \\  _ \\ / / / /       \\ \\    / __ \\   / / /_  __ \\ / ___ \\
     \\ ___ \\  __// / / /___     \\ \\  / /_/ /  / /   / / / / / /__/ /
      \\__/ \\__|/___/\\____/      \\_\\ \\____/   /_/   /_/ /_/  \\____/ 
{YELLOW}
                        I'm not afraid of rivers.
                      I'm afraid of five, just five.
                      Five is an unlucky number.
                      That's why I swim nowhere all year."""

# Reset cursor position
cursor_up = lambda n: f"\033[{n}A\033[{n}D"

def main():
    # Clear screen for Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Set console title for Windows
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW("Woody Allen's Neurosis")
    
    # Animated Prince appears
    sys.stdout.write(PRINCE)
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write(cursor_up(9))
    time.sleep(0.5)
    
    # Animated border
    animated_border()
    
    # Enter message
    sys.stdout.write(cursor_up(12) + "\033[K" + f"\033[10B{WHITE}              WHOOSH!        {RESET}")
    time.sleep(0.7)
    sys.stdout.write(cursor_up(1) + "\033[K" + f"{GREEN}              THE PRINCE         {RESET}")
    time.sleep(0.7)
    sys.stdout.write(cursor_up(1) + "\033[K" + f"{BOLD}{ITALIC}              DISAPPEARED!       {RESET}")
    time.sleep(1.0)
    
    # Show final quote
    sys.stdout.write(cursor_up(3) + "\033[K" + cursor_up(4) + "\033["
    for line in QUOTE.split('\n'):
        sys.stdout.write(cursor_down(1) + "\033[0G" + line)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.0)
    
    # Credits
    sys.stdout.write(cursor_down(5) + "\033[0G" + f"{BOLD}{RED}              ↙     ↘          {RESET}")
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{GREEN}           ┌───────────────┐   {RESET}")
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{YELLOW}           │{BOLD}       BY:       {RESET}{YELLOW}│   {RESET}")
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{YELLOW}           │     {MAGENTA}WOODY ALLEN{RESET}{YELLOW}    │   {RESET}")
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{GREEN}           └───────────────┘   {RESET}")
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{BOLD}{RED}              ↖     ↙          {RESET}")
    time.sleep(1.5)
    
    # Final message
    sys.stdout.write(cursor_down(5) + "\033[0G" + f"{BOLD}{GREEN}                  ΘΘΘ   {RESET}")
    time.sleep(1.0)
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{BOLD}{GREEN}                 •••••         {RESET}")
    time.sleep(0.5)
    sys.stdout.write(cursor_down(1) + "\033[0G" + f"{BOLD}{GREEN}                  ▄▄▄                {RESET}")

if __name__ == "__main__":
    main()