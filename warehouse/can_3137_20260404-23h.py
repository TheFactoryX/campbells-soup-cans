"""
Campbell's Soup Can #3137
Produced: 2026-04-04 23:46:26
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random
import re

# Clear screen and hide cursor (will be shown again at end)
sys.stdout.write('\033[2J\033[?25l')
sys.stdout.flush()

def strip_ansi(s):
    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)

def typewriter(text, delay=0.03, color='\033[38;5;229m', jitter=0.01):
    """Typewriter effect with random jitter for neurotic vibe"""
    for char in text:
        if char == '\n':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay * 3)
            continue
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter*2))

def draw_neurotic_border(width, char_set='/|\-'):
    """Draw a slightly uneven, neurotic border"""
    sys.stdout.write('\033[38;5;245m')
    pattern = ''.join(random.choice(char_set) for _ in range(width))
    sys.stdout.write('+' + pattern + '+\n')
    sys.stdout.flush()

def draw_wavy_line(width):
    """Draw a wavy line that's never quite straight"""
    sys.stdout.write('\033[38;5;245m')
    for i in range(width):
        if i % 3 == 0:
            sys.stdout.write(random.choice(['~', '·', '⁓']))
        else:
            sys.stdout.write('-')
    sys.stdout.write('\033[0m\n')
    sys.stdout.flush()

# Woody Allen quote (original creation)
quote = """
I was born at an early age.
I've had a perfectly wonderful evening,
but this wasn't it.
I don't want to achieve immortality
through my work; I want to achieve it
through not dying.
"""

# Format and print with neurotic flair
width = max(len(strip_ansi(line)) for line in quote.strip().split('\n')) + 8

sys.stdout.write('\n' * 3)

# Draw neurotic top border
draw_wavy_line(width)
time.sleep(0.2)

# Type the quote with color variations
lines = quote.strip().split('\n')
colors = ['\033[38;5;229m', '\033[38;5;251m', '\033[38;5;180m', '\033[38;5;153m']

for i, line in enumerate(lines):
    padding = (width - len(strip_ansi(line))) // 2
    sys.stdout.write(' ' * padding)
    color = colors[i % len(colors)]
    typewriter(line, delay=0.04, color=color, jitter=0.008)
    time.sleep(0.1)

time.sleep(0.3)

# Draw neurotic bottom border (upside down for extra neurosis)
sys.stdout.write('\033[38;5;245m')
for i in range(width):
    if i % 4 == 0:
        sys.stdout.write(random.choice(['/', '|', '\\', '-']))
    else:
        sys.stdout.write('-')
sys.stdout.write('\033[0m\n')

# Add a tiny, anxious footnote
time.sleep(0.5)
sys.stdout.write('\033[38;5;244m')
typewriter("  (This wisdom brought to you by existential dread)", 
           delay=0.03, color='\033[38;5;244m', jitter=0.005)
sys.stdout.write('\033[0m')

# Show cursor again
sys.stdout.write('\033[?25h')
sys.stdout.flush()

# Keep window open briefly to admire our neurotic masterpiece
time.sleep(2)