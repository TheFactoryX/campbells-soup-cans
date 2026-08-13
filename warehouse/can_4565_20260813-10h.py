"""
Campbell's Soup Can #4565
Produced: 2026-08-13 10:27:39
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, itertools

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def main():
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."
    width = len(quote) + 4
    top = "+" + "-" * (width - 2) + "+"
    bottom = "+" + "-" * (width - 2) + "+"

    # Fun little spinner before the quote appears
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    for _ in range(12):
        sys.stdout.write('\r' + color(next(spinner), '33'))
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write('\r' + '  ' + '\r')  # clear spinner

    # Print colorful box with typewriter effect inside
    print(color(top, '36'))  # cyan top border
    sys.stdout.write('| ')
    sys.stdout.flush()
    for ch in quote:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.045)  # typewriter speed
    sys.stdout.write(' |\\n')
    print(color(bottom, '36'))  # cyan bottom border

if __name__ == "__main__":
    main()