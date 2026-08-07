"""
Campbell's Soup Can #4461
Produced: 2026-08-07 16:08:45
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI color codes
COLORS = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
BOLD_WHITE = '\033[1;37m'
RESET = '\033[0m'

def typewriter(text, delay=0.07):
    for ch in text:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    quote = "I think the universe is a cosmic joke, and I'm the punchline that keeps asking why."
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    width = len(quote) + 4
    top = f"{BOLD_WHITE}+{'-'*width}+{RESET}"
    side = f"{BOLD_WHITE}|{RESET}"
    print(top)
    # Empty line inside box
    print(f"{side}  {' ' * len(quote)}  {side}")
    print(top)
    # Move cursor to inside box (row 2, column 4)
    sys.stdout.write(f"\033[2;4H")
    sys.stdout.flush()
    typewriter(quote)

if __name__ == "__main__":
    main()
