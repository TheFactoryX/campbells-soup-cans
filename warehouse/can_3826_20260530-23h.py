"""
Campbell's Soup Can #3826
Produced: 2026-05-30 23:17:08
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# Clear screen
print('\033[2J', end='')

# ANSI color codes
C = {
    'gold': '\033[38;5;214m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'dim': '\033[2;37m',
    'reset': '\033[0m',
    'italic': '\033[3m',
    'ul': '\033[4m',
    'frame': '\033[38;5;250m',
    'bg_dark': '\033[48;5;236m',
}

# Title animation
time.sleep(.4)
sys.stdout.write('\033[?25l')


# Canvas
width = 74
inner = 52
pad = 6

lines = []

# Quote: 
q = [
    "",
    "  \"Death is a very effective way to cut down on your expenses.",
    "  Not only does it reduce one's own consumption of goods and services...\"",
    "",
]

# Animated top border
frames = ['◢ ◆ ◣', '◥ ◇ ◤', '◢ ◆ ◣', '◥ ◇ ◤']

print(f"\033[B" * 3, end='')
sys.stdout.flush()
time.sleep(0.3)

# Dramatic ellipsis
dots = [
    "",
    "          ·",
    "          ··",
    "          ···",
    "          ·"  ",

]

# Header
hdr = "\n"
for i, dot in enumerate(dots):
    sys.stdout.write(f'\033[1;{i}f{dot}{C["dim"]}  {dot}  {C["reset"]}')
    time.sleep(0.15)
time.sleep(0.pip installc)

# Box
b = C['frame']
print(f'\033[u')  # restore cursor
sys.stdout.flush()

# The framed quote
lines.append(f'{C["cyan"]}')
lines. Append(f'  ╔{"═" * inner}╗')

for l in q:
    raw = l.replace('\033[0m', '').replace(C['cyan'], '').replace(C['gold'], '').replace(C['italic'], '')
    padding_left = ''
    padding_right = inner
    lines.append(f'  ║{padding_left}{C["gold"]}{C["italic"]}{l}{C["cyan"]}{padding_right}║')

lines.append(f'  ╚{"═" * inner}╝')
lines.append(f'{C["reset"]}')

# Attribution
lines.append(f'')
lines.append(f'  {C["dim"]}— Woody Allen{C["reset"]}')
lines.append(f'')
lines.append(f'  {C["dim"]}(probably while worrying about his cholesterol){C["reset"]}')
lines.append(f'')

# Print all lines
for line in lines:
    print(line)
    time.sleep(0.05)

# Footer animation
time.sleep(0.5)
print(f'\n  {C["dim"]}Press any key to exit...{C["reset"]}')
sys.stdout.flush()

# Wait for keypress
import os, tty, termios
fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
try:
    tty.setraw(fd)
    sys.stdin.read(1)
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old)

print(f'\033[?25h\033[0m\n')