"""
Campbell's Soup Can #4202
Produced: 2026-07-15 03:34:44
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = [
    "I'm terrified of death,",
    "but I'm even more terrified of not being terrified enough.",
    "It's the only thing that makes me feel...",
    "human."
]

colors = [
    '\033[91m',  # red
    '\033[93m',  # yellow
    '\033[96m',  # cyan
    '\033[92m',  # green
]

border = "+---------------------------------------------------------------+"

print(border)
for i in range(len(quote)):
    line = quote[i]
    color = colors[i]
    reset = '\033[0m'
    print(f"{color}| {line:<61} |{reset}")
    time.sleep(0.5)
print(border)

# Print ASCII art in red
print('\033[91m')
print(r'''
     .-'''''-.
    /  .---.  \
    | /     \ |
    ||       ||
    ||       ||
    |\       /|
     \ '---' /
      '-----'
''')
print('\033[0m')