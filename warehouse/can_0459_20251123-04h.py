"""
Campbell's Soup Can #459
Produced: 2025-11-23 04:04:06
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from colorama import init, Fore, Style

init()  # Initialize colorama

def woody_allen_quote():
    print(f"{Fore.YELLOW}Okay, okay, here we go...{Style.RESET_ALL}")
    print("∞")
    print("   _____      _____")
    print("  /      \\    /      \\")
    print(" /        \\  /        \\")
    print("|   O   O  | |   O   O  |")
    print(" \\        /  \\        /")
    print("  \\_____/    \\_____/")
    print(f" {Fore.MAGENTA}\"I'm not a morning person. I'm not a night person. I'm a 'whenever the coffee kicks in' person.\"{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}\"The only thing I know is that I know nothing. And that's what makes life so... uncertain.\"{Style.RESET_ALL}")
    print(f"  {Fore.RED}\"I'm not a neurotic, I'm just passionately committed to being anxious.\"{Style.RESET_ALL}")

def animation():
    quotes = [
        "∞",
        "   _____      _____",
        "  /      \\    /      \\",
        " /        \\  /        \\",
        "|   O   O  | |   O   O  |",
        " \\        /  \\        /",
        "  \\_____/    \\_____/",
        " {Fore.MAGENTA}\"I'm not a morning person. I'm not a night person. I'm a 'whenever the coffee kicks in' person.\"{Style.RESET_ALL}",
        " {Fore.CYAN}\"The only thing I know is that I know nothing. And that's what makes life so... uncertain.\"{Style.RESET_ALL}",
        " {Fore.RED}\"I'm not a neurotic, I'm just passionately committed to being anxious.\"{Style.RESET_ALL}"
    ]
    for i in range(len(quotes)):
        time.sleep(0.5)
        print(f" {quotes[i]}")
        if i < len(quotes) - 1:
            print(f" {Style.RESET_ALL}{Fore.CYAN}\"{random.choice(quotes[len(quotes)-1:i+1])**Style.RESET_ALL}\"")

woody_allen_quote()
animation()