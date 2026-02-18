"""
Campbell's Soup Can #2292
Produced: 2026-02-18 09:04:38
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_allen_quote():
    reset = '\033[0m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    bold = '\033[1m'
    
    width = 42
    quote_lines = [
        "  I'm not afraid of death; I'm afraid of the",
        "  afterlife's customer service. They keep",
        "  putting me on hold during my final breath,",
        "  and the hold music is just Kafka reading",
        "  tax code in Yiddish. Meanwhile my soul's",
        "  stuck in limbo with a ticket #4,294,967,295",
        "  watching my life pass by... in standard",
        "  definition. Some immortality!"
    ]
    
    coffee_art = [
        red + "     .-.", 
        red + "    (   )  " + cyan + "Eternal",
        red + "     `-'   " + cyan + "Espresso",
        red + "    _@/_   " + cyan + "Please..."
    ]
    
    sys.stdout.write(yellow + '┌' + '─' * width + '┐' + reset + '\n')
    
    for i in range(9):
        if i == 0:
            sys.stdout.write(yellow + '│' + reset)
            for j in range(width):
                char = ' ' if j % 5 != 0 else '•'
                sys.stdout.write(yellow + char + reset)
                sys.stdout.flush()
                time.sleep(0.005)
            sys.stdout.write(yellow + '│' + reset + '\n')
        elif i == 2:
            for j, line in enumerate(coffee_art):
                padding = ' ' * (width - len(line.replace(reset, '')) - 2)
                sys.stdout.write(yellow + '│ ' + line + padding + yellow + '│' + reset + '\n')
                time.sleep(0.08)
        else:
            line_num = i - 4
            if 0 <= line_num < len(quote_lines):
                quote = quote_lines[line_num]
                padding = ' ' * (width - len(quote) - 1)
                sys.stdout.write(yellow + '│' + reset)
                for char in quote:
                    sys.stdout.write(cyan + char + reset)
                    sys.stdout.flush()
                    time.sleep(0.03)
                sys.stdout.write(padding + yellow + '│' + reset + '\n')
            else:
                sys.stdout.write(yellow + '│' + reset + ' ' * width + yellow + '│' + reset + '\n')
    
    sys.stdout.write(yellow + '└' + '─' * width + '┘' + reset + '\n')
    sys.stdout.write(bold + cyan + '            (A neurotic truth, probably)' + reset + '\n')
    time.sleep(0.5)

if __name__ == "__main__":
    woody_allen_quote()