"""
Campbell's Soup Can #2587
Produced: 2026-03-05 18:21:45
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import textwrap

YELLOW = '\033[93m'
BLUE_BG = '\033[44m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

quote = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "But let's be honest, I'm not sure I want to be anywhere. "
    "Existence is like a bad play: poorly written, with too many intermissions, "
    "and the refreshments are terrible. Also, the audience keeps coughing."
)

total_width = 60
inner_width = total_width - 4
wrapped = textwrap.wrap(quote, inner_width)

time.sleep(0.5)

print(f"{YELLOW}{'=' * total_width}{RESET}")
print(f"{YELLOW}|{RESET}{' ' * (total_width - 2)}{YELLOW}|{RESET}")

for i, line in enumerate(wrapped):
    padded = line.ljust(inner_width)
    inner_str = f" {padded} "
    
    print(f"{YELLOW}|{RESET}", end='', flush=True)
    time.sleep(0.1)
    
    if i == len(wrapped) - 1:
        print(f"{BOLD}{BLUE_BG}{WHITE}", end='', flush=True)
    else:
        print(f"{BLUE_BG}{WHITE}", end='', flush=True)
    
    for char in inner_str:
        print(char, end='', flush=True)
        time.sleep(0.015)
    
    print(f"{RESET}{YELLOW}|{RESET}", flush=True)

print(f"{YELLOW}|{RESET}{' ' * (total_width - 2)}{YELLOW}|{RESET}")
print(f"{YELLOW}{'=' * total_width}{RESET}")

time.sleep(0.3)
print(f"\n{BOLD}{YELLOW}  Why is eternity so short?{RESET}")
time.sleep(0.5)
print(f"{BLUE_BG}{WHITE}  (Probably because I'm in it){RESET}")
time.sleep(0.7)