"""
Campbell's Soup Can #4468
Produced: 2026-08-07 22:55:15
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def type_animation(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class colors:
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def main():
    print(f"{colors.YELLOW}        🌌\n         🌙\n{n colors.RED}☁️\n{colors.CYAN}______{colors.RESET}\n{colors.CYAN}|______|{colors.RESET}", end='    ')
    time.sleep(0.5)
    
    quote = ("I'm not afraid of death; I just hate the paperwork. "\
             "And also I keep losing my keys in the couch cushions, "\
             "but that's a different kind of disappearing act.")
    
    time.sleep(1)
    
    quote_length = len(quote)
    border = f"+{'—' * (quote_length + 2)}+"
    top = f"{colors.CYAN}{border}{colors.RESET}"
    bottom = f"{colors.GREEN}{border}{colors.RESET}"
    
    print(f"{colors.CYAN}{top}{colors.RESET}")
    sys.stdout.flush()
    time.sleep(0.3)
    
    left_part = f"{colors.CYAN}| "
    right_part = f"{colors.CYAN} |"
    
    sys.stdout.write(left_part)
    sys.stdout.flush()
    sys.stdout.write(colors.WHITE)
    sys.stdout.flush()
    type_animation(f" {quote} ", delay=0.04)
    sys.stdout.write(right_part + "\n")
    sys.stdout.flush()
    
    time.sleep(0.5)
    print(f"{colors.GREEN}{bottom}{colors.RESET}")
    
    time.sleep(1)
    
    print(f"""
    {colors.RED}🤔 Thought Bubble: 
           ╔════════════╗
           ║ 'Or maybe I'm a    ║
           ║  profound existential  ║
           ║  metaphor for my    ║
           ║  missing sock?'      ║
           ╚════════════╝""")
    print(f"{colors.RESET}" + "="*40)

if __name__ == "__main__":
    main()