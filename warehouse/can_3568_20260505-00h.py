"""
Campbell's Soup Can #3568
Produced: 2026-05-05 00:08:05
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

COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m'
}

def print_couch():
    lines = [
        "    __§§__",
        "   /  §§  \\",
        "  | § § § |",
        "  |_______|",
        "  |_______|",
        "  |_______|"
    ]
    for line in lines:
        print(f"{COLORS['cyan']}{line}{COLORS['reset']}")
        time.sleep(0.1)

def typewriter(text, color, delay=0.03):
    for char in text:
        sys.stdout.write(f"{color}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote(lines, color):
    max_len = max(len(line) for line in lines)
    border = '═' * (max_len + 2)
    
    print(f"{color}╔{border}╗{COLORS['reset']}")
    
    for line in lines:
        padded = line.ljust(max_len)
        typewriter(f"║ {padded} ║", color)
    
    print(f"{color}╚{border}╝{COLORS['reset']}")

def main():
    print("\n" * 3)
    print_couch()
    print()
    
    quote_lines = [
        "I tried to embrace the present moment,",
        "but it kept changing channels,",
        "so I sued it for breach of contract.",
        "My lawyer says the case is... present, tense."
    ]
    
    print_quote(quote_lines, COLORS['magenta'])
    
    print(f"\n{COLORS['bold']}{COLORS['yellow']}     (with apologies to existential dread){COLORS['reset']}\n")

if __name__ == "__main__":
    main()