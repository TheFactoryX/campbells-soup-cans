"""
Campbell's Soup Can #4621
Produced: 2026-08-16 05:43:21
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def color(text, code):
    return f"{code}{text}\033[0m"

def type_word(word, col):
    for c in word:
        sys.stdout.write(color(c, col))
        sys.stdout.flush()
        time.sleep(0.06)
    sys.stdout.write(' ')
    sys.stdout.flush()
    time.sleep(0.2)

def main():
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # ASCII art header    
    print(color("+-----------------------------+", CYAN))
    print(color("[ O ]", RED) + " " * 22 + color("+----------------------------+", CYAN))
    print(color(" |                        |    |", RED))
    print(color(" | Existential Crisis Hub |    |", RED))
    print(color(" |                        |----", RED) + color(" [!] Please Wait...", YELLOW))
    print(color("+-------------------------+----+", CYAN))
    time.sleep(3)
    
    print("\n")
    
    # The quote in segmented colors
    parts = [
        ("I'm", RED), ("not", BLUE), ("afraid", GREEN), 
        ("of death,", CYAN), ("I", YELLOW), ("just", WHITE),
        ("don't", RED), ("want", BLUE), ("to die,", GREEN),
        ("because", CYAN), ("I", YELLOW), ("procrastinate", WHITE),
        ("everything,", RED), ("including", BLUE),
        ("my", GREEN), ("existential", CYAN), ("crisis.", YELLOW),
    ]
    
    for word, col in parts:
        type_word(word, col)
    
    print(f"\n\n{color(" — Woody Allen (probably)", CYAN + YELLOW)}")
    time.sleep(3)

if __name__ == "__main__":
    main()