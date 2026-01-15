"""
Campbell's Soup Can #1630
Produced: 2026-01-15 19:36:52
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes for colors and effects
BLINK = "\033[5m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
CLEAR = "\033c"

quote = (
    "I don't believe in an afterlife, although I am bringing "
    "a change of underwear just in case."
)

def print_with_delay(text, delay=0.05, color=YELLOW):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def animated_loading(duration=1.5):
    steps = ["/-\\|" * 5 for _ in range(3)]
    for step in steps:
        for frame in step:
            print(f"\r{MAGENTA}Contemplating existence {frame}{RESET}", end='')
            time.sleep(duration / len(step))
    print("\r" + " " * 30 + "\r", end='')

def main():
    print(CLEAR)
    animated_loading()
    
    # ASCII art box dimensions
    box_width = len(quote) + 8
    print(f"\n{MAGENTA}╭{'─' * box_width}╮{RESET}")
    print(f"{MAGENTA}│{RESET}  ", end='')
    print_with_delay(quote, color=YELLOW)
    print(f"{MAGENTA}╰{'─' * box_width}╯{RESET}")
    
    time.sleep(1)
    print(f"\n{CYAN}  ― Woody Allen{RESET}", end='')
    
    # Blinking caret effect
    for _ in range(3):
        print(f"{BLINK}_{RESET}", end='\r', flush=True)
        time.sleep(0.5)
        print(" " + " " * len(quote), end='\r')
        time.sleep(0.5)
    
    print()

if __name__ == "__main__":
    main()