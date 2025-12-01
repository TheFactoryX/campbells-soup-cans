"""
Campbell's Soup Can #652
Produced: 2025-12-01 21:28:25
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, color‑rich Woody Allen‑style philosophical quote.
"""

import sys, time, random

# ANSI colour codes
COL = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'cyan': '\033[96m',
    'magenta': '\033[95m',
    'yellow': '\033[93m',
    'white': '\033[97m',
}

def typewriter(text, delay=0.06):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # Random tiny jitter so it feels a bit alive
        time.sleep(delay + random.uniform(-0.015, 0.015))
    sys.stdout.write('\n')
    sys.stdout.flush()

def box(lines, width=50):
    """Return a string of a coloured box containing the given lines."""
    top = f"{COL['magenta']}+{'-' * (width-2)}+{COL['reset']}"
    middle = [f"{COL['magenta']}|{COL['reset']}{COL['yellow']}{line:<{width-2}}{COL['reset']}{COL['magenta']}|{COL['reset']}"
              for line in lines]
    bottom = f"{COL['magenta']}+{'-' * (width-2)}+{COL['reset']}"
    return '\n'.join([top] + middle + [bottom])

def main():
    header = ["=== Think Before You Exist ===", "", "  Woody Allen  "]
    print(box(header, width=48))

    # Funny philosophical quote in Woody Allen style
    quote = ("I’m terrified of floating on a pillow of panic, "
             "yet I haven’t decided if that alarmingly cute "
             "comfort is worth the existential headache it might bring.")
    typewriter(f"{COL['cyan']}— Woody Allen{COL['reset']}")
    typewriter(quote, delay=0.08)

    # A little animation: a spinning cursor that "rubs the edge of the
    # existential dread" for a split second
    spinner = ['|', '/', '-', '\\']
    print("\nRidiculous existential roller‑coaster:", end=' ', flush=True)
    for _ in range(12):
        for c in spinner:
            sys.stdout.write(f'\b{c}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\b \b\n')
    sys.stdout.flush()

if __name__ == "__main__":
    main()