"""
Campbell's Soup Can #1380
Produced: 2026-01-04 06:48:28
Worker: Meta: Llama 3.1 405B Instruct (free) (meta-llama/llama-3.1-405b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote(quote):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }

    ascii_art = """
  ***********************************
  *                                *
  *  {}Woody Allen says:         *
  *                                *
  ***********************************
""".format(colors['blue'])

    animation = "|/-\\"

    sys.stdout.write(ascii_art)
    for i, line in enumerate(quote.splitlines()):
        for j, char in enumerate(line):
            sys.stdout.write("\r{}\n".format(" " * (len(ascii_art.splitlines()[0]) + i)))
            sys.stdout.write("{}{}{}".format(colors['red'], animation[j % len(animation)], colors['end']))
            sys.stdout.write("  {}".format(line[:j]))
            sys.stdout.write("{}{}{}".format(colors['green'], char, colors['end']))
            sys.stdout.write("{}".format(line[j+1:]))
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write("\n")
    sys.stdout.write(colors['end'])

quote = """I'm not sure what's more depressing,
my inevitable demise or
the fact that I'll have to
do my taxes one last time."""

print_quote(quote)