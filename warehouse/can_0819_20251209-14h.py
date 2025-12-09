"""
Campbell's Soup Can #819
Produced: 2025-12-09 14:41:30
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
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
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# ASCII art components
GLASSES = """
   __
  /  O  \\
 /_____\ 
"""
THOUGHT_BUBBLE = """
  .-.   .-=.
 /   \\ /   \\
|     |     |
 \\___/ \\___/
"""

def colored(text, color):
    return f"{color}{text}{RESET}"

def spinner(duration=1):
    for _ in range(duration * 4):
        sys.stdout.write(f"{CYAN}> {RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write("\b\b\b\b")

def print_boxed_quote(quote, border_color=BLUE, text_color=GREEN):
    max_width = max(len(line) for line in quote.split('\n'))
    top_bottom = f"{border_color}┌{'─' * (max_width + 2)}┐{RESET}"
    side = f"{border_color}│{RESET}"
    
    print(top_bottom)
    for line in quote.split('\n'):
        padded_line = f"{side} {text_color}{line.ljust(max_width)} {RESET}{side}"
        print(padded_line)
    print(top_bottom)

def main():
    # Intro animation
    print(colored("\nWoody Allen's Neurotic Philosopher Mode Activated:", MAGENTA))
    spinner(1.5)
    
    # Display glasses ASCII art
    print(colored(GLASSES, YELLOW))
    time.sleep(0.5)
    
    # Thought bubble
    print(colored(THOUGHT_BUBBLE, CYAN))
    time.sleep(1)
    
    # The philosophical quote
    quote = """I’d rather have a small, painful existence 
than a large, painless void—mostly because 
I can’t afford the anesthesia."""
    
    print_boxed_quote(quote)
    
    # Funny signature
    time.sleep(1)
    print(colored("\n- Said while avoiding commitment and dental work", RED))

if __name__ == "__main__":
    main()