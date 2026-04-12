"""
Campbell's Soup Can #3266
Produced: 2026-04-12 23:51:43
Worker: OpenAI: o4 Mini High (openai/o4-mini-high)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, itertools

RESET = '\033[0m'
COLORS = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']

def typewriter(text, color_cycle, delay=0.02):
    for ch in text:
        color = next(color_cycle)
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    quote = "I plan to live forever. So far, so good. But if I do die, don't cry—think of me as just extremely late."
    width = len(quote) + 2
    top = '┌' + '─' * width + '┐'
    mid = '│ ' + quote + ' │'
    bot = '└' + '─' * width + '┘'
    header = '\033[1m\033[35m' + "Woody Allen's Neurotic Epiphany" + RESET

    # Animated header
    for ch in header:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n\n')

    # Animate box
    for line in [top, mid, bot]:
        typewriter(line, itertools.cycle(COLORS), delay=0.01)
    sys.stdout.write('\n')

    # Blinking footer
    blink = '\033[5m'
    footer_text = "Am I late? Or is eternity just running behind?"
    footer = blink + footer_text + RESET
    blank = ' ' * len(footer_text)
    for _ in range(4):
        sys.stdout.write('\r' + footer)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + blank)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\r' + footer + '\n')

if __name__ == '__main__':
    main()