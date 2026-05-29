"""
Campbell's Soup Can #3813
Produced: 2026-05-29 19:40:27
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

def col(c, txt):
    shades = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'magenta':35,'cyan':36,'white':37}
    return f"\033[{shades.get(c,'37')}m{txt}\033[0m"

border = col('yellow', '+' + '-' * 48 + '+')
empty  = col('cyan',   '|' + ' ' * 48 + '|')
quote_line = col('magenta', '|' + quote.center(48) + '|')

for line in (border, empty, quote_line, empty, border):
    sys.stdout.write(line + '\n')
    sys.stdout.flush()
    time.sleep(0.7)