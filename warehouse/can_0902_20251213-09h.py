"""
Campbell's Soup Can #902
Produced: 2025-12-13 09:31:02
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
    colors = ['\033[93m', '\033[95m']
    border = "\033[94m*" * 60 + "\033[0m"
    face = r'''
       O
       °
       ▽
      / \
    ‘‘‘‘‘‘‘‘
    '''
    
    print("\033[2J\033[H")  # Clear screen
    print("\033[94m" + face + "\033[0m")
    
    print(border)
    for i, char in enumerate(text):
        sys.stdout.write(colors[i%2] + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.08 if char not in ',;.!?' else 0.4)
    print()
    print(border)
    
    # Add blinking existential asterisk
    print("\n\033[5m*\033[0m \033[3m- Woody Allen probably\033[0m \033[5m*\033[0m")

quote = (
    "I'm plagued by existential dread and separation anxiety - "
    "which means I'm equally terrified of the universe's infinite "
    "meaninglessness and my barber taking weekends off."
)

woody_print(quote)