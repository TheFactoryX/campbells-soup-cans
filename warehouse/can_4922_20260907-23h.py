"""
Campbell's Soup Can #4922
Produced: 2026-09-07 23:30:21
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
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WHITE = '\033[97m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05, color=Colors.YELLOW):
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header():
    header = f"""
{Colors.CYAN}    ╔══════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║              {Colors.BOLD}WOODY ALLEN'S NEUROTIC PHILOSOPHY{Colors.CYAN}               ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(header)

def create_box(text, width=70):
    lines = []
    words = text.split()
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width - 4:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    max_len = max(len(line) for line in lines) if lines else 0
    padded_lines = [f"│ {line.ljust(max_len)} │" for line in lines]
    
    top = f"┌{'─' * (max_len + 2)}┐"
    bottom = f"└{'─' * (max_len + 2)}┘"
    
    return [top] + padded_lines + [bottom]

def main():
    clear_screen()
    
    # Print header with animation
    print_header()
    time.sleep(1)
    
    # The Woody Allen style quote
    quote = "I'm not afraid of death, I just don't want to be there when it happens. \
Actually, I'd prefer not to be there for most things - meetings, birthdays, my own existence. \
The universe is indifferent, I'm neurotic, and somehow this is the best I can do."
    
    print(f"\n{Colors.BOLD}{Colors.WHITE}    A philosophical musing from a perpetually anxious filmmaker:{Colors.RESET}\n")
    
    # Create and print the box
    box_lines = create_box(quote)
    
    for i, line in enumerate(box_lines):
        if i == 0 or i == len(box_lines) - 1:
            print(f"{Colors.BLUE}    {line}{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}    {line}{Colors.RESET}")
        time.sleep(0.1)
    
    # Animated signature
    print(f"\n{Colors.ITALIC}{Colors.YELLOW}")
    type_text("    — Woody Allen's Therapist, probably", delay=0.08)
    print(Colors.RESET)
    
    # Final existential thought
    time.sleep(0.5)
    print(f"\n{Colors.RED}{Colors.ITALIC}")
    type_text("    Why am I here? What's the meaning of life? Does my therapist really like me?", delay=0.1)
    print(Colors.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Well, I guess even philosophy needs a break...{Colors.RESET}")
        sys.exit(0)