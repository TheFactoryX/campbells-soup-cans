"""
Campbell's Soup Can #4573
Produced: 2026-08-13 21:03:19
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

def typewriter(text, delay=0.05):
    """Print text one character at a time with random colors."""
    for ch in text:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_box(text):
    """Print a colored ASCII box around the given text."""
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    border = f"{random.choice(COLORS)}+" + "-" * (width + 2) + f"+{RESET}"
    print(border)
    for line in lines:
        print(f"{random.choice(COLORS)}| {line.ljust(width)} |{RESET}")
    print(border)

def main():
    quote = (
        "I think the universe is a cosmic joke, "
        "and I'm the punchline that keeps asking why."
    )
    header = "Woody Allen Style Philosophical Quote"
    print_box(header)
    typewriter(quote, delay=0.07)

if __name__ == "__main__":
    main()
