"""
Campbell's Soup Can #5110
Produced: 2026-10-15 09:55:36
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color=Colors.YELLOW):
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_glasses():
    glasses = f"""
    {Colors.BOLD}{Colors.PURPLE}
       ___
      (   )
       ) (
      (___)
    {Colors.RESET}
    """
    print(glasses)

def print_quote():
    quote = f"""{Colors.ITALIC}{Colors.YELLOW}
    "I don't want to achieve immortality through my work;
     I want to achieve it through not dying.
     ...though given my luck, I'll probably be immortal 
     through my unpaid parking tickets."
    {Colors.RESET}"""
    
    border = f"{Colors.BLUE}┌──────────────────────────────────────────────────────┐{Colors.RESET}"
    bottom_border = f"{Colors.BLUE}└──────────────────────────────────────────────────────┘{Colors.RESET}"
    
    print(border)
    print(f"{Colors.BLUE}│{Colors.RESET} " + " " * 58 + f" {Colors.BLUE}│{Colors.RESET}")
    print(f"{Colors.BLUE}│{Colors.RESET} {Colors.BOLD}{Colors.CYAN}WOODY ALLEN STYLE{Colors.RESET} " + " " * 41 + f"{Colors.BLUE}│{Colors.RESET}")
    print(f"{Colors.BLUE}│{Colors.RESET} " + " " * 58 + f" {Colors.BLUE}│{Colors.RESET}")
    
    # Split quote into lines and center them
    lines = quote.split('\n')
    for line in lines:
        if line.strip():
            # Remove ANSI codes for length calculation
            clean_line = line.replace('\033[93m', '').replace('\033[3m', '').replace('\033[0m', '')
            padding = (58 - len(clean_line)) // 2
            print(f"{Colors.BLUE}│{Colors.RESET} {' ' * padding}{line}{' ' * (58 - len(clean_line) - padding)} {Colors.BLUE}│{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}│{Colors.RESET} " + " " * 58 + f" {Colors.BLUE}│{Colors.RESET}")
    
    print(f"{Colors.BLUE}│{Colors.RESET} " + " " * 58 + f" {Colors.BLUE}│{Colors.RESET}")
    print(bottom_border)

def main():
    clear_screen()
    
    # Animated intro
    print(f"\n{Colors.BOLD}{Colors.RED}★ {Colors.YELLOW}EXISTENTIAL CRISIS THEATER {Colors.RED} ★{Colors.RESET}\n")
    
    # Blinking effect
    for _ in range(3):
        sys.stdout.write(f"\r{Colors.GREEN}●{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{Colors.RESET}●{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n")
    print_glasses()
    print("\n")
    
    # Type the quote with different colors for different parts
    type_text(f"{Colors.BOLD}{Colors.PURPLE}Hmm... let me think about this...{Colors.RESET}", 0.05)
    time.sleep(0.5)
    
    print_quote()
    
    # Outro
    print(f"\n{Colors.ITALIC}{Colors.CYAN}* existential dread level: maximum *{Colors.RESET}")
    print(f"{Colors.ITALIC}{Colors.RED}* therapy recommended *{Colors.RESET}\n")

if __name__ == "__main__":
    main()