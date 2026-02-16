"""
Campbell's Soup Can #2267
Produced: 2026-02-16 21:44:44
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

YELLOW = '\033[93m'
CYAN = '\033[96m'
GRAY = '\033[90m'
RESET = '\033[0m'

def print_with_delay(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

sys.stdout.write("\033[H\033[J")
print_with_delay(f"{GRAY}  ~  ~  ~  {RESET}\n", 0.1)
print_with_delay(f"{GRAY}  (ò̖ ̖̀o)  {RESET}\n", 0.1)
print_with_delay(f"{GRAY}   \\ ̗̀| ̖́/   {RESET}\n\n", 0.1)

width = 52
top = f"{YELLOW}╔{'═' * width}╗{RESET}"
bottom = f"{YELLOW}╚{'═' * width}╝{RESET}"

quote = "My therapist says I have a preoccupation with vengeance. \nWe'll see when she gets MY electric bill."

print(top)
lines = [line.ljust(width - 2) for line in quote.split('\n')]

for line in lines:
    sys.stdout.write(f"{YELLOW}║ {CYAN}")
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
    sys.stdout.write(f"{CYAN} {YELLOW}║{RESET}\n")
    time.sleep(0.3)

print(bottom)
print(f"\n{YELLOW}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
print_with_delay(f"{CYAN}     Woody Allen would've overanalyzed this moment{RESET}", 0.04)
sys.stdout.write("\n\n")