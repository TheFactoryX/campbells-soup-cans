"""
Campbell's Soup Can #1436
Produced: 2026-01-06 19:29:09
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_woody_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "- Woody Allen"

    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }

    def animate_text(text, color, delay=0.1):
        for char in text:
            sys.stdout.write(f"{colors[color]}{char}{colors['reset']}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def boxed_text(text):
        lines = text.split('\n')
        width = max(len(line) for line in lines)
        print(f"{colors['blue']}┌{'─' * (width + 2)}┐{colors['reset']}")
        for line in lines:
            print(f"{colors['blue']}│ {line.ljust(width)} │{colors['reset']}")
        print(f"{colors['blue']}└{'─' * (width + 2)}┘{colors['reset']}")

    animate_text(quote, 'yellow')
    animate_text(author, 'magenta')
    print()
    animate_text("But wait, there's more!", 'green')
    time.sleep(1)
    print()
    animate_text("A Neo-Dadaist representation of the quote:", 'cyan')
    print()
    time.sleep(1)

    woody_ascii = f"""
         _____
        /     \\
       /       \\
      |  o   o  |
      |    <    |    {colors['red']}I'm not afraid of death;{colors['reset']}
       \  ___  /     {colors['green']}I just don't want to be there when it happens.{colors['reset']}
        \_____/
    """

    boxed_text(woody_ascii)

if __name__ == "__main__":
    print_woody_quote()