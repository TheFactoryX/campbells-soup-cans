"""
Campbell's Soup Can #1881
Produced: 2026-01-27 13:13:42
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def flush():
    sys.stdout.flush()

def rainbow_quote(text):
    # ANSI foreground colors
    colors = ['\x1b[31m', '\x1b[32m', '\x1b[33m', '\x1b[34m', '\x1b[35m', '\x1b[36m', '\x1b[37m']
    words = text.split()
    for i, word in enumerate(words):
        sys.stdout.write(colors[i % len(colors)] + word + '\x1b[0m')
        if i != len(words) - 1:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('\n')
        flush()
        time.sleep(0.035)   # a little pause for dramatic effect

def draw_box(content):
    width = 34
    border = f"┌{'─' * width}┐"
    middle = f"│ {content.center(width)} │"
    footer = f"└{'─' * width}┘"
    for line in (border, middle, footer):
        print(line)
        flush()

# ASCII‑art title
title = """
      ┌───────────────────────────┐
      │ Woody Allen's             │
      │ Existential Comedy Club  │
      │   (with a side of neurotic)│
      └───────────────────────────┘
"""
print(title)
print()

# The philosophical quote
quote = "I don't think life has any purpose, it's just a series of improbable events ending with a bowl of cereal."
rainbow_quote(quote)

print()
draw_box("That's a funny one!")