"""
Campbell's Soup Can #3459
Produced: 2026-04-26 11:04:16
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ANSI colour codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m',
}

# an ASCII “neurotic” typewriter animation
def typewrite(text, delay=0.08):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != '\n':
            time.sleep(delay)
    print()

def main():
    quote = (
        f"{COLORS['magenta']}“I’ve been thinking—if I die, would I get in the
        server room and find nobody to let me in?  I’d feel so embarrassed
        that even my own mortality would be a punchline.”{COLORS['reset']}"
    )

    border = f"{COLORS['cyan']}┌{'─' * 60}┐{COLORS['reset']}"
    bottom = f"{COLORS['cyan']}└{'─' * 60}┘{COLORS['reset']}"

    print(border)
    # split quote into lines of max width 56 (width minus borders)
    lines = []
    for sentence in quote.split('. '):
        while len(sentence) > 56:
            # find last space within limit
            split_at = sentence.rfind(' ', 0, 56)
            if split_at == -1:
                split_at = 56
            lines.append(sentence[:split_at])
            sentence = sentence[split_at+1:]
        lines.append(sentence)

    for line in lines:
        print(f"{COLORS['green']}│{COLORS['reset']} {line:<56} {COLORS['green']}│{COLORS['reset']}")
    print(bottom)

    # animated punchline reveal
    punchline = (
        f"{COLORS['yellow']}--- I am having an existential crisis—"
        f"  *watch me crumble*"
        f"{COLORS['reset']}"
    )
    time.sleep(1)
    typewrite(punchline, delay=0.12)

if __name__ == "__main__":
    main()
