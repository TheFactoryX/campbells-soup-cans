"""
Campbell's Soup Can #1619
Produced: 2026-01-15 07:37:58
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes
YELLOW = "\033[38;5;11m"
BG_BLUE = "\033[48;5;17m"
RESET = "\033[0m"
BOLD = "\033[1m"

quote = (
    "I'm torn between the existential dread of cosmic insignificance "
    "and the crushing responsibility of having to choose what's "
    "for dinner - like some kind of deity presiding over my own "
    "personal universe of mediocre takeout options."
)

def print_thought_bubble():
    print(f"{BG_BLUE}{YELLOW}", end="")
    print(r'''
     ___ 
   .'   `.
  /       \
 |         |
 |         |_
  \       _  `-.
   `.___.' `._  `-._''')
    print(RESET)

def print_speaker():
    print(f"{BOLD}{YELLOW}")
    print(r'''
        o
         o
           o
       ___      o
      (   ) 
       \ /''')
    print(RESET)

def main():
    # Print thought bubble with typing animation
    print_thought_bubble()
    print(f"{BG_BLUE}{YELLOW}  ", end="")
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.03 if char not in '.,;:' else 0.2)
    print(f"  {RESET}\n")
    
    # Print Woody Allen-esque speaker
    print_speaker()
    
    # Print signature line
    print(f"{BOLD}{YELLOW}       - Woody Allen's Anxiety{RESET}")

if __name__ == "__main__":
    main()