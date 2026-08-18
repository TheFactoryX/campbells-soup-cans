"""
Campbell's Soup Can #4677
Produced: 2026-08-18 15:46:08
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI color codes
CYAN = '\033[36m'
RESET = '\033[0m'
# Colors for random letters
COLORS = ['31', '32', '33', '34', '35', '36', '37']

quote = (
    "I think I'm a philosopher, but I keep asking myself if I'm a philosopher "
    "or just a guy who thinks he's a philosopher, and the answer is always "
    "'I don't know, but I'm sure I'm not a genius'."
)

width = len(quote)

def typewriter_line(text, left_border, right_border, delay=0.04):
    sys.stdout.write(left_border)
    for ch in text:
        color = random.choice(COLORS)
        sys.stdout.write(f'\033[{color}m{ch}\033[0m')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(right_border + '\n')
    sys.stdout.flush()

def main():
    # Top border
    sys.stdout.write(CYAN + '┌' + '─' * width + '┐' + RESET + '\n')
    # Empty line
    sys.stdout.write(CYAN + '│' + ' ' * width + '│' + RESET + '\n')
    # Quote line with typewriter effect
    typewriter_line(quote, CYAN + '│' + RESET, CYAN + '│' + RESET)
    # Empty line
    sys.stdout.write(CYAN + '│' + ' ' * width + '│' + RESET + '\n')
    # Bottom border
    sys.stdout.write(CYAN + '└' + '─' * width + '┘' + RESET + '\n')

if __name__ == '__main__':
    main()
