"""
Campbell's Soup Can #4464
Produced: 2026-08-07 19:15:19
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
RESET = '\033[0m'

def typewriter(text, delay=0.05, end='\n'):
    for ch in text:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def print_box_with_typewriter(text, delay=0.05):
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    border = '*' * (width + 4)
    sys.stdout.write(f"\033[33m{border}\033[0m\n")
    for line in lines:
        sys.stdout.write(f"\033[33m* \033[0m")
        typewriter(line.ljust(width), delay=delay, end='')
        sys.stdout.write(f"\033[33m \033[0m*\n")
    sys.stdout.write(f"\033[33m{border}\033[0m\n")

def main():
    quote = ("I think the universe is a cosmic joke, "
             "and I'm the punchline that keeps asking why.")
    art = r"""
      ____
     / ___|
    | |  _  ___  ___
    | |_| |/ _ \/ __|
     \____|\___/\__ \
     \____/      \___/
    """
    sys.stdout.write('\033[35m' + art + '\033[0m')
    sys.stdout.flush()
    time.sleep(1)
    print_box_with_typewriter(quote, delay=0.07)

if __name__ == "__main__":
    main()
