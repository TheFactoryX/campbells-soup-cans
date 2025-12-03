"""
Campbell's Soup Can #683
Produced: 2025-12-03 08:45:29
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_quote():
    return "I'm not \033[91mafraid\033[0m of \033[92mdeath\033[0m; I just don't want to be there when it \033[93mhappens\033[0m."

def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def boxify(text):
    lines = text.split('\n')
    width = max(len(l) for l in lines)
    top_bottom = '+' + '-' * (width + 2) + '+'
    middle = '|' + ' ' * (width + 2) + '|'
    new_lines = [f"| {l:<{width}} |" for l in lines]
    return '\n'.join([top_bottom, middle] + new_lines + [middle, top_bottom])

def main():
    quote = woody_quote()
    boxed_quote = boxify(quote)
    animate_text(boxed_quote + '\n')

if __name__ == '__main__':
    main()