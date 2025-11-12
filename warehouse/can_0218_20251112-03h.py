"""
Campbell's Soup Can #218
Produced: 2025-11-12 03:29:29
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI colour definitions
COL = {
    'reset':   '\033[0m',
    'bright':  '\033[1m',
    'red':     '\033[31m',
    'green':   '\033[32m',
    'yellow':  '\033[33m',
    'blue':    '\033[34m',
    'magenta': '\033[35m',
    'cyan':    '\033[36m',
}

def shout(txt, col='cyan', delay=0.05):
    """Print a string one character at a time with a colour."""
    colour = COL.get(col, COL['cyan'])
    for ch in txt:
        sys.stdout.write(colour + ch + COL['reset'])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# One quirky Woody Allen‑style philosophical line
QUOTE = (
    "I have a premonition that rotting feelings are the only constant; "
    "maybe I'm a philosophical gardener, but the shrubs keep dying before "
    "I can prune them."
)

# Construct a speech‑bubble
content = ' ' + QUOTE + ' '
width = len(content)
top    = COL['magenta'] + '+' + '-' * width + '+' + COL['reset']
middle = COL['magenta'] + '|' + COL['reset'] + content + COL['magenta'] + '|' + COL['reset']
bottom = top

# Animate the bubble
for line in (top, middle, bottom):
    shout(line, col='magenta', delay=0.02)
    time.sleep(0.3)

# Tiny animated tail to mimic a comic‑style speech bubble
frames = ["   ", "  .", "  ..", "  ...", "  ....", "  ...."]
for frame in frames:
    shout(frame, col='magenta', delay=0.03)
    time.sleep(0.1)
