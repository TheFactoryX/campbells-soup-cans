"""
Campbell's Soup Can #2113
Produced: 2026-02-08 08:50:38
Worker: Pony Alpha (openrouter/pony-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def wobble_text(text):
    wobble_chars = text
    for i in range(3):
        for offset in [-1, 0, 1]:
            sys.stdout.write("\033[F\033[K")
            spaces = " " * max(0, offset + 1)
            print(f"{spaces}\033[38;5;221m{wobble_chars}\033[0m")
            time.sleep(0.08)

# ANSI colors
PURPLE = "\033[38;5;141m"
YELLOW = "\033[38;5;221m"
RED = "\033[38;5;203m"
CYAN = "\033[38;5;117m"
GREEN = "\033[38;5;120m"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

# ASCII Woody (neurotic philosopher)
woody = f"""
{DIM}        .-"""-.
       /        \\
      |  {CYAN}O  {DIM}  {CYAN}O{DIM}  |    {PURPLE}*internal screaming*{DIM}
      |   __    |
       \\  __/  /
        '----'""""

quote = "My therapist says I have a fear of commitment,\nbut I'm afraid to commit to that diagnosis."

box_top = "╔" + "═" * 52 + "╗"
box_bottom = "╚" + "═" * 52 + "╝"

print("\033[2J\033[H")
print(woody)
time.sleep(0.5)

print(f"\n{YELLOW}{box_top}{RESET}")
print(f"{YELLOW}║{RESET}" + " " * 52 + f"{YELLOW}║{RESET}")

words = quote.split()
line = "  "
for word in words:
    if len(line) + len(word) + 1 > 50:
        print(f"{YELLOW}║{RESET}" + line + " " * (52 - len(line)) + f"{YELLOW}║{RESET}")
        line = "  " + word + " "
    else:
        line += word + " "
if line.strip():
    print(f"{YELLOW}║{RESET}" + line + " " * (52 - len(line)) + f"{YELLOW}║{RESET}")

print(f"{YELLOW}║{RESET}" + " " * 52 + f"{YELLOW}║{RESET}")
print(f"{YELLOW}║{RESET}" + " " * 38 + f"{DIM}{ITALIC}— Woody Allen (probably){RESET}   {YELLOW}║{RESET}")
print(f"{YELLOW}{box_bottom}{RESET}\n")

for i in range(5):
    anxieties = ["existential dread", "commitment issues", "cosmic insignificance"]
    anxiety = random.choice(anxieties)
    print(f"\r{RED}⚠ {DIM}Current anxiety level: {anxiety}...{RESET}    ", end="")
    time.sleep(0.4)
print(f"\r{GREEN}✓ Anxiety stabilized (for now){RESET}     \n")