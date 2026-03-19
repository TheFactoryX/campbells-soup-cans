"""
Campbell's Soup Can #2850
Produced: 2026-03-19 18:05:13
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def type_writer(text, delay=0.07, colors=None):
    if colors is None:
        colors = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan
    for i, ch in enumerate(text):
        if ch == '\n':
            sys.stdout.write(ch)
            sys.stdout.flush()
            continue
        color = colors[i % len(colors)]
        sys.stdout.write(f'\x1b[{color}m{ch}\x1b[0m')
        sys.stdout.flush()
        time.sleep(delay)

def main():
    quote = (
        "I'm not pessimistic; I'm just well-informed about how the universe conspires to disappoint me.\n"
        " — A Neurotic Philosopher"
    )
    lines = quote.splitlines()
    width = max(len(line) for line in lines) + 4  # two spaces and two asterisks
    top_bottom = '*' * width

    # top border
    sys.stdout.write('\x1b[36m' + top_bottom + '\x1b[0m\n')
    sys.stdout.flush()
    time.sleep(0.2)

    # quote lines with typing effect
    for line in lines:
        sys.stdout.write('\x1b[36m* \x1b[0m')
        sys.stdout.flush()
        type_writer(line, delay=0.08)
        sys.stdout.write('\x1b[36m *\x1b[0m\n')
        sys.stdout.flush()
        time.sleep(0.1)

    # bottom border
    sys.stdout.write('\x1b[36m' + top_bottom + '\x1b[0m\n')
    sys.stdout.flush()
    time.sleep(0.2)

    # a little neurotic face    face = r"""
          \ \ / / 
           \ V /  
            > <   
           / _ \  
          / / \ \ 
    """
    for ch in face:
        if ch == '\n':
            sys.stdout.write(ch)
            continue        sys.stdout.write('\x1b[33m' + ch + '\x1b[0m')
        sys.stdout.flush()
        time.sleep(0.004)

    print()  # final newline

if __name__ == "__main__":
    main()