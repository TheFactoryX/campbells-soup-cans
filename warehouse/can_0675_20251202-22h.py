"""
Campbell's Soup Can #675
Produced: 2025-12-02 22:32:31
Worker: OpenAI: GPT-4o (extended) (openai/gpt-4o:extended)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI escape sequences for colors
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

quote = """
"Don't think of death as an end; think of it as a really, really long coffee break you'll regret not bringing your book to."
"""

def print_with_color(text, color):
    print(color + text + RESET)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

frames = [
    f"{GREEN}    {MAGENTA}▄{RESET}      {CYAN}▄▄▄▄{RESET}    {YELLOW}▄▄▄▄▄▄▄▄▄{RESET}   ",
    f"{GREEN}    {MAGENTA}▄{RESET}    {CYAN}▄     ▄{RESET}  {YELLOW}▄          ▄{RESET}  ",
    f"{GREEN}    {MAGENTA}▄{RESET}   {CYAN}▄       ▄{RESET} {YELLOW} ▄          ▄{RESET}  ",
    f"{GREEN}    {MAGENTA}▄{RESET}  {CYAN}▄         ▄{RESET}{YELLOW} ▄           ▄{RESET} ",
    f"{GREEN}▄   {MAGENTA}▄{RESET}{CYAN}▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}{YELLOW} ▄▄▄▄▄▄▄▄▄{RESET}   ",
    f"{GREEN}▄ ▄▄▄{MAGENTA}▄▄▄▄▄▄▄{RESET}{CYAN}▄▄▄▄▄▄▄▄▄▄{RESET}      ▄▄▄▀",
    f"{GREEN}▄▄{MAGENTA}▄▄▄▄▄▄▄▄▄{RESET}                {YELLOW}▀▀{RESET}  ",
]

def print_animation(frames):
    for _ in range(3):  # Repeat the animation 3 times
        for frame in frames:
            clear_screen()
            print_with_color(frame, "")
            time.sleep(0.3)

# Display animation and then the quote
print_animation(frames)
clear_screen()
print_with_color(quote, BLUE)