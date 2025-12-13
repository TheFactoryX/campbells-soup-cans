"""
Campbell's Soup Can #914
Produced: 2025-12-13 21:29:13
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

# ANSI escape codes for colors
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def typewriter(text, color=RESET, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Randomly select one of Woody's "profound" observations
    quote = (
        "I'm not afraid of being forgotten by history...\n" 
        "I'm terrified that the cosmic void might forget\n" 
        "to disable my Netflix subscription after I'm gone."
    )

    # Create dramatic pause before the tombstone appears
    time.sleep(0.5)
    
    # ASCII Art Tombstone with colored text
    print("\n"*2)
    typewriter(f"{' ' * 22}⚰️{' ' * 22}", YELLOW, 0.01)
    typewriter(f"{' ' * 15}╔{'═' * 28}╗", YELLOW)
    typewriter(f"{' ' * 15}║{RED}     REST IN PARANOIA       {YELLOW}║", delay=0.02)
    typewriter(f"{' ' * 15}║{' ' * 28}║")
    
    # Split quote into lines for layout
    lines = quote.split('\n')
    for line in lines:
        padded_line = line.center(28)
        typewriter(f"{' ' * 15}║{CYAN}{padded_line}{YELLOW}║", delay=0.02)
    
    typewriter(f"{' ' * 15}╚{'═' * 28}╝", YELLOW)
    typewriter(f"{' ' * 18}|\\{MAGENTA}\"WiFi: afterlife5G\"{RESET}|", delay=0.03)
    typewriter(f"{' ' * 18}|/{MAGENTA}\"Password: oblivion\"{RESET}|", delay=0.03)
    print("\n"*2)

if __name__ == "__main__":
    main()