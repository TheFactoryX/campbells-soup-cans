"""
Campbell's Soup Can #4542
Produced: 2026-08-11 22:04:48
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
Woody Allen Philosophical Quote Generator
A neurotic musing on existence, served with a side of anxiety
"""

import sys
import time
import random

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
    BLINK = '\033[5m'
    RESET = '\033[0m'

def clear_screen():
    """Clear the terminal screen"""
    print('\033[2J\033[H', end='', flush=True)

def type_writer(text, delay=0.03, color=None, end='\n'):
    """Print text with a typewriter effect"""
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.01))
    sys.stdout.write(Colors.RESET)
    sys.stdout.write(end)
    sys.stdout.flush()

def print_slowly(text, delay=0.02):
    """Print text line by line slowly"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def draw_frame():
    """Draw an elaborate ASCII frame"""
    top = f"{Colors.MAGENTA}╔══════════════════════════════════════════════════════════════════════╗"
    bottom = f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}"
    side = f"{Colors.MAGENTA}║                                                                          ║{Colors.RESET}"
    
    print(top)
    print(side)

def print_ascii_art():
    """Print a nervous little character"""
    art = f"""
    {Colors.CYAN}
           .-'''''-.
          /         \\
         |  .---.  |
         |  |o o|  |
         |  | ^ |  |
         |  '---'  |
          \\_______/
    {Colors.YELLOW}    //     \\\\
    {Colors.BLUE}   ((       ))
    {Colors.MAGENTA}    \\\\_____//
    {Colors.DIM}    /       \\\\
    {Colors.CYAN}   |  O   O  |
    {Colors.YELLOW}   |  _____  |
    {Colors.BLUE}   | |     | |
    {Colors.MAGENTA}   |_|     |_|
    {Colors.RESET}
    """
    print(art)

def print_quotation_box(quote_lines):
    """Print quote inside a nice box"""
    max_len = max(len(line) for line in quote_lines)
    padding = 4
    
    # Top border
    print(f"{Colors.MAGENTA}╔{'═' * (max_len + padding)}╗")
    
    # Quote lines
    for line in quote_lines:
        spaces = ' ' * (max_len - len(line) + padding)
        if line.strip():
            print(f"║   {Colors.BOLD}{Colors.YELLOW}{line}{Colors.RESET}{spaces}{Colors.MAGENTA}║")
        else:
            print(f"║{spaces}{Colors.MAGENTA}║")
    
    # Bottom border
    print(f"╚{'═' * (max_len + padding)}╝{Colors.RESET}")

def main():
    clear_screen()
    
    # Dramatic opening
    intro = f"""
    {Colors.BOLD}{Colors.RED}╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║    {Colors.CYAN} WOODY ALLEN {Colors.YELLOW}PHILOSOPHICAL QUOTE GENERATOR{Colors.RED}              ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(intro)
    time.sleep(1)
    
    # The nervous character
    print(f"{Colors.DIM}Loading profound anxieties..." + Colors.RESET)
    time.sleep(1)
    
    # Random loading dots
    for i in range(3):
        print(f"{Colors.MAGENTA}{'.' * (i+1):>3}{Colors.RESET}")
        time.sleep(0.3)
    
    clear_screen()
    
    # Print the character
    print_ascii_art()
    time.sleep(1)
    
    # The quote - Woody Allen style, neurotic and existential
    quote_lines = [
        "I'm not afraid of dying...",
        "I just don't want to miss the",
        "screening of my life story.",
        "",
        "And what's worse? I'm playing",
        "myself in the movie adaptation.",
        "Talk about method acting!"
    ]
    
    # Type the quote with animation
    full_quote = "\n".join(quote_lines)
    print(f"\n{Colors.BOLD}{Colors.GREEN}", end='')
    type_writer(full_quote, delay=0.04)
    
    time.sleep(1)
    
    # Print in a nice box
    print()
    print_quotation_box(quote_lines)
    
    time.sleep(1)
    
    # Philosophical footnote
    footnote = f"{Colors.ITALIC}{Colors.DIM}— A profound truth that took me 3 hours of therapy to realize{Colors.RESET}"
    print(footnote)
    
    time.sleep(1)
    
    # Existential warning
    print(f"\n{Colors.RED}{Colors.BOLD}WARNING:{Colors.RESET} {Colors.DIM}Reading this quote may cause existential dread,")
    print(f"         sudden urges to call your mother, or mild panic attacks{Colors.RESET}")
    
    time.sleep(1)
    
    # Final flourish
    print(f"\n{Colors.MAGENTA}{'=' * 70}")
    print(f"{Colors.YELLOW}{Colors.BOLD}Remember: The universe doesn't care about your problems,")
    print(f"{Colors.CYAN}but at least your problems are consistent!{Colors.RESET}")
    print(f"{Colors.MAGENTA}{'=' * 70}{Colors.RESET}")

if __name__ == "__main__":
    main()