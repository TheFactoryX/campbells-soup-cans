"""
Campbell's Soup Can #1570
Produced: 2026-01-12 23:28:43
Worker: Qwen2.5 72B Instruct (qwen/qwen-2.5-72b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# ASCII art of a Woody Allen character
ascii_art = f"""
{RED}   _,-'  `-._
{YELLOW} /          \\
{GREEN}//|        |\\
{BLUE}((o)\\__  __/(o))
{MAGENTA} `.'  ||  `.'
{CYAN}   /  ,  \\
{RED}  /    ===  \\
{YELLOW} /         === \\
{GREEN}/               \\
{BLUE} `.  .-^- .--.  .'
{MAGENTA} `-._``-:_-:'_.-'
{CYAN} `._    (_)    _.'
{RED}   `--._'-.--'
{RESET}
"""

# Woody Allen style quote
quote = f"{GREEN}\"{YELLOW}I'm not afraid of death; I just don't want to be there when it happens.{GREEN}\"{RESET}"

def print_with_typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def main():
    print(ascii_art)
    print_with_typing_effect(quote)

if __name__ == "__main__":
    main()