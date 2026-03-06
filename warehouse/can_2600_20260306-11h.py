"""
Campbell's Soup Can #2600
Produced: 2026-03-06 11:44:09
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

glasses = [
    "  o   o  ",
    "   ---   "
]

quote = "I'm not afraid of death. I'm afraid of arriving late and having to sit through the whole thing."

box_width = 50
inner_width = box_width - 4

words = quote.split()
lines = []
curr_line = ""
for word in words:
    test_line = f"{curr_line} {word}".strip()
    if len(test_line) <= inner_width:
        curr_line = test_line
    else:
        lines.append(curr_line)
        curr_line = word
if curr_line:
    lines.append(curr_line)

centered_lines = [line.center(inner_width) for line in lines]

print('\033[36m', end='', flush=True)
for line in glasses:
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()
print('\033[0m', end='', flush=True)

print('\033[33m', end='', flush=True)
print('┌', end='', flush=True); time.sleep(0.1)
for _ in range(box_width):
    print('─', end='', flush=True); time.sleep(0.05)
print('┐', end='', flush=True); time.sleep(0.1)
print()

for line in centered_lines:
    print('│ ', end='', flush=True); time.sleep(0.05)
    print('\033[37m', end='', flush=True)
    for char in line:
        print(char, end='', flush=True); time.sleep(0.03)
    print('\033[33m', end='', flush=True)
    print(' │', end='', flush=True); time.sleep(0.05)
    print()

print('└', end='', flush=True); time.sleep(0.1)
for _ in range(box_width):
    print('─', end='', flush=True); time.sleep(0.05)
print('┘', flush=True); time.sleep(0.1)
print('\033[0m', flush=True)