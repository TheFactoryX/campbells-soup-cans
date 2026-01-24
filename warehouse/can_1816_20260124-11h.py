"""
Campbell's Soup Can #1816
Produced: 2026-01-24 11:29:03
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_print(text):
    colors = {'yellow': '\033[93m', 'red': '\033[91m', 'end': '\033[0m'}
    frame = colors['red'] + r'''
    .-'~~~-.
   .'o  oOOOo`.
   :~~~-.oOo   o`.
    `. \ ~-.  oOOo.
      `.; / ~.  OO:
      .'  ;-- `.o.'
     ,'  ; ~~--'~
     ;  ;
______)_;______
''' + colors['end']
    
    print(frame)
    for char in text:
        sys.stdout.write(colors['yellow'] + char + colors['end'])
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    sys.stdout.write(colors['yellow'] + '_' + colors['end'])
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write('\b \b\n\n')

quote = '''"I'd tell you my theory of existential dread, but\nwhat if we're just background characters\nin someone else's anxiety dream?"'''

woody_print(quote)