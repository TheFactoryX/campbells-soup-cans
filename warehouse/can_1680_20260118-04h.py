"""
Campbell's Soup Can #1680
Produced: 2026-01-18 04:13:43
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED    = '\x1b[31m'
GREEN  = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE   = '\x1b[34m'
MAGENTA= '\x1b[35m'
CYAN   = '\x1b[36m'
RESET  = '\x1b[0m'

def typewriter(txt, color=YELLOW, delay=0.02):
    """Print text character‑by‑character with a color and a tiny delay."""
    for ch in txt:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    # Clear the terminal (ANSI escape sequence)
    sys.stdout.write('\x1b[2J\x1b[H')
    
    # Top border
    print(f"{RED}+{'-'*56}+{RESET}")
    
    # Decorative interior line
    print(f"{RED}| {BLUE}Existential Comedy:{RESET} {CYAN} — a Woody Allen thought bubble{RESET} |")
    
    # Bottom border of the inner box
    print(f"{RED}+{'-'*56}+{RESET}")
    
    # The philosophical quote (type‑written for drama)
    quote = "I’m not afraid of death; I just don’t want to be there when it happens."
    typewriter(f"\"{quote}\"", color=MAGENTA, delay=0.03)
    typewriter(f" — {BLUE}Woody Allen{RESET}", color=CYAN, delay=0.02)
    
    # Closing border
    print(f"{RED}+{'-'*56}+{RESET}")

if __name__ == '__main__':
    main()