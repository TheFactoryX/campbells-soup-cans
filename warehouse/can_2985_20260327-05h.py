"""
Campbell's Soup Can #2985
Produced: 2026-03-27 05:50:42
Worker: MiniMax: MiniMax M2.7 (minimax/minimax-m2.7)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
A single-file, visually interesting quote display with ANSI colors and ASCII art
"""

import sys
import time
import os

# ANSI Color Codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM = '\033[2m'
ITALIC = '\033[3m'

def typewriter(text, delay=0.03, color=WHITE):
    """Print text character by character with a typewriter effect"""
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def slow_print(text, delay=0.1, color=WHITE):
    """Print text with a delay between lines"""
    print(f"{color}{text}{RESET}")
    time.sleep(delay)

def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Clear screen
    print('\033[2J\033[H', end='')  # VT100 clear screen
    
    # Fancy header ASCII art
    header = f"""
{CYAN}{BOLD}    ╔══════════════════════════════════════════════════════════╗
    ║  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
    ║  █ {YELLOW}░█▀▀░█░█░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░{CYAN}█  ║
    ║  █ {YELLOW}░█▀▀░░█░░█░░░░█░░█░░░░█░░█▀▀░░█░░█░░░{CYAN}█  ║
    ║  █ {YELLOW}░▀░░░░▀░░▀▀▀░▀▀▀░▀░░░▀▀▀░▀░░░░▀░░▀▀▀░{CYAN}█  ║
    ║  █ {YELLOW}░█▀█░█▀▀░▀█▀░█▀█░█▀▀░▀█▀░▀█▀░█▀▀░{CYAN}█  ║
    ║  █ {YELLOW}░█▀▀░█▀▀░░█░░█░█░█▀▀░░█░░░█░░█░░░{CYAN}█  ║
    ║  █ {YELLOW}░▀░░░▀░░░▀▀▀░▀░▀░▀░░░░▀░░░▀░░▀▀▀░{CYAN}█  ║
    ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
    ╚══════════════════════════════════════════════════════════╝{RESET}
"""
    
    print(header)
    
    # Animated subtitle
    subtitle = f"  {MAGENTA}{BOLD}~ Philosophical Wisdom from a Neurotic Genius ~{RESET}"
    for char in subtitle:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    
    # Decorative divider
    print(f"\n{CYAN}  {'═' * 58}{RESET}\n")
    
    # Opening quote mark with animation
    print(f"  {YELLOW}{BOLD}\"", end='', flush=True)
    time.sleep(0.3)
    print(f"{RESET}", end='')
    
    # The MAIN QUOTE - typewriter effect
    quote = [
        (f"{WHITE}I think", 0.04),
        (f" {YELLOW}about death", 0.06),
        (f" {WHITE}a lot.", 0.05),
        (f"\n  {WHITE}Not because", 0.04),
        (f" {MAGENTA}I'm suicidal", 0.06),
        (f" {WHITE}or anything -", 0.05),
        (f"\n  {WHITE}it's just that", 0.04),
        (f" {CYAN}eternity", 0.06),
        (f" {WHITE}bores me,", 0.05),
        (f"\n  {WHITE}and", 0.03),
        (f" {RED}time", 0.06),
        (f" {WHITE}is just", 0.04),
        (f" {GREEN}NOT", 0.08),
        (f" {WHITE}on my side.", 0.05),
    ]
    
    for text, delay in quote:
        print(f"{text}", end='', flush=True)
        time.sleep(delay)
    
    # Closing quote and author
    print(f'{YELLOW}"{RESET}\n')
    time.sleep(0.5)
    
    # Author attribution with style
    print(f"{CYAN}  {'─' * 20}{RESET}")
    time.sleep(0.3)
    print(f"\n  {GREEN}{BOLD}✦ {ITALIC}Woody Allen{RESET}")
    print(f"  {DIM}(filmmaker, hypochondriac, and existential wreck){RESET}")
    
    # Fun footer with emoji-style ASCII
    print(f"\n{CYAN}  {'═' * 58}{RESET}")
    
    footer = f"""
  {YELLOW}        ___________________
  {YELLOW}       /                   \\
  {YELLOW}      |   ___       ___   |
  {YELLOW}      |  |   |     |   |  |
  {YELLOW}      |  | o |     | o |  |
  {YELLOW}      |  |___|     |___|  |
  {YELLOW}      |    _________      |
  {YELLOW}      |   |  ___  |       |
  {YELLOW}      |   | |   | |       |
  {YELLOW}      |   |_|___|_|       |
  {YELLOW}      |___________________|
  {YELLOW}      |  ___    ___    ___|
  {YELLOW}      | |   |  |   |  |   |
  {YELLOW}      | |___|  |___|  |___|
  {YELLOW}      |_____________________|
  {YELLOW}      (  Woody Allen, c. NOW ){RESET}
"""
    print(footer)
    
    # Blinking existential thought
    print(f"\n  {MAGENTA}{ITALIC}(This quote will still be true in 1000 years...){RESET}")
    print(f"  {RED}{BOLD}(assuming the universe doesn't end first){RESET}")

if __name__ == "__main__":
    main()