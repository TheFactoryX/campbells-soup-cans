"""
Campbell's Soup Can #2388
Produced: 2026-02-23 07:31:42
Worker: Perplexity: Sonar Pro Search (perplexity/sonar-pro-search)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
class Colors:
    RED = '\033[91m'    GREEN = '\033[92m'    YELLOW = '\033[93m'    BLUE = '\033[94m'    MAGENTA = '\033[95m'    CYAN = '\033[96m'    WHITE = '\033[97m'    BOLD = '\033[1m'    UNDERLINE = '\033[4m'    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, color=Colors.WHITE, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(flush=True)

def print_woody_art():
    art = f"""
{Colors.BOLD}{Colors.CYAN}
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░  {Colors.YELLOW}WOODY ALLEN'S NEUROTIC WISDOM{Colors.CYAN}  ░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{Colors.RESET}
    """
    print(art)

def animate_quote():
    clear_screen()
    print_woody_art()
    
    quote = "I'm not afraid of the universe's indifference; I just hate that it's so disappointed in ME too."
    
    # Typing animation with neurotic pauses
    print_slow(f"{Colors.BOLD}{Colors.MAGENTA}“", color=Colors.MAGENTA, delay=0.1)
    print_slow(quote[:30], Colors.YELLOW, 0.08)
    time.sleep(0.3)  # Neurotic pause
    print_slow(quote, Colors.YELLOW, 0.08)
    time.sleep(0.5)  # Existential hesitation
    print_slow(quote[55:], Colors.YELLOW, 0.08)
    print_slow(f"{Colors.MAGENTA}”{Colors.RESET}", color=Colors.MAGENTA, delay=0.1)
    
    # Fancy underline box
    print(f"\n{Colors.CYAN}╔{'═' * 70}╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BLUE}{' ' * 70}{Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.GREEN}     Life: 99% anxiety, 1% bagels, 0% cosmic meaning{Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BLUE}{' ' * 70}{Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚{'═' * 70}╝{Colors.RESET}")

def main():
    # Neurotic startup sequence
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}Woody.exe initializing... (Why must even programs suffer?)")
    time.sleep(1.2)
    print(f"{Colors.YELLOW}Loading existential dread... 73%{Colors.RESET}")
    time.sleep(0.8)
    
    animate_quote()
    
    # Fade out effect
    time.sleep(2)
    for i in range(10, 0, -1):
        clear_screen()
        print_woody_art()
        print(f"{Colors.BOLD}{Colors.MAGENTA}“{Colors.YELLOW}{quote}{Colors.MAGENTA}”{Colors.RESET}")
        print(f"\n{Colors.DIM}...fading into the void in {i}s{Colors.RESET}")
        time.sleep(0.3)
    
    print(f"\n\n{Colors.GREEN}{Colors.BOLD}Thanks for nothing, universe!{Colors.RESET}")

if __name__ == "__main__":
    main()