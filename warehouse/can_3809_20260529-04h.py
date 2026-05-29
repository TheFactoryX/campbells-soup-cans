"""
Campbell's Soup Can #3809
Produced: 2026-05-29 04:43:00
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def clear_screen():
    print("\033[2J\033[H", end="")

def print_ascii_header():
    print(f"{BLUE}{BOLD}")
    print("  ___  _  _  ___  ___ ___ ___ ___ ___ ")
    print(" / _ \/ )( \/ _ \(_  / __ / __ / __ / __|")
    print("/ ___/ /  /    // /(__  (__  (__  \__ \ ")
    print("/_/   \__/\___//___\___/\___/\___/\___/ ")
    print(f"{RESET}")

def animate_text(text, color=YELLOW, delay=0.03):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_rainbow(text):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(f"{color}{char}{RESET}", end="")
    print()

RED = '\033[31m'

def main():
    clear_screen()
    print_ascii_header()
    
    print(f"\n{MAGENTA}Generating existential dread...{RESET}\n")
    time.sleep(1)
    
    quote_lines = [
        "I have a lot of anxiety about my anxiety,",
        "and then I worry about the anxiety of my anxiety.",
        "It's like my therapist said: 'Your neuroses are",
        "not just a hobby—they're a full-time job.'",
        "But at least when I'm dead,",
        "I won't have to attend my own funeral.",
        "Though somehow,",
        "I'll probably find a way to mess that up too."
    ]
    
    border = f"{CYAN}│{RESET}"
    max_length = max(len(line) for line in quote_lines)
    
    print(f"{CYAN}╔{'═' * (max_length + 2)}╗")
    print(f"{border}{' ' * (max_length + 2)}{border}")
    
    for line in quote_lines:
        animated_line = line.ljust(max_length)
        print(f"{border} {RESET}", end="")
        animate_text(animated_line)
        print(f"{border}", end="")
        print(RESET, end="")
    
    print(f"\n{border}{' ' * (max_length + 2)}{border}")
    print(f"╚{'═' * (max_length + 2)}╝\n")
    
    time.sleep(0.5)
    print(" — ", end="")
    print_rainbow("Woody Allen (probably)")
    print()

if __name__ == "__main__":
    main()