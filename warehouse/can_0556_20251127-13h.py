"""
Campbell's Soup Can #556
Produced: 2025-11-27 13:02:11
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def print_quote():
    # ANSI color codes
    BROWN = "\033[38;5;94m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    RED = "\033[31m"
    RESET = "\033[0m"
    
    # Clear screen
    print("\033[2J\033[H")
    
    # Coffee cup ASCII art
    cup = f"""{BROWN}
      ( (
       ) )
  ) ) ( (
 ( (  - )
  \\_/  /
   {RESET}"""
    print(cup)
    time.sleep(0.5)
    
    # Quote with border animation
    quote = "Life is meaningless, but at least there's coffee. And even that's decaf in my case."
    border_top = f"{CYAN}╭{''.join(['─' for _ in range(len(quote)+2)])}╮{RESET}"
    border_bottom = f"{CYAN}╰{''.join(['─' for _ in range(len(quote)+2)])}╯{RESET}"
    
    # Typewriter effect
    def typewriter(text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    print(border_top)
    print(f"{CYAN}│ {RESET}", end="")
    typewriter(f"{YELLOW}{quote}{RESET}", 0.03)
    print(f"{CYAN}│{RESET}")
    print(border_bottom)
    time.sleep(1)
    
    # Funny postscript
    ps = f"{RED}\n  (Meanwhile, the espresso machine judges you silently){RESET}"
    for char in ps:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

if __name__ == "__main__":
    print_quote()