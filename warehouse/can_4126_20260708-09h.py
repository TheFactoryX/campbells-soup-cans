"""
Campbell's Soup Can #4126
Produced: 2026-07-08 09:37:04
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def type_line(line, delay=0.03):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

red = '\033[31m'
cyan = '\033[36m'
yellow = '\033[33m'
blue = '\033[34m'
reset = '\033[0m'

title = f"{cyan}WOODY ALLEN'S EXISTENTIAL DREAD{reset}"
print(f"{cyan}{'=' * 60}{reset}")
print(f"{cyan}{title.center(60)}{reset}")
print(f"{cyan}{'=' * 60}{reset}\n")

lines = [
    f"{red}I'm terrified of dying,{reset}",
    f"{cyan}but even more terrified of not making a mark before then.{reset}",
    f"{yellow}Then there's the nagging thought that maybe I already have,{reset}",
    f"{blue}and it's just not a very impressive one.{reset}",
]

print(f"{blue}{'*' * 60}{reset}")
print(f"{blue}* " + " " * 56 + " *{reset}")
for line in lines:
    type_line(line)
print(f"{blue}* " + " " * 56 + " *{reset}")
print(f"{blue}{'*' * 60}{reset}")