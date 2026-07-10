"""
Campbell's Soup Can #4146
Produced: 2026-07-10 17:07:44
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Colors
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# ASCII Art for Woody Allen's neurotic persona
print(f"{YELLOW}      ,------.")
print(f"{YELLOW}    ,'          '.")
print(f"{YELLOW}   /   O      O   \\")
print(f"{YELLOW}  :                :")
print(f"{YELLOW}  |  ',--------,'  |")
print(f"{YELLOW}  :    `----'    :")
print(f"{YELLOW}   \\  '-......-'  /")
print(f"{YELLOW}    '.          .'")
print(f"{YELLOW}      '-......-'{RESET}")

time.sleep(1)

quote_lines = [
    "I've accepted the universe is indifferent,",
    "but could it at least be consistent?",
    "I check the same spot every morning for meaning,",
    "and it's always the same old existential pothole."
]

max_len = max(len(line) for line in quote_lines)
border = f"{CYAN}+" + "-" * (max_len + 2) + "+"

print(f"{CYAN}{border}{RESET}")
for line in quote_lines:
    padded_line = f"| {line.ljust(max_len)} |"
    print_with_delay(padded_line, 0.03)
print(f"{CYAN}{border}{RESET}")