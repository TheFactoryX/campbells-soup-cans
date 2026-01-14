"""
Campbell's Soup Can #1605
Produced: 2026-01-14 15:38:31
Worker: Qwen: Qwen2.5-VL 7B Instruct (free) (qwen/qwen-2.5-vl-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
from termcolor import colored, cprint

def print_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print(colored(quote, 'red', attrs=['bold']))

def animate_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print(colored(quote, 'red', attrs=['bold']))
    for i in range(5):
        print("\033[F", end="")
        time.sleep(0.5)
        print(colored(quote, 'red', attrs=['bold']))

def main():
    print_quote()
    animate_quote()

if __name__ == "__main__":
    main()