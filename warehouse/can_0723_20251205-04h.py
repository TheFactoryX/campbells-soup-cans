"""
Campbell's Soup Can #723
Produced: 2025-12-05 04:43:08
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

YELLOW = "\033[93m"
CYAN = "\033[96m"
PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    print("\033c", end="")

clear_screen()

head = [
    f"   {YELLOW}@@@@@@@@@@@{RESET}   ",
    f"  {YELLOW}@@@{PINK}_____{YELLOW}@@@{RESET}  ",
    f" {YELLOW}(@@{PINK}/   \\{YELLOW}@){RESET} ",
    f"{YELLOW} <{PINK}( o o ){YELLOW}> {RESET}",
    f"{YELLOW}  {PINK}\\  -  /{YELLOW}  {RESET} ",
    f"{YELLOW}   {PINK}'---'{YELLOW}   {RESET}  "
]

quote_lines = [
    "I've concluded life is a meaningless void",
    "—but what if I'm wrong? What if it's only",
    "30% void? I'm not taking that risk.",
    "Better to stay home where the void is familiar"
]

width = 38
top_bottom = CYAN + '╭' + '─' * (width + 2) + '╮' + RESET
side = CYAN + '│' + RESET
bottom = CYAN + '╰' + '─' * (width + 2) + '╯' + RESET

print("\n" * 5)
for line in head:
    time.sleep(0.1)
    print(line.center(50))

time.sleep(0.3)
print(PINK + "       ︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵" + RESET)
time.sleep(0.5)

print(top_bottom)
for line in quote_lines:
    time.sleep(0.2)
    padded = line.ljust(width)
    text = f"{side} {PINK}{BOLD}{padded}{RESET} {side}"
    print_slow(text, 0.02)
print(bottom)

time.sleep(0.5)
print(f"\n{YELLOW}  ~ Woody Allen (probably while having a panic attack) ~{RESET}")
time.sleep(1.5)
print("\n" * 3)