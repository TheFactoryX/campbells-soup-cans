"""
Campbell's Soup Can #2838
Produced: 2026-03-19 03:21:04
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# ANSI color codes
CODES = {
    'reset': '\033[0m',
    'cyan': '\033[36m',
    'magenta': '\033[35m',
    'yellow': '\033[33m',
}

def color(text, name):
    return CODES.get(name, '') + text + CODES['reset']

quote = "I was going to write a novel, but I realized I'm just a sentence waiting for punctuation."
border = "ᗢ"
width = len(quote) + 4
top    = border * width
middle = border + " " + quote + " " + borderbottom = border * width

print(color(top, 'cyan'))
print(color(middle, 'magenta'))
print(color(bottom, 'cyan'))