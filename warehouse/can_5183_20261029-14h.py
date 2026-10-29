"""
Campbell's Soup Can #5183
Produced: 2026-10-29 14:20:46
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def main():
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."
    
    hyphens = '-' * len(quote)
    
    top = f"{CYAN}+{hyphens}+{RESET}"
    
    def print_colored_line(line_color, text, mid_color=None):
        if mid_color:
            print(f"{line_color}|{mid_color}{text}{line_color}|{RESET}", end='')
        else:
            print(f"{line_color}|{text}|{RESET}", end='')
    
    print(top)
    time.sleep(0.2)
    print_colored_line(RED, quote, GREEN)
    print()  # Newline after the middle line
    time.sleep(0.2)
    print(top)
    
    time.sleep(0.2)
    print(f"{YELLOW}Press Ctrl+C to leave your body. Or don't. It's a minor detail.{RESET}")

if __name__ == "__main__":
    main()