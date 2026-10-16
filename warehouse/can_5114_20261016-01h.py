"""
Campbell's Soup Can #5114
Produced: 2026-10-16 01:21:32
Worker: Tencent: Hy3 (tencent/hy3)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
BLINK = "\033[5m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

def typewriter(text, color, delay=0.025):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def main():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    
    sys.stdout.write(MAGENTA + BOLD + "WOODY ALLEN'S EXISTENTIAL SIMULATOR v0.1" + RESET + "\n")
    time.sleep(0.4)
    sys.stdout.write(DIM + "Calibrating neurosis...")
    for _ in range(3):
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n\n" + RESET)
    time.sleep(0.6)
    
    inner_width = 74
    
    sys.stdout.write(CYAN + "╔═" + "═" * inner_width + "═╗\n" + RESET)
    
    quote_lines = [
        "My neurosis is very egalitarian: it doesn't care about my IQ,",
        "my Oscar, or my cholesterol—it just sits in the corner of my",
        "tiny apartment whispering, 'None of this will be remembered,",
        "and frankly, neither will you, but hey, want a bagel?'"
    ]
    
    for line in quote_lines:
        sys.stdout.write(CYAN + "║ " + RESET)
        typewriter(line, YELLOW, 0.02)
        pad = inner_width - len(line)
        sys.stdout.write(CYAN + " " * pad + " ║\n" + RESET)
        time.sleep(0.3)
        
    sys.stdout.write(CYAN + "╚═" + "═" * inner_width + "═╝\n" + RESET)
    
    time.sleep(0.5)
    sys.stdout.write(DIM + " " * 18)
    typewriter("— Woody Allen (as transcribed by an anxious Python script)", BLUE, 0.01)
    print("\n")
    
    sys.stdout.write(BLINK + CYAN + "█" + RESET)
    time.sleep(1.5)
    print("\n")

if __name__ == "__main__":
    main()