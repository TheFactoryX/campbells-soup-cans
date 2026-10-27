"""
Campbell's Soup Can #5173
Produced: 2026-10-27 05:06:48
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import textwrap

# Woody Allen style quote
quote = """
I'm not afraid of death; I just don't want to be there when it happens. 
But then again, I'm also terrified of being late to my own funeral, 
mostly because I hate waiting in line for anything, even eternity.
"""

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def print_slow(text, delay=0.03, color=Colors.RESET):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_border(width=60):
    """Create a decorative border"""
    top_bottom = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"
    return top_bottom, bottom

def wrap_text(text, width=55):
    """Wrap text to fit within specified width"""
    lines = []
    for paragraph in text.strip().split('\n'):
        wrapped = textwrap.wrap(paragraph, width=width)
        lines.extend(wrapped if wrapped else [''])
    return lines

def main():
    # Clear screen (works on most systems)
    print("\033[2J\033[H", end="")
    
    # Print Woody Allen style header
    print(f"\n{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}{Colors.YELLOW}{Colors.BOLD}              WOODY ALLEN'S NEUROTIC PHILOSOPHY                {Colors.RESET}{Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    # Create border
    width = 62
    top_border, bottom_border = create_border(width)
    
    # Print top border
    print(f"{Colors.BLUE}{top_border}{Colors.RESET}")
    
    # Wrap and print quote with typewriter effect
    lines = wrap_text(quote, width=width - 4)  # Account for padding and borders
    
    for line in lines:
        # Print left border with padding
        print(f"{Colors.BLUE}│{Colors.RESET} {Colors.YELLOW}{Colors.ITALIC}", end="")
        print_slow(line, delay=0.02, color=Colors.YELLOW)
        print(f"{Colors.RESET} {Colors.BLUE}│{Colors.RESET}")
    
    # Print bottom border
    print(f"{Colors.BLUE}{bottom_border}{Colors.RESET}")
    
    # Print a funny footnote
    print(f"\n{Colors.RED}{Colors.ITALIC}* According to a very anxious person *{Colors.RESET}")
    
    # Print existential crisis counter
    print(f"{Colors.WHITE}Existential Dread Level: {Colors.RED}9/10{Colors.RESET}")
    print(f"{Colors.WHITE}Anxiety about mortality: {Colors.RED}DEFCON 1{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Even my existential crisis got interrupted...{Colors.RESET}")