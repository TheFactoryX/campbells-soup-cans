"""
Campbell's Soup Can #2238
Produced: 2026-02-15 10:47:31
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap
import time

YELLOW = '\033[93m'
CYAN = '\033[96m'
END = '\033[0m'

brain = [
    "  .-\"\"\"-.  ",
    " /   oo   \\ ",
    "|   \\__/   |",
    "|  .-\"\"-.  |",
    " \\/      \\ /",
    "  '.    .'  ",
    "    '--'    "
]

for line in brain:
    print(YELLOW + line + END)
    time.sleep(0.1)
print()

quote = (
    "I'm not afraid of death; I'm afraid of the waiting room before death. "
    "What if my only entertainment is 'Better Homes and Afterlife' magazine?"
)

width = 45
lines = textwrap.wrap(quote, width=width)
box_width = max(len(line) for line in lines)
if not lines:
    lines = ["Existence: 50% existential dread, 50% wondering why refrigerators hum."]
    box_width = 45

top_bottom = '+' + '-' * (box_width + 2) + '+'
print(YELLOW + top_bottom + END)

for line in lines:
    print(YELLOW + '|' + END, end='', flush=True)
    time.sleep(0.07)
    print(CYAN + ' ', end='', flush=True)
    time.sleep(0.07)
    
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.04)
    padding = box_width - len(line)
    print(' ' * padding + ' ', end='', flush=True)
    
    print(YELLOW + '|' + END)
    time.sleep(0.2)

print(YELLOW + top_bottom + END)
time.sleep(1.5)

print("\n" + CYAN + "  (Neurosis: it's not just for breakfast anymore)" + END)