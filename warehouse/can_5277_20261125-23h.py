"""
Campbell's Soup Can #5277
Produced: 2026-11-25 23:37:20
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic, colorful Woody Allen-style philosophical quote — pure Python, no deps."""
import time
import sys

# ANSI palette (terminal-safe)
C = {
    'r': '\033[91m',  # red
    'g': '\033[92m',  # green
    'y': '\033[93m',  # yellow
    'b': '\033[94m',  # blue
    'm': '\033[95m',  # magenta
    'c': '\033[96m',  # cyan
    'w': '\033[97m',  # white
    'R': '\033[0m',   # reset
    'B': '\033[1m',   # bold
}

# The quote — neurotic, existential, self-deprecating, very Woody
quote = (
    f"{C['c']}\""
    f"I'm not afraid of death. I just don't want to be there when it happens, "
    f"mostly because I'd spend the whole time wondering if I locked the door, "
    f"paid the rent, and whether the afterlife has a minimum age requirement."
    f"{C['R']}\""
)

# Typewriter effect for that neurotic buildup
def typew(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

if __name__ == '__main__':
    # Colorful ASCII border
    print(f"{C['m']}+{C['B']}{'—'*58}{C['R']}{C['m']}+{C['R']}")
    print(f"{C['m']}|{C['w']}{C['B']}   A WOODY ALLEN MOMENT   {C['R']}{C['m']}|{C['R']}")
    print(f"{C['m']}+{C['B']}{'—'*58}{C['R']}{C['m']}+{C['R']}")
    typew(quote)
    print(f"{C['m']}+{C['B']}{'—'*58}{C['R']}{C['m']}+{C['R']}")
    typew(f"{C['y']}(Deep down, we're all just hoping the checkout line moves faster than eternity.){C['R']}")
    print(f"{C['m']}+{C['B']}{'—'*58}{C['R']}{C['m']}+{C['R']}")
    typew(f"{C['c']}    Remember: if at first you don't succeed, the afterlife has a waiting list.{C['R']}")

/*/
/*
*Note: The above runs cleanly in any standard terminal. 
*Feel free to copy, paste, and enjoy the neurotic vibes.*